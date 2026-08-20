# XI. Plots for Paper Config

<p class="section-updated">Last updated: 19 Aug 2026</p>

This page collects exploratory plots used to investigate how operational InfoEx and AvCan danger levels and avalanche problems align across the four study areas. The overlays highlight candidate analysis windows for the paper configuration work.

## 1. Grid configurations

Method detail lives on [Spatial Config](spatial-config.md). Hex fitting notebook:

<div class="note-box">
<p class="note-box__title">Semi-distributed hex investigation</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_Data/DEM/Semi_distributed_initial_investigation.ipynb">/Users/machtl/Documents/Projects_Data/DEM/Semi_distributed_initial_investigation.ipynb</a>
</div>
</div>

The three HRDPS-based spatial sampling setups compared in the paper:

- **Full grid** — one SNOWPACK run per elevation-corrected HRDPS cell (2.5 km), using a 30 m DEM median height and temperature lapse-rate correction; this is the full spatial distribution of instability.
- **Semi-distributed (15 km hex)** — HRDPS cells are grouped into hexagons (~15 km circumradius); within each hex, forcing is aggregated by elevation band (ALP / TL / BTL) so far fewer simulations are needed.
- **Single point** — one location per operation (station or nearest-cell extract), with a representative ALP / TL / BTL height; lowest compute, no spatial distribution.

<a href="../assets/images/paper_config/fitted_hexes_v2.png" class="glightbox image-zoom" data-gallery="paper-config-hex" data-type="image" data-title="Fitted hexes v2 — Whistler without W7 (other ops unchanged)">
  <img src="../assets/images/paper_config/fitted_hexes_v2.png" alt="Fitted 15 km hexes over Whistler, Rogers Pass, Banff, and MWHS" />
</a>

<p class="fig-caption"><strong>Figure 1.</strong> Fitted hexes v2 (15 km) over the four operations — Whistler without W7; Rogers, Banff, and MWHS unchanged. Click to maximize.</p>

<a href="../assets/images/paper_config/mwhs_domain.png" class="glightbox image-zoom" data-gallery="paper-config-hex" data-type="image" data-title="MWHS domain — HRDPS grid, hex cells M1–M8, and operation boundary">
  <img src="../assets/images/paper_config/mwhs_domain.png" alt="MWHS domain with HRDPS points, hex polygons M1 to M8, and operation boundary" />
</a>

<p class="fig-caption"><strong>Figure 2.</strong> MWHS domain — HRDPS grid points, 15 km hex cells M1–M8, and the operation boundary. Click to maximize.</p>

## 2. Period definition

### 2.1 Whistler

Source notebook:

<div class="note-box">
<p class="note-box__title">InfoEx / AvCan avalanche problems overview</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/infoex/infoex_tools/notebooks/avalanche_problems_overview.ipynb">/Users/machtl/Documents/infoex/infoex_tools/notebooks/avalanche_problems_overview.ipynb</a>
</div>
</div>

<a href="../assets/images/paper_config/whistler_blackcomb.png" class="glightbox image-zoom" data-gallery="paper-config-whistler" data-type="image" data-title="Whistler Blackcomb: InfoEx vs AvCan — danger levels + avalanche problems">
  <img src="../assets/images/paper_config/whistler_blackcomb.png" alt="Whistler Blackcomb InfoEx vs AvCan danger levels and avalanche problems" />
</a>

<p class="fig-caption"><strong>Figure 3.</strong> Whistler Blackcomb — InfoEx vs AvCan danger levels and avalanche problems (winter 2025/26). Orange box marks the candidate analysis period. Click to maximize.</p>

### 2.2 Rogers

<a href="../assets/images/paper_config/rogers_pass.png" class="glightbox image-zoom" data-gallery="paper-config-rogers" data-type="image" data-title="Glacier / Rogers Pass: InfoEx vs AvCan — danger levels + avalanche problems">
  <img src="../assets/images/paper_config/rogers_pass.png" alt="Glacier Rogers Pass InfoEx vs AvCan danger levels and avalanche problems" />
</a>

<p class="fig-caption"><strong>Figure 4.</strong> Glacier / Rogers Pass — InfoEx vs AvCan danger levels and avalanche problems (winter 2025/26). Click to maximize.</p>

### 2.3 Banff

<a href="../assets/images/paper_config/banff.png" class="glightbox image-zoom" data-gallery="paper-config-banff" data-type="image" data-title="Banff: InfoEx vs AvCan — danger levels + avalanche problems">
  <img src="../assets/images/paper_config/banff.png" alt="Banff InfoEx vs AvCan danger levels and avalanche problems" />
</a>

<p class="fig-caption"><strong>Figure 5.</strong> Banff — InfoEx vs AvCan danger levels and avalanche problems (winter 2025/26). Click to maximize.</p>

### 2.4 MWHS

<a href="../assets/images/paper_config/mwhs.png" class="glightbox image-zoom" data-gallery="paper-config-mwhs" data-type="image" data-title="MWHS: InfoEx vs AvCan — danger levels + avalanche problems">
  <img src="../assets/images/paper_config/mwhs.png" alt="MWHS InfoEx vs AvCan danger levels and avalanche problems" />
</a>

<p class="fig-caption"><strong>Figure 6.</strong> MWHS — InfoEx vs AvCan danger levels and avalanche problems (winter 2025/26). Click to maximize.</p>

## 3. Precip Analysis

<div class="note-box">
<p class="note-box__title">Precipitation analysis notebook</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/docker_fun/docs/notebooks/Precip_analysis.ipynb">/Users/machtl/Documents/docker_fun/docs/notebooks/Precip_analysis.ipynb</a>
</div>
</div>

Precipitation (and new-snow) comparison across the three grid configurations for the candidate period.

<details class="table-dropdown">
<summary><strong>3.1 Single median forcing</strong> — click to expand</summary>

Band-median single-point forcing (ALP / TL / BTL): temperature, 24/48 h precipitation, and modeled snow height. Miniatures below; click any panel to maximize.

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_single_whistler.png" class="glightbox image-zoom" data-gallery="paper-config-precip-single" data-type="image" data-title="Whistler · single-point (band median)">
      <img src="../assets/images/paper_config/precip_single_whistler.png" alt="Whistler single-point band median temperature and precipitation" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_single_rogers.png" class="glightbox image-zoom" data-gallery="paper-config-precip-single" data-type="image" data-title="Rogers / GNP · single-point (band median)">
      <img src="../assets/images/paper_config/precip_single_rogers.png" alt="Rogers GNP single-point band median temperature and precipitation" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_single_banff.png" class="glightbox image-zoom" data-gallery="paper-config-precip-single" data-type="image" data-title="Banff · single-point (band median)">
      <img src="../assets/images/paper_config/precip_single_banff.png" alt="Banff single-point band median temperature and precipitation" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_single_mwhs.png" class="glightbox image-zoom" data-gallery="paper-config-precip-single" data-type="image" data-title="MWHS · single-point (band median)">
      <img src="../assets/images/paper_config/precip_single_mwhs.png" alt="MWHS single-point band median temperature and precipitation" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 7.</strong> Single-point (band median) temperature and precipitation / HS by elevation band — Whistler, Rogers / GNP, Banff, and MWHS. Click a miniature to maximize.</p>

</details>

<details class="table-dropdown">
<summary><strong>3.2 Hex approach</strong> — click to expand</summary>

Hex-band forcing for the candidate window (17–31 Dec 2025): TA spaghetti across hexes, plus HN24/48 markers with HS. Miniatures use the small preview scale; click any panel to maximize.

<div class="station-col-grid">
  <div class="station-col">
    <p class="station-col__title">Whistler</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_hex_whistler_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-whistler" data-type="image" data-title="Whistler · hex forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_whistler_ta.png" alt="Whistler hex TA spaghetti ALP TL BTL" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_hex_whistler_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-whistler" data-type="image" data-title="Whistler · hex · HN24/48 markers + HS · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_whistler_hn.png" alt="Whistler hex HN24/48 and HS" />
      </a>
      <span class="pro-evo-grid__label">HN24/48 + HS</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Rogers / GNP</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_hex_rogers_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-rogers" data-type="image" data-title="Rogers / GNP · hex forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_rogers_ta.png" alt="Rogers GNP hex TA spaghetti ALP TL BTL" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_hex_rogers_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-rogers" data-type="image" data-title="Rogers / GNP · hex · HN24/48 markers + HS · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_rogers_hn.png" alt="Rogers GNP hex HN24/48 and HS" />
      </a>
      <span class="pro-evo-grid__label">HN24/48 + HS</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Banff</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_hex_banff_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-banff" data-type="image" data-title="Banff · hex forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_banff_ta.png" alt="Banff hex TA spaghetti ALP TL BTL" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_hex_banff_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-banff" data-type="image" data-title="Banff · hex · HN24/48 markers + HS · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_banff_hn.png" alt="Banff hex HN24/48 and HS" />
      </a>
      <span class="pro-evo-grid__label">HN24/48 + HS</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">MWHS</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_hex_mwhs_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-mwhs" data-type="image" data-title="MWHS · hex forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_mwhs_ta.png" alt="MWHS hex TA spaghetti ALP TL BTL" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_hex_mwhs_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-hex-mwhs" data-type="image" data-title="MWHS · hex · HN24/48 markers + HS · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_hex_mwhs_hn.png" alt="MWHS hex HN24/48 and HS" />
      </a>
      <span class="pro-evo-grid__label">HN24/48 + HS</span>
    </div>
  </div>
</div>

<p class="fig-caption"><strong>Figure 8.</strong> Hex approach — TA spaghetti and HN24/48 + HS by elevation band for Whistler, Rogers / GNP, Banff, and MWHS (17–31 Dec 2025). Click a miniature to maximize.</p>

</details>

<details class="table-dropdown">
<summary><strong>3.3 Full grid</strong> — click to expand</summary>

Full HRDPS-grid forcing for the candidate window (17–31 Dec 2025): TA spaghetti, HN24/48 markers, and HS spaghetti by elevation band. Miniatures use the small preview scale; click any panel to maximize.

<div class="station-col-grid">
  <div class="station-col">
    <p class="station-col__title">Whistler</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_full_whistler_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-whistler" data-type="image" data-title="Whistler · full grid forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_whistler_ta.png" alt="Whistler full grid TA spaghetti" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_full_whistler_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-whistler" data-type="image" data-title="Whistler · full grid · HN24/48 markers · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_whistler_hn.png" alt="Whistler full grid HN24/48 markers" />
      </a>
      <span class="pro-evo-grid__label">HN24/48</span>
      <a href="../assets/images/paper_config/precip_full_whistler_hs.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-whistler" data-type="image" data-title="Whistler · full grid · HS spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_whistler_hs.png" alt="Whistler full grid HS spaghetti" />
      </a>
      <span class="pro-evo-grid__label">HS spaghetti</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Rogers / GNP</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_full_rogers_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-rogers" data-type="image" data-title="Rogers / GNP · full grid forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_rogers_ta.png" alt="Rogers GNP full grid TA spaghetti" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_full_rogers_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-rogers" data-type="image" data-title="Rogers / GNP · full grid · HN24/48 markers · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_rogers_hn.png" alt="Rogers GNP full grid HN24/48 markers" />
      </a>
      <span class="pro-evo-grid__label">HN24/48</span>
      <a href="../assets/images/paper_config/precip_full_rogers_hs.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-rogers" data-type="image" data-title="Rogers / GNP · full grid · HS spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_rogers_hs.png" alt="Rogers GNP full grid HS spaghetti" />
      </a>
      <span class="pro-evo-grid__label">HS spaghetti</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Banff</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_full_banff_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-banff" data-type="image" data-title="Banff · full grid forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_banff_ta.png" alt="Banff full grid TA spaghetti" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_full_banff_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-banff" data-type="image" data-title="Banff · full grid · HN24/48 markers · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_banff_hn.png" alt="Banff full grid HN24/48 markers" />
      </a>
      <span class="pro-evo-grid__label">HN24/48</span>
      <a href="../assets/images/paper_config/precip_full_banff_hs.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-banff" data-type="image" data-title="Banff · full grid · HS spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_banff_hs.png" alt="Banff full grid HS spaghetti" />
      </a>
      <span class="pro-evo-grid__label">HS spaghetti</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">MWHS</p>
    <div class="station-col__figs">
      <a href="../assets/images/paper_config/precip_full_mwhs_ta.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-mwhs" data-type="image" data-title="MWHS · full grid forcing · TA spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_mwhs_ta.png" alt="MWHS full grid TA spaghetti" />
      </a>
      <span class="pro-evo-grid__label">TA spaghetti</span>
      <a href="../assets/images/paper_config/precip_full_mwhs_hn.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-mwhs" data-type="image" data-title="MWHS · full grid · HN24/48 markers · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_mwhs_hn.png" alt="MWHS full grid HN24/48 markers" />
      </a>
      <span class="pro-evo-grid__label">HN24/48</span>
      <a href="../assets/images/paper_config/precip_full_mwhs_hs.png" class="glightbox image-zoom" data-gallery="paper-config-precip-full-mwhs" data-type="image" data-title="MWHS · full grid · HS spaghetti · 2025-12-17 → 2025-12-31">
        <img src="../assets/images/paper_config/precip_full_mwhs_hs.png" alt="MWHS full grid HS spaghetti" />
      </a>
      <span class="pro-evo-grid__label">HS spaghetti</span>
    </div>
  </div>
</div>

<p class="fig-caption"><strong>Figure 9.</strong> Full grid — TA spaghetti, HN24/48 markers, and HS spaghetti by elevation band for Whistler, Rogers / GNP, Banff, and MWHS (17–31 Dec 2025). Click a miniature to maximize.</p>

</details>

## 4. Precip distribution comparison

Side-by-side comparison of single-point, hex (min/median/max), and full-grid distributions for the candidate window. Click any panel to maximize.

### 4.1 Whistler

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_whistler_psum.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-whistler" data-type="image" data-title="Whistler · PSUM 24h · single-point + hex min/median/max + grid percentiles · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_whistler_psum.png" alt="Whistler PSUM 24h distribution comparison" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h lines / markers</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_whistler_hn_box.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-whistler" data-type="image" data-title="Whistler · HN24 · daily grid boxplots + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_whistler_hn_box.png" alt="Whistler HN24 grid boxplots comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_whistler_hn_violin.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-whistler" data-type="image" data-title="Whistler · HN24 · daily grid violins + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_whistler_hn_violin.png" alt="Whistler HN24 grid violins comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid violins</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 10.</strong> Whistler precip distribution comparison (17–31 Dec 2025) — three visualization options: PSUM 24h overlays, HN24 grid boxplots, and HN24 grid violins (each with hex min/median/max and single-point). Click a miniature to maximize.</p>

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_whistler_psum_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-whistler" data-type="image" data-title="Whistler · PSUM_24h · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_whistler_psum_rank.png" alt="Whistler PSUM 24h single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h rank + hex coverage</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_whistler_hn48_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-whistler" data-type="image" data-title="Whistler · HN48 · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_whistler_hn48_rank.png" alt="Whistler HN48 single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">HN48 rank + hex coverage</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 11.</strong> Whistler — single-point rank in the full grid and hex coverage of grid cells (17–31 Dec 2025) for PSUM 24h and HN48. Click a miniature to maximize.</p>

**PSUM 24h** (Whistler, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p43 (rank 10–90: p34–p50; bias −1.143 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 100% of days. Hex contains 61% of grid cells and spans 0.66× the grid p10–p90 width (hex median bias −1.393 mm).
- **Treeline:** single-point sits at grid p44 (rank 10–90: p37–p58; bias −0.916 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 100% of days. Hex contains 51% of grid cells and spans 0.51× the grid p10–p90 width (hex median bias −1.074 mm).
- **Below treeline:** single-point sits at grid p43 (rank 10–90: p35–p82; bias −1.071 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 60% of days. Hex contains 43% of grid cells and spans 0.45× the grid p10–p90 width (hex median bias +0.237 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 77 | 5 | 15 | 15.590 | −1.143 | −1.393 | 42.857 | 34.286 | 49.610 | 100.0 | 100.0 | 100.0 | 60.519 | 0.662 |
| TL | 64 | 5 | 15 | 14.662 | −0.916 | −1.074 | 43.750 | 36.875 | 58.125 | 100.0 | 100.0 | 100.0 | 51.146 | 0.515 |
| BTL | 143 | 4 | 15 | 14.201 | −1.071 | +0.237 | 43.357 | 35.385 | 81.538 | 100.0 | 100.0 | 60.0 | 42.517 | 0.453 |

**HN48** (Whistler, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p56 (rank 10–90: p40–p89; bias +0.004 m vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 100% of days. Hex contains 76% of grid cells and spans 1.21× the grid p10–p90 width (hex median bias −0.002 m).
- **Treeline:** single-point sits at grid p55 (rank 10–90: p38–p81; bias −0.004 m vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 87% of days. Hex contains 62% of grid cells and spans 0.72× the grid p10–p90 width (hex median bias −0.008 m).
- **Below treeline:** single-point sits at grid p69 (rank 10–90: p46–p93; bias +0.014 m vs grid median). Inside grid IQR on 73% of days; inside hex envelope on 80% of days. Hex contains 53% of grid cells and spans 1.32× the grid p10–p90 width (hex median bias +0.047 m).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 45 | 5 | 15 | 0.139 | +0.004 | +0.002 | 55.556 | 30.222 | 97.333 | 86.667 | 100.000 | 100.000 | 77.481 | 1.054 |
| TL | 33 | 5 | 15 | 0.142 | −0.002 | −0.004 | 54.545 | 34.545 | 92.121 | 86.667 | 100.000 | 80.000 | 64.848 | 0.576 |
| BTL | 29 | 4 | 15 | 0.131 | +0.008 | +0.017 | 72.414 | 27.586 | — | — | — | — | — | — |

### 4.2 MWHS

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_mwhs_psum.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-mwhs" data-type="image" data-title="MWHS · PSUM 24h · single-point vs hex vs full-grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_mwhs_psum.png" alt="MWHS PSUM 24h distribution comparison" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h lines / markers</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_mwhs_hn_box.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-mwhs" data-type="image" data-title="MWHS · HN24 · daily grid boxplots + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_mwhs_hn_box.png" alt="MWHS HN24 grid boxplots comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_mwhs_hn_violin.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-mwhs" data-type="image" data-title="MWHS · HN24 · daily grid violins + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_mwhs_hn_violin.png" alt="MWHS HN24 grid violins comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid violins</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 12.</strong> MWHS precip distribution comparison (17–31 Dec 2025) — PSUM 24h overlays, HN24 grid boxplots, and HN24 grid violins. Click a miniature to maximize.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_mwhs_psum_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-mwhs" data-type="image" data-title="MWHS · PSUM_24h · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_mwhs_psum_rank.png" alt="MWHS PSUM 24h single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h rank + hex coverage</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_mwhs_hn24_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-mwhs" data-type="image" data-title="MWHS · HN24 · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_mwhs_hn24_rank.png" alt="MWHS HN24 single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">HN24 rank + hex coverage</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_mwhs_hn48_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-mwhs" data-type="image" data-title="MWHS · HN48 · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_mwhs_hn48_rank.png" alt="MWHS HN48 single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">HN48 rank + hex coverage</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 13.</strong> MWHS — single-point rank in the full grid and hex coverage of grid cells (17–31 Dec 2025) for PSUM 24h, HN24, and HN48. Click a miniature to maximize.</p>

**PSUM 24h** (MWHS, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p47 (rank 10–90: p26–p50; bias −0.741 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 27% of days. Hex contains 27% of grid cells and spans 0.57× the grid p10–p90 width (hex median bias −5.197 mm).
- **Treeline:** single-point sits at grid p39 (rank 10–90: p23–p48; bias −0.993 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 40% of days. Hex contains 27% of grid cells and spans 0.36× the grid p10–p90 width (hex median bias −3.586 mm).
- **Below treeline:** single-point sits at grid p39 (rank 10–90: p26–p49; bias −1.096 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 73% of days. Hex contains 65% of grid cells and spans 0.92× the grid p10–p90 width (hex median bias +0.187 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 55 | 3 | 15 | 12.182 | −0.741 | −5.197 | 47.273 | 26.182 | 50.182 | 86.667 | 100.0 | 26.667 | 26.788 | 0.574 |
| TL | 89 | 4 | 15 | 10.215 | −0.993 | −3.586 | 39.326 | 22.697 | 48.315 | 86.667 | 100.0 | 40.000 | 26.891 | 0.365 |
| BTL | 585 | 6 | 15 | 7.845 | −1.096 | +0.187 | 38.803 | 26.427 | 48.752 | 86.667 | 100.0 | 73.333 | 64.615 | 0.924 |

**HN24** (MWHS, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p43 (rank 10–90: p24–p73; bias −0.011 m vs grid median). Inside grid IQR on 73% of days; inside hex envelope on 40% of days. Hex contains 39% of grid cells and spans 0.59× the grid p10–p90 width (hex median bias −0.047 m).
- **Treeline:** single-point sits at grid p43 (rank 10–90: p24–p67; bias −0.011 m vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 60% of days. Hex contains 40% of grid cells and spans 0.50× the grid p10–p90 width (hex median bias −0.039 m).
- **Below treeline:** single-point sits at grid p27 (rank 10–90: p6–p76; bias −0.027 m vs grid median). Inside grid IQR on 53% of days; inside hex envelope on 80% of days. Hex contains 81% of grid cells and spans 1.04× the grid p10–p90 width (hex median bias −0.010 m).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 55 | 3 | 15 | 0.125 | −0.011 | −0.047 | 42.593 | 24.364 | 72.963 | 73.333 | 100.0 | 40.0 | 39.026 | 0.593 |
| TL | 89 | 4 | 15 | 0.106 | −0.011 | −0.039 | 42.697 | 23.820 | 67.191 | 86.667 | 100.0 | 60.0 | 40.000 | 0.499 |
| BTL | 299 | 6 | 15 | 0.097 | −0.027 | −0.010 | 27.425 | 6.355 | 76.054 | 53.333 | 60.0 | 80.0 | 81.093 | 1.042 |

**HN48** (MWHS, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p39 (rank 10–90: p28–p50; bias −0.022 m vs grid median). Inside grid IQR on 93% of days; inside hex envelope on 27% of days. Hex contains 29% of grid cells and spans 0.61× the grid p10–p90 width (hex median bias −0.102 m).
- **Treeline:** single-point sits at grid p38 (rank 10–90: p26–p49; bias −0.024 m vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 47% of days. Hex contains 31% of grid cells and spans 0.47× the grid p10–p90 width (hex median bias −0.089 m).
- **Below treeline:** single-point sits at grid p19 (rank 10–90: p8–p48; bias −0.058 m vs grid median). Inside grid IQR on 40% of days; inside hex envelope on 80% of days. Hex contains 82% of grid cells and spans 1.16× the grid p10–p90 width (hex median bias −0.023 m).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 55 | 3 | 15 | 0.274 | −0.022 | −0.102 | 38.889 | 27.636 | 50.404 | 93.333 | 100.0 | 26.667 | 28.584 | 0.614 |
| TL | 89 | 4 | 15 | 0.231 | −0.024 | −0.089 | 38.202 | 25.618 | 48.539 | 86.667 | 100.0 | 46.667 | 31.386 | 0.472 |
| BTL | 299 | 6 | 15 | 0.206 | −0.058 | −0.023 | 19.064 | 7.893 | 47.960 | 40.000 | 80.0 | 80.000 | 82.453 | 1.163 |

### 4.3 GNP

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_rogers_psum.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-rogers" data-type="image" data-title="Rogers / GNP · PSUM 24h · single-point vs hex vs full-grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_rogers_psum.png" alt="Rogers GNP PSUM 24h distribution comparison" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h lines / markers</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_rogers_hn_box.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-rogers" data-type="image" data-title="Rogers / GNP · HN24 · daily grid boxplots + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_rogers_hn_box.png" alt="Rogers GNP HN24 grid boxplots comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_rogers_hn_violin.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-rogers" data-type="image" data-title="Rogers / GNP · HN24 · daily grid violins + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_rogers_hn_violin.png" alt="Rogers GNP HN24 grid violins comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid violins</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 14.</strong> Rogers / GNP precip distribution comparison (17–31 Dec 2025) — PSUM 24h overlays, HN24 grid boxplots, and HN24 grid violins. Click a miniature to maximize.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_rogers_psum_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-rogers" data-type="image" data-title="Rogers / GNP · PSUM_24h · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_rogers_psum_rank.png" alt="Rogers GNP PSUM 24h single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h rank + hex coverage</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_rogers_hn24_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-rogers" data-type="image" data-title="Rogers / GNP · HN24 · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_rogers_hn24_rank.png" alt="Rogers GNP HN24 single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">HN24 rank + hex coverage</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_rogers_hn48_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-rogers" data-type="image" data-title="Rogers / GNP · HN48 · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_rogers_hn48_rank.png" alt="Rogers GNP HN48 single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">HN48 rank + hex coverage</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 15.</strong> Rogers / GNP — single-point rank in the full grid and hex coverage of grid cells (17–31 Dec 2025) for PSUM 24h, HN24, and HN48. Click a miniature to maximize.</p>

**PSUM 24h** (Rogers / GNP, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p48 (rank 10–90: p33–p56; bias −0.752 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 7% of days. Hex contains 10% of grid cells and spans 0.16× the grid p10–p90 width (hex median bias −8.279 mm).
- **Treeline:** single-point sits at grid p45 (rank 10–90: p36–p49; bias −1.045 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 13% of days. Hex contains 14% of grid cells and spans 0.11× the grid p10–p90 width (hex median bias −3.777 mm).
- **Below treeline:** single-point sits at grid p45 (rank 10–90: p33–p49; bias −0.832 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 67% of days. Hex contains 32% of grid cells and spans 0.30× the grid p10–p90 width (hex median bias −0.703 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 46 | 2 | 15 | 14.502 | −0.752 | −8.279 | 47.826 | 33.043 | 55.652 | 100.0 | 100.0 | 6.667 | 10.000 | 0.161 |
| TL | 40 | 2 | 15 | 10.425 | −1.045 | −3.777 | 45.000 | 36.000 | 49.000 | 100.0 | 100.0 | 13.333 | 14.333 | 0.112 |
| BTL | 126 | 2 | 15 | 8.742 | −0.832 | −0.703 | 45.238 | 33.016 | 49.206 | 100.0 | 100.0 | 66.667 | 32.381 | 0.296 |

**HN24** (Rogers / GNP, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p50 (rank 10–90: p28–p78; bias −0.006 m vs grid median). Inside grid IQR on 93% of days; inside hex envelope on 13% of days. Hex contains 26% of grid cells and spans 0.20× the grid p10–p90 width (hex median bias −0.072 m).
- **Treeline:** single-point sits at grid p40 (rank 10–90: p31–p87; bias −0.010 m vs grid median). Inside grid IQR on 93% of days; inside hex envelope on 33% of days. Hex contains 27% of grid cells and spans 0.12× the grid p10–p90 width (hex median bias −0.034 m).
- **Below treeline:** single-point sits at grid p36 (rank 10–90: p22–p88; bias −0.023 m vs grid median). Inside grid IQR on 80% of days; inside hex envelope on 73% of days. Hex contains 38% of grid cells and spans 0.39× the grid p10–p90 width (hex median bias −0.023 m).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 46 | 2 | 15 | 0.143 | −0.006 | −0.072 | 50.000 | 27.826 | 77.826 | 93.333 | 100.0 | 13.333 | 25.652 | 0.203 |
| TL | 40 | 2 | 15 | 0.109 | −0.010 | −0.034 | 40.000 | 31.000 | 87.000 | 93.333 | 100.0 | 33.333 | 27.333 | 0.124 |
| BTL | 76 | 2 | 15 | 0.110 | −0.023 | −0.023 | 35.526 | 21.842 | 87.895 | 80.000 | 100.0 | 73.333 | 38.421 | 0.391 |

**HN48** (Rogers / GNP, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p43 (rank 10–90: p32–p50; bias −0.020 m vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 13% of days. Hex contains 16% of grid cells and spans 0.21× the grid p10–p90 width (hex median bias −0.168 m).
- **Treeline:** single-point sits at grid p42 (rank 10–90: p34–p62; bias −0.025 m vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 20% of days. Hex contains 18% of grid cells and spans 0.13× the grid p10–p90 width (hex median bias −0.088 m).
- **Below treeline:** single-point sits at grid p29 (rank 10–90: p23–p57; bias −0.048 m vs grid median). Inside grid IQR on 80% of days; inside hex envelope on 93% of days. Hex contains 34% of grid cells and spans 0.38× the grid p10–p90 width (hex median bias −0.046 m).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 46 | 2 | 15 | 0.320 | −0.020 | −0.168 | 43.478 | 32.174 | 49.565 | 100.0 | 100.0 | 13.333 | 16.087 | 0.210 |
| TL | 40 | 2 | 15 | 0.241 | −0.025 | −0.088 | 42.500 | 33.500 | 62.000 | 100.0 | 100.0 | 20.000 | 18.000 | 0.125 |
| BTL | 76 | 2 | 15 | 0.236 | −0.048 | −0.046 | 28.947 | 23.421 | 57.368 | 80.0 | 100.0 | 93.333 | 33.860 | 0.380 |

### 4.4 Banff

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_banff_psum.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-banff" data-type="image" data-title="Banff · PSUM 24h · single-point vs hex vs full-grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_banff_psum.png" alt="Banff PSUM 24h distribution comparison" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h lines / markers</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_banff_hn_box.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-banff" data-type="image" data-title="Banff · HN24 · daily grid boxplots + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_banff_hn_box.png" alt="Banff HN24 grid boxplots comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_banff_hn_violin.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-banff" data-type="image" data-title="Banff · HN24 · daily grid violins + hex min/median/max + single-point · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_banff_hn_violin.png" alt="Banff HN24 grid violins comparison" />
    </a>
    <span class="pro-evo-grid__label">HN24 grid violins</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 16.</strong> Banff precip distribution comparison (17–31 Dec 2025) — PSUM 24h overlays, HN24 grid boxplots, and HN24 grid violins. Click a miniature to maximize.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_banff_psum_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-banff" data-type="image" data-title="Banff · PSUM_24h · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_banff_psum_rank.png" alt="Banff PSUM 24h single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">PSUM 24h rank + hex coverage</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_banff_hn24_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-banff" data-type="image" data-title="Banff · HN24 · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_banff_hn24_rank.png" alt="Banff HN24 single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">HN24 rank + hex coverage</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_dist_banff_hn48_rank.png" class="glightbox image-zoom" data-gallery="paper-config-precip-dist-banff" data-type="image" data-title="Banff · HN48 · single-point rank in grid | hex coverage of grid · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_dist_banff_hn48_rank.png" alt="Banff HN48 single-point rank and hex coverage" />
    </a>
    <span class="pro-evo-grid__label">HN48 rank + hex coverage</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 17.</strong> Banff — single-point rank in the full grid and hex coverage of grid cells (17–31 Dec 2025) for PSUM 24h, HN24, and HN48. Click a miniature to maximize.</p>

**PSUM 24h** (Banff, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p47 (rank 10–90: p26–p52; bias −0.768 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 13% of days. Hex contains 27% of grid cells and spans 0.42× the grid p10–p90 width (hex median bias −3.113 mm).
- **Treeline:** single-point sits at grid p40 (rank 10–90: p15–p58; bias −0.918 mm vs grid median). Inside grid IQR on 80% of days; inside hex envelope on 60% of days. Hex contains 39% of grid cells and spans 0.36× the grid p10–p90 width (hex median bias −1.589 mm).
- **Below treeline:** single-point sits at grid p38 (rank 10–90: p22–p63; bias −0.981 mm vs grid median). Inside grid IQR on 80% of days; inside hex envelope on 73% of days. Hex contains 52% of grid cells and spans 0.47× the grid p10–p90 width (hex median bias −0.664 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 101 | 3 | 15 | 8.664 | −0.768 | −3.113 | 46.535 | 26.139 | 52.277 | 86.667 | 100.0 | 13.333 | 27.327 | 0.424 |
| TL | 89 | 3 | 15 | 7.472 | −0.918 | −1.589 | 40.449 | 14.607 | 58.202 | 80.000 | 100.0 | 60.000 | 38.951 | 0.362 |
| BTL | 247 | 3 | 15 | 5.950 | −0.981 | −0.664 | 37.652 | 22.267 | 63.401 | 80.000 | 100.0 | 73.333 | 52.200 | 0.472 |

**HN24** (Banff, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p39 (rank 10–90: p18–p95; bias −0.009 m vs grid median). Inside grid IQR on 73% of days; inside hex envelope on 47% of days. Hex contains 46% of grid cells and spans 0.58× the grid p10–p90 width (hex median bias −0.035 m).
- **Treeline:** single-point sits at grid p35 (rank 10–90: p12–p97; bias −0.010 m vs grid median). Inside grid IQR on 73% of days; inside hex envelope on 73% of days. Hex contains 52% of grid cells and spans 0.50× the grid p10–p90 width (hex median bias −0.009 m).
- **Below treeline:** single-point sits at grid p23 (rank 10–90: p14–p97; bias −0.018 m vs grid median). Inside grid IQR on 47% of days; inside hex envelope on 80% of days. Hex contains 66% of grid cells and spans 0.72× the grid p10–p90 width (hex median bias −0.009 m).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 97 | 3 | 15 | 0.095 | −0.009 | −0.035 | 39.175 | 17.938 | 95.258 | 73.333 | 93.333 | 46.667 | 46.323 | 0.583 |
| TL | 78 | 3 | 15 | 0.080 | −0.010 | −0.009 | 34.615 | 12.051 | 96.667 | 73.333 | 93.333 | 73.333 | 51.880 | 0.499 |
| BTL | 174 | 3 | 15 | 0.073 | −0.018 | −0.009 | 22.857 | 14.253 | 97.126 | 46.667 | 93.333 | 80.000 | 65.581 | 0.724 |

**HN48** (Banff, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p37 (rank 10–90: p26–p72; bias −0.021 m vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 27% of days. Hex contains 35% of grid cells and spans 0.50× the grid p10–p90 width (hex median bias −0.067 m).
- **Treeline:** single-point sits at grid p27 (rank 10–90: p11–p70; bias −0.027 m vs grid median). Inside grid IQR on 53% of days; inside hex envelope on 60% of days. Hex contains 34% of grid cells and spans 0.44× the grid p10–p90 width (hex median bias −0.027 m).
- **Below treeline:** single-point sits at grid p14 (rank 10–90: p9–p69; bias −0.038 m vs grid median). Inside grid IQR on 27% of days; inside hex envelope on 73% of days. Hex contains 55% of grid cells and spans 0.66× the grid p10–p90 width (hex median bias −0.014 m).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 97 | 3 | 15 | 0.205 | −0.021 | −0.067 | 37.113 | 26.186 | 72.371 | 86.667 | 100.000 | 26.667 | 35.052 | 0.496 |
| TL | 78 | 3 | 15 | 0.177 | −0.027 | −0.027 | 26.923 | 10.769 | 70.256 | 53.333 | 86.667 | 60.000 | 33.590 | 0.438 |
| BTL | 174 | 3 | 15 | 0.155 | −0.038 | −0.014 | 14.368 | 8.851 | 68.736 | 26.667 | 80.000 | 73.333 | 55.172 | 0.662 |

## 5. Stability distribution analysis

<div class="note-box">
<p class="note-box__title">Stability analysis QMAH</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/docker_fun/docs/notebooks/Stability_analysis_QMAH.ipynb">/Users/machtl/Documents/docker_fun/docs/notebooks/Stability_analysis_QMAH.ipynb</a>
</div>
</div>

QMAH GeoJSON, daily **18:00 UTC**, **all aspects**. Banff window on disk: **20–23 Dec 2025**. Grid boxplots / violins vs hex min–median–max; magenta markers are the operational **station** (Bow Summit, alpine) — not Config III band medians. Slab height is the QMAH critical-layer `depth` (cm); SK38 / Punstable / CCL can pick different layers.

### 5.1 Banff — SK38, Punstable, CCL

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_sk38_box_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff" data-type="image" data-title="Banff · SK38 · daily 18Z all aspects · grid boxplots + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_sk38_box_banff_national_park.png" alt="Banff SK38 grid boxplots vs hex and station" />
    </a>
    <span class="pro-evo-grid__label">SK38 boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_sk38_violin_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff" data-type="image" data-title="Banff · SK38 · daily 18Z all aspects · grid violins + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_sk38_violin_banff_national_park.png" alt="Banff SK38 grid violins vs hex and station" />
    </a>
    <span class="pro-evo-grid__label">SK38 violins</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_punstable_box_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff" data-type="image" data-title="Banff · P unstable · daily 18Z all aspects · grid boxplots + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_punstable_box_banff_national_park.png" alt="Banff Punstable grid boxplots vs hex and station" />
    </a>
    <span class="pro-evo-grid__label">Punstable boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_punstable_violin_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff" data-type="image" data-title="Banff · P unstable · daily 18Z all aspects · grid violins + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_punstable_violin_banff_national_park.png" alt="Banff Punstable grid violins vs hex and station" />
    </a>
    <span class="pro-evo-grid__label">Punstable violins</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_ccl_box_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff" data-type="image" data-title="Banff · Critical cut length (m) · daily 18Z all aspects · grid boxplots + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_ccl_box_banff_national_park.png" alt="Banff CCL grid boxplots vs hex and station" />
    </a>
    <span class="pro-evo-grid__label">CCL boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_ccl_violin_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff" data-type="image" data-title="Banff · Critical cut length (m) · daily 18Z all aspects · grid violins + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_ccl_violin_banff_national_park.png" alt="Banff CCL grid violins vs hex and station" />
    </a>
    <span class="pro-evo-grid__label">CCL violins</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 18.</strong> Banff QMAH — SK38, Punstable, and critical cut length: daily 18Z grid distributions vs hex min/median/max and station (20–23 Dec 2025, all aspects). Click a miniature to maximize.</p>

### 5.2 Banff — slab height (critical-layer depth)

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_sk38_slab_cm_box_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff-slab" data-type="image" data-title="Banff · SK38 slab height (cm) · daily 18Z all aspects · grid boxplots + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_sk38_slab_cm_box_banff_national_park.png" alt="Banff SK38 slab height grid boxplots" />
    </a>
    <span class="pro-evo-grid__label">SK38 slab boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_sk38_slab_cm_violin_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff-slab" data-type="image" data-title="Banff · SK38 slab height (cm) · daily 18Z all aspects · grid violins + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_sk38_slab_cm_violin_banff_national_park.png" alt="Banff SK38 slab height grid violins" />
    </a>
    <span class="pro-evo-grid__label">SK38 slab violins</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_pu_slab_cm_box_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff-slab" data-type="image" data-title="Banff · Punstable slab height (cm) · daily 18Z all aspects · grid boxplots + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_pu_slab_cm_box_banff_national_park.png" alt="Banff Punstable slab height grid boxplots" />
    </a>
    <span class="pro-evo-grid__label">Punstable slab boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_pu_slab_cm_violin_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff-slab" data-type="image" data-title="Banff · Punstable slab height (cm) · daily 18Z all aspects · grid violins + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_pu_slab_cm_violin_banff_national_park.png" alt="Banff Punstable slab height grid violins" />
    </a>
    <span class="pro-evo-grid__label">Punstable slab violins</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_ccl_slab_cm_box_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff-slab" data-type="image" data-title="Banff · CCL slab height (cm) · daily 18Z all aspects · grid boxplots + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_ccl_slab_cm_box_banff_national_park.png" alt="Banff CCL slab height grid boxplots" />
    </a>
    <span class="pro-evo-grid__label">CCL slab boxplots</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_qmah_ccl_slab_cm_violin_banff_national_park.png" class="glightbox image-zoom" data-gallery="paper-config-stab-qmah-banff-slab" data-type="image" data-title="Banff · CCL slab height (cm) · daily 18Z all aspects · grid violins + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_qmah_ccl_slab_cm_violin_banff_national_park.png" alt="Banff CCL slab height grid violins" />
    </a>
    <span class="pro-evo-grid__label">CCL slab violins</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 19.</strong> Banff QMAH — slab height (critical-layer depth, cm) for the SK38, Punstable, and CCL layers: daily 18Z grid distributions vs hex min/median/max and station (20–23 Dec 2025, all aspects). Click a miniature to maximize.</p>

## 6. AvAPro

<div class="note-box">
<p class="note-box__title">AvAPro analysis</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/docker_fun/docs/notebooks/AvAPro_analysis.ipynb">/Users/machtl/Documents/docker_fun/docs/notebooks/AvAPro_analysis.ipynb</a>
</div>
</div>

Daily problem prevalence (grid vs hex vs station) for storm, wind, persistent, and deep persistent — **18:00 UTC**, all aspects. Prevalence is the fraction of cell×aspect samples with the flag (1.0 = every profile in that band). Magenta `x` is the station’s fraction of aspects (alpine / treeline depending on the site).

### 6.1 Whistler — daily prevalence by problem

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_avapro_storm_whistler_combined.png" class="glightbox image-zoom" data-gallery="paper-config-avapro-whistler" data-type="image" data-title="Whistler · Storm slab · daily 18Z all aspects · grid prevalence + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_avapro_storm_whistler_combined.png" alt="Whistler storm slab daily prevalence" />
    </a>
    <span class="pro-evo-grid__label">Storm slab</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_avapro_wind_whistler_combined.png" class="glightbox image-zoom" data-gallery="paper-config-avapro-whistler" data-type="image" data-title="Whistler · Wind slab · daily 18Z all aspects · grid prevalence + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_avapro_wind_whistler_combined.png" alt="Whistler wind slab daily prevalence" />
    </a>
    <span class="pro-evo-grid__label">Wind slab</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_avapro_persistent_whistler_combined.png" class="glightbox image-zoom" data-gallery="paper-config-avapro-whistler" data-type="image" data-title="Whistler · Persistent slab · daily 18Z all aspects · grid prevalence + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_avapro_persistent_whistler_combined.png" alt="Whistler persistent slab daily prevalence" />
    </a>
    <span class="pro-evo-grid__label">Persistent slab</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_avapro_deep_persistent_whistler_combined.png" class="glightbox image-zoom" data-gallery="paper-config-avapro-whistler" data-type="image" data-title="Whistler · Deep persistent · daily 18Z all aspects · grid prevalence + hex min/median/max + station · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/p1_avapro_deep_persistent_whistler_combined.png" alt="Whistler deep persistent daily prevalence" />
    </a>
    <span class="pro-evo-grid__label">Deep persistent</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 20.</strong> Whistler AvAPro — daily 18Z prevalence by problem (grid vs hex min/median/max vs station), 20–23 Dec 2025, all aspects. Click a miniature to maximize.</p>

### 6.2 All operations — snapshot bars and Dec-window timeline

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_avapro_prevalence_bars_2025-12-22_12-00-00.png" class="glightbox image-zoom" data-gallery="paper-config-avapro-ops" data-type="image" data-title="Paper 1 §4.3 — AvAPro prevalence grid vs hex @ 2025-12-22_12-00-00">
      <img src="../assets/images/paper_config/p1_avapro_prevalence_bars_2025-12-22_12-00-00.png" alt="AvAPro prevalence bars grid vs hex 22 Dec 2025 12Z" />
    </a>
    <span class="pro-evo-grid__label">Prevalence bars · 22 Dec 12Z</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/p1_avapro_prevalence_timeline_dec2025.png" class="glightbox image-zoom" data-gallery="paper-config-avapro-ops" data-type="image" data-title="Dec-window timeline: any AvAPro problem prevalence">
      <img src="../assets/images/paper_config/p1_avapro_prevalence_timeline_dec2025.png" alt="Any AvAPro problem prevalence timeline Dec 2025" />
    </a>
    <span class="pro-evo-grid__label">Any-problem timeline</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 21.</strong> All operations — AvAPro prevalence grid vs hex at 22 Dec 2025 12Z, and any-problem fraction through the Dec window (6-hourly). Click a miniature to maximize.</p>

<div class="note-box">
<p class="note-box__title">Timeline CSV</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/docker_fun/docs/figures/p1_avapro_prevalence_timeline_dec2025.csv">/Users/machtl/Documents/docker_fun/docs/figures/p1_avapro_prevalence_timeline_dec2025.csv</a>
 · <a href="../assets/images/paper_config/p1_avapro_prevalence_timeline_dec2025.csv">copy on this site</a>
</div>
</div>

<details class="table-dropdown">
<summary><strong>18:00 UTC extract</strong> — any-problem and storm prevalence (20–23 Dec 2025) — click to expand</summary>

| domain | config | ts | any_problem | storm | n |
|--------|--------|----|-------------|-------|---|
| whistler | grid | 2025-12-20_18-00-00 | 0.928 | 0.659 | 545 |
| whistler | grid | 2025-12-21_18-00-00 | 0.932 | 0.585 | 545 |
| whistler | grid | 2025-12-22_18-00-00 | 0.941 | 0.653 | 545 |
| whistler | grid | 2025-12-23_18-00-00 | 0.982 | 0.716 | 545 |
| whistler | hex | 2025-12-20_18-00-00 | 1.000 | 0.886 | 70 |
| whistler | hex | 2025-12-21_18-00-00 | 1.000 | 0.800 | 70 |
| whistler | hex | 2025-12-22_18-00-00 | 1.000 | 0.857 | 70 |
| whistler | hex | 2025-12-23_18-00-00 | 1.000 | 0.914 | 70 |
| rogers | grid | 2025-12-20_18-00-00 | 0.895 | 0.581 | 640 |
| rogers | grid | 2025-12-21_18-00-00 | 0.891 | 0.494 | 640 |
| rogers | grid | 2025-12-22_18-00-00 | 0.902 | 0.495 | 640 |
| rogers | grid | 2025-12-23_18-00-00 | 0.927 | 0.412 | 640 |
| rogers | hex | 2025-12-20_18-00-00 | 0.567 | 0.067 | 30 |
| rogers | hex | 2025-12-21_18-00-00 | 0.600 | 0.133 | 30 |
| rogers | hex | 2025-12-22_18-00-00 | 0.600 | 0.067 | 30 |
| rogers | hex | 2025-12-23_18-00-00 | 0.667 | 0.000 | 30 |
| mwhs | grid | 2025-12-20_18-00-00 | 0.946 | 0.369 | 1329 |
| mwhs | grid | 2025-12-21_18-00-00 | 0.953 | 0.334 | 1329 |
| mwhs | grid | 2025-12-22_18-00-00 | 0.957 | 0.347 | 1329 |
| mwhs | grid | 2025-12-23_18-00-00 | 0.979 | 0.053 | 1329 |
| mwhs | hex | 2025-12-20_18-00-00 | 0.723 | 0.092 | 65 |
| mwhs | hex | 2025-12-21_18-00-00 | 0.800 | 0.200 | 65 |
| mwhs | hex | 2025-12-22_18-00-00 | 0.723 | 0.277 | 65 |
| mwhs | hex | 2025-12-23_18-00-00 | 0.862 | 0.000 | 65 |
| banff | grid | 2025-12-20_18-00-00 | 0.105 | 0.015 | 1750 |
| banff | grid | 2025-12-21_18-00-00 | 0.102 | 0.014 | 1750 |
| banff | grid | 2025-12-22_18-00-00 | 0.109 | 0.012 | 1750 |
| banff | grid | 2025-12-23_18-00-00 | 0.142 | 0.001 | 1750 |
| banff | hex | 2025-12-20_18-00-00 | 0.756 | 0.044 | 45 |
| banff | hex | 2025-12-21_18-00-00 | 0.756 | 0.067 | 45 |
| banff | hex | 2025-12-22_18-00-00 | 0.911 | 0.000 | 45 |
| banff | hex | 2025-12-23_18-00-00 | 0.933 | 0.000 | 45 |

</details>
