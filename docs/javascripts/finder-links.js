/**
 * Make local file:// links open (reveal) in Finder.
 * - file:// pages: navigate to the folder URL (Finder opens)
 * - http(s) pages: browsers block file://, so copy the folder path
 *   and show a short tip for Go → Go to Folder (⇧⌘G)
 */
(function () {
  function decodeFileUrl(href) {
    try {
      var path = decodeURIComponent(String(href).replace(/^file:\/\//i, ""));
      if (path.indexOf("localhost") === 0) {
        path = path.replace(/^localhost/i, "");
      }
      return path;
    } catch (e) {
      return null;
    }
  }

  function folderPathFor(path) {
    if (!path) return null;
    var cleaned = path.replace(/\/+$/, "") || "/";
    var base = cleaned.split("/").pop() || "";
    // Treat as file if the last segment looks like name.ext
    if (base.indexOf(".") !== -1) {
      var parent = cleaned.replace(/\/[^/]+$/, "");
      return parent || "/";
    }
    return cleaned;
  }

  function folderFileUrl(folderPath) {
    var parts = folderPath.split("/").map(function (p) {
      return encodeURIComponent(p);
    });
    // keep leading slash: "" + "Users" → "/Users/..."
    return "file://" + parts.join("/");
  }

  function showToast(message) {
    var existing = document.getElementById("finder-link-toast");
    if (existing) existing.remove();

    var toast = document.createElement("div");
    toast.id = "finder-link-toast";
    toast.className = "finder-link-toast";
    toast.setAttribute("role", "status");
    toast.textContent = message;
    document.body.appendChild(toast);

    window.setTimeout(function () {
      toast.classList.add("finder-link-toast--visible");
    }, 10);
    window.setTimeout(function () {
      toast.classList.remove("finder-link-toast--visible");
      window.setTimeout(function () {
        toast.remove();
      }, 200);
    }, 3200);
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        resolve();
      } catch (err) {
        reject(err);
      } finally {
        ta.remove();
      }
    });
  }

  function openInFinder(event) {
    var link = event.currentTarget;
    var href = link.getAttribute("href") || "";
    if (!/^file:/i.test(href)) return;

    event.preventDefault();
    event.stopPropagation();

    var path = decodeFileUrl(href);
    var folder = folderPathFor(path);
    if (!folder) return;

    // Local static HTML (opened from Finder): folder file:// opens Finder
    if (window.location.protocol === "file:") {
      window.location.href = folderFileUrl(folder);
      return;
    }

    // mkdocs serve / GitHub Pages: copy path for ⇧⌘G
    copyText(folder)
      .then(function () {
        showToast("Folder path copied — Finder: Go → Go to Folder (⇧⌘G), paste, Go");
      })
      .catch(function () {
        showToast("Open in Finder: " + folder);
      });
  }

  function enhance() {
    var links = document.querySelectorAll('a[href^="file:"], a[href^="FILE:"]');
    links.forEach(function (link) {
      if (link.dataset.finderEnhanced === "1") return;
      link.dataset.finderEnhanced = "1";
      link.classList.add("finder-link");
      link.title = "Open in Finder";
      link.addEventListener("click", openInFinder);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhance);
  } else {
    enhance();
  }
})();
