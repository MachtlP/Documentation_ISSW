# IX. Status Update Aug 6

<p class="section-updated">Last updated: 6 Aug 2026</p>

## 1. Avapro v0

The original AvaPro philosophy was built around **weak-layer tracking from surface formation**: a new-snow burial window looked for the old snow surface under fresh accumulation, then carried that layer forward as a tracked problem. In practice this meant **one NAP and one PAP at a time** — a newer persistent catch typically demoted the previous PAP into a **DAP list** with awkward multi-DAP stacking, while NAP/PAP themselves stayed single-member scalars. Time handling was **pandas-centric**: dry avalanche problems were evaluated only at **drytime** (classically morning, ~9:00 local) and wet problems only at **wettime**, with one dataframe row per calendar day (`df_P` / avaprobs pickles) rather than a continuous hourly stack.

<div class="pro-evo-grid__item pro-evo-grid__item--legend">
  <a href="../assets/images/avapro_v0_flowcharts/legend.png" class="glightbox image-zoom" data-gallery="avapro-v0-flow" data-type="image" data-title="AvaPro v0 flowchart legend">
    <img src="../assets/images/avapro_v0_flowcharts/legend.png" alt="AvaPro v0 flowchart legend" />
  </a>
  <span class="pro-evo-grid__label">Legend</span>
</div>

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_v0_flowcharts/workflow_find_wl.png" class="glightbox image-zoom" data-gallery="avapro-v0-flow" data-type="image" data-title="Workflow: find WL and AvaProblems">
      <img src="../assets/images/avapro_v0_flowcharts/workflow_find_wl.png" alt="Workflow find WL and AvaProblems" />
    </a>
    <span class="pro-evo-grid__label">Find WL / treat prior problems</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_v0_flowcharts/find_new_wl.png" class="glightbox image-zoom" data-gallery="avapro-v0-flow" data-type="image" data-title="Find new WL / problems">
      <img src="../assets/images/avapro_v0_flowcharts/find_new_wl.png" alt="Find new WL and problems flowchart" />
    </a>
    <span class="pro-evo-grid__label">Find new WL / problems</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_v0_flowcharts/post_processing.png" class="glightbox image-zoom" data-gallery="avapro-v0-flow" data-type="image" data-title="Post-processing of detected WLs">
      <img src="../assets/images/avapro_v0_flowcharts/post_processing.png" alt="Post-processing of detected WLs flowchart" />
    </a>
    <span class="pro-evo-grid__label">Post-processing of detected WLs</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 1.</strong> AvaPro v0 flowchart set (legend + find / treat / post-process). Click a miniature to maximize.</p>

## 2. Avapro v1

Current work lives in [`avapro_jul26`](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26) (stacking / RTA / hourly branches under `pap_stack` and `hourly-find-aps`). The philosophy shift is from **single-member surface tracking** to **concurrent weak-layer stacks**, plus an explicit mid-pack **RTA catch** for layers the burial window missed, and a cleaner **DAP** definition instead of “whatever got demoted from PAP.”

### 2.1 Update Compared to v0

#### 2.1.1 NAP (Nap Stacking)

In v0, NAP was a single tracked new-snow weak layer. In v1, NAP is a **list stack**: each new burial catch can **append** a member, near-duplicates (~3 cm height cluster) keep the older formation/burial identity, and day-level problem flags are **OR’d across members**. Because a brief `find_lay` miss used to wipe an older still-viable NAP when a new catch arrived, v1 adds **`napgrace`**: keep last geometry for a few days (3 calendar days; fractional days on the hourly path) with `napcalc = 0` so grace members do not false-trigger while the stack recovers.

#### 2.1.2 PAP (Pap Stacking)

v0 kept one PAP and demoted the previous one into DAP when a newer persistent catch appeared. v1 treats PAP as a **concurrent stack** as well: append + height-cluster dedup, **no automatic demotion to DAP**. Burial-window catches set burial/formation to the catch day; stability / existence flags are OR’d across members. Young buried PAPs (finite burial within ~48 h) can also contribute to NAP-day flags via an early-PAP→NAP path, so a freshly buried persistent grain family is not forced into a false “aging only” lane.

#### 2.1.3 RTA Treatment

Surface burial tracking alone missed weak layers that never showed up as a clean new-snow interface catch. After the burial window, v1 runs a **once-per-day RTA pre-check** (at `drytime` / `rta_hour`): scan for persistent-grain peaks with **RTA ≥ 0.7** (`DH` / `SH` / `FC` / `FCxr`). Hits already near an existing PAP/DAP cluster are skipped; otherwise the layer is appended (as PAP or DAP — see below) with **`burial = NaN`** and **`formation = detection`**. That is the deliberate fix for WLs the old surface-formation philosophy never saw.

#### 2.1.4 DAP (Ground Formation Window and Deep RTA Catch)

v0’s DAP was mostly the aging dump from successive PAP demotions. v1 turns demotion off and refills DAP from RTA when the layer is **near ground** (WL height ≤ ~20 cm) or under a **deep slab** (surface − WL > ~80 cm and not already in a PAP cluster); otherwise the RTA hit stays on the PAP stack. Post-processing applies the same OR / threshold logic to DAP members, so deep or basal persistent structure is a first-class problem rather than a side effect of PAP stacking.

#### 2.1.5 Temporal Resolution

v0 split logic into **drytime** (all dry problems) vs **wettime** (wet only) on a daily pandas row. v1 still uses those gates for burial/RTA (once per day at the dry hour), but the hourly branch writes **one `df_P` row per hour**, runs wet / wind / stack carry at the true stamp, and ages stacks in fractional days (`+1/24`). Post-processing then **`aggregate_ampm()`** into AM **[6, 12)** / PM **[12, 18)** with OR of problem flags, so output stays bulletin-friendly without going back to a single 9:00 dry snapshot for everything.

## 3. Results

### 3.1 Storm Slab

<p class="section-updated">Last updated: 6 Aug 2026</p>

InfoEx Storm vs model NAP (AM/PM) for the four NWP stations. Miniatures use the small preview scale; click any panel to maximize.

<div class="station-col-grid">
  <div class="station-col">
    <p class="station-col__title">Whistler</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_storm_slab/whistler/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Storm Slab (AM/PM) · Whistler Rendezvous · Treeline aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_storm_slab/whistler/overview_ampm.png" alt="Storm Slab AM/PM overview Whistler Rendezvous" />
      </a>
      <span class="pro-evo-grid__label">Overview · TL aspects + hazard</span>
      <a href="../assets/images/results_storm_slab/whistler/detail_N.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Storm Slab detail (AM/PM) · Whistler Rendezvous · N">
        <img src="../assets/images/results_storm_slab/whistler/detail_N.png" alt="Storm Slab detail Whistler N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_storm_slab/whistler/detail_E.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Storm Slab detail (AM/PM) · Whistler Rendezvous · E">
        <img src="../assets/images/results_storm_slab/whistler/detail_E.png" alt="Storm Slab detail Whistler E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_storm_slab/whistler/detail_S.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Storm Slab detail (AM/PM) · Whistler Rendezvous · S">
        <img src="../assets/images/results_storm_slab/whistler/detail_S.png" alt="Storm Slab detail Whistler S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_storm_slab/whistler/detail_W.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Storm Slab detail (AM/PM) · Whistler Rendezvous · W">
        <img src="../assets/images/results_storm_slab/whistler/detail_W.png" alt="Storm Slab detail Whistler W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_storm_slab/whistler/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Trend diagnostics · Whistler Rendezvous · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/whistler/trend_diagnostics.png" alt="Trend diagnostics Whistler Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
      <a href="../assets/images/results_storm_slab/whistler/confusion.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Confusion matrix · Whistler Rendezvous · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/whistler/confusion.png" alt="Confusion matrix Whistler Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Confusion matrix</span>
      <a href="../assets/images/results_storm_slab/whistler/roc_poc.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="ROC / POC · Whistler Rendezvous · InfoEx Storm vs NAP (soft=7d)">
        <img src="../assets/images/results_storm_slab/whistler/roc_poc.png" alt="ROC POC Whistler Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC</span>
      <a href="../assets/images/results_storm_slab/whistler/confusion_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="Confusion matrix · Whistler Rendezvous · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/whistler/confusion_dl2.png" alt="Confusion matrix Whistler Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">Confusion · DL≥2</span>
      <a href="../assets/images/results_storm_slab/whistler/roc_poc_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-whistler" data-type="image" data-title="ROC / POC · Whistler Rendezvous · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/whistler/roc_poc_dl2.png" alt="ROC POC Whistler Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC · DL≥2</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Bow Summit</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_storm_slab/bow_summit/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Storm Slab (AM/PM) · Bow Summit · Treeline aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_storm_slab/bow_summit/overview_ampm.png" alt="Storm Slab AM/PM overview Bow Summit" />
      </a>
      <span class="pro-evo-grid__label">Overview · TL aspects + hazard</span>
      <a href="../assets/images/results_storm_slab/bow_summit/detail_N.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Storm Slab detail (AM/PM) · Bow Summit · N">
        <img src="../assets/images/results_storm_slab/bow_summit/detail_N.png" alt="Storm Slab detail Bow Summit N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_storm_slab/bow_summit/detail_E.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Storm Slab detail (AM/PM) · Bow Summit · E">
        <img src="../assets/images/results_storm_slab/bow_summit/detail_E.png" alt="Storm Slab detail Bow Summit E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_storm_slab/bow_summit/detail_S.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Storm Slab detail (AM/PM) · Bow Summit · S">
        <img src="../assets/images/results_storm_slab/bow_summit/detail_S.png" alt="Storm Slab detail Bow Summit S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_storm_slab/bow_summit/detail_W.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Storm Slab detail (AM/PM) · Bow Summit · W">
        <img src="../assets/images/results_storm_slab/bow_summit/detail_W.png" alt="Storm Slab detail Bow Summit W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_storm_slab/bow_summit/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Trend diagnostics · Bow Summit · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/bow_summit/trend_diagnostics.png" alt="Trend diagnostics Bow Summit Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
      <a href="../assets/images/results_storm_slab/bow_summit/confusion.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Confusion matrix · Bow Summit · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/bow_summit/confusion.png" alt="Confusion matrix Bow Summit Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Confusion matrix</span>
      <a href="../assets/images/results_storm_slab/bow_summit/roc_poc.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="ROC / POC · Bow Summit · InfoEx Storm vs NAP (soft=7d)">
        <img src="../assets/images/results_storm_slab/bow_summit/roc_poc.png" alt="ROC POC Bow Summit Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC</span>
      <a href="../assets/images/results_storm_slab/bow_summit/confusion_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="Confusion matrix · Bow Summit · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/bow_summit/confusion_dl2.png" alt="Confusion matrix Bow Summit Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">Confusion · DL≥2</span>
      <a href="../assets/images/results_storm_slab/bow_summit/roc_poc_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-bow" data-type="image" data-title="ROC / POC · Bow Summit · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/bow_summit/roc_poc_dl2.png" alt="ROC POC Bow Summit Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC · DL≥2</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Fidelity</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_storm_slab/fidelity/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Storm Slab (AM/PM) · Fidelity · Treeline aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_storm_slab/fidelity/overview_ampm.png" alt="Storm Slab AM/PM overview Fidelity" />
      </a>
      <span class="pro-evo-grid__label">Overview · TL aspects + hazard</span>
      <a href="../assets/images/results_storm_slab/fidelity/detail_N.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Storm Slab detail (AM/PM) · Fidelity · N">
        <img src="../assets/images/results_storm_slab/fidelity/detail_N.png" alt="Storm Slab detail Fidelity N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_storm_slab/fidelity/detail_E.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Storm Slab detail (AM/PM) · Fidelity · E">
        <img src="../assets/images/results_storm_slab/fidelity/detail_E.png" alt="Storm Slab detail Fidelity E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_storm_slab/fidelity/detail_S.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Storm Slab detail (AM/PM) · Fidelity · S">
        <img src="../assets/images/results_storm_slab/fidelity/detail_S.png" alt="Storm Slab detail Fidelity S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_storm_slab/fidelity/detail_W.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Storm Slab detail (AM/PM) · Fidelity · W">
        <img src="../assets/images/results_storm_slab/fidelity/detail_W.png" alt="Storm Slab detail Fidelity W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_storm_slab/fidelity/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Trend diagnostics · Fidelity · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/fidelity/trend_diagnostics.png" alt="Trend diagnostics Fidelity Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
      <a href="../assets/images/results_storm_slab/fidelity/confusion.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Confusion matrix · Fidelity · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/fidelity/confusion.png" alt="Confusion matrix Fidelity Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Confusion matrix</span>
      <a href="../assets/images/results_storm_slab/fidelity/roc_poc.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="ROC / POC · Fidelity · InfoEx Storm vs NAP (soft=7d)">
        <img src="../assets/images/results_storm_slab/fidelity/roc_poc.png" alt="ROC POC Fidelity Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC</span>
      <a href="../assets/images/results_storm_slab/fidelity/confusion_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="Confusion matrix · Fidelity · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/fidelity/confusion_dl2.png" alt="Confusion matrix Fidelity Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">Confusion · DL≥2</span>
      <a href="../assets/images/results_storm_slab/fidelity/roc_poc_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-fidelity" data-type="image" data-title="ROC / POC · Fidelity · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/fidelity/roc_poc_dl2.png" alt="ROC POC Fidelity Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC · DL≥2</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">MWHS</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_storm_slab/mwhs/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Storm Slab (AM/PM) · MWHS · Treeline aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_storm_slab/mwhs/overview_ampm.png" alt="Storm Slab AM/PM overview MWHS" />
      </a>
      <span class="pro-evo-grid__label">Overview · TL aspects + hazard</span>
      <a href="../assets/images/results_storm_slab/mwhs/detail_N.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Storm Slab detail (AM/PM) · MWHS · N">
        <img src="../assets/images/results_storm_slab/mwhs/detail_N.png" alt="Storm Slab detail MWHS N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_storm_slab/mwhs/detail_E.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Storm Slab detail (AM/PM) · MWHS · E">
        <img src="../assets/images/results_storm_slab/mwhs/detail_E.png" alt="Storm Slab detail MWHS E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_storm_slab/mwhs/detail_S.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Storm Slab detail (AM/PM) · MWHS · S">
        <img src="../assets/images/results_storm_slab/mwhs/detail_S.png" alt="Storm Slab detail MWHS S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_storm_slab/mwhs/detail_W.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Storm Slab detail (AM/PM) · MWHS · W">
        <img src="../assets/images/results_storm_slab/mwhs/detail_W.png" alt="Storm Slab detail MWHS W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_storm_slab/mwhs/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Trend diagnostics · MWHS · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/mwhs/trend_diagnostics.png" alt="Trend diagnostics MWHS Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
      <a href="../assets/images/results_storm_slab/mwhs/confusion.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Confusion matrix · MWHS · InfoEx Storm vs NAP">
        <img src="../assets/images/results_storm_slab/mwhs/confusion.png" alt="Confusion matrix MWHS Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">Confusion matrix</span>
      <a href="../assets/images/results_storm_slab/mwhs/roc_poc.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="ROC / POC · MWHS · InfoEx Storm vs NAP (soft=7d)">
        <img src="../assets/images/results_storm_slab/mwhs/roc_poc.png" alt="ROC POC MWHS Storm vs NAP" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC</span>
      <a href="../assets/images/results_storm_slab/mwhs/confusion_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="Confusion matrix · MWHS · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/mwhs/confusion_dl2.png" alt="Confusion matrix MWHS Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">Confusion · DL≥2</span>
      <a href="../assets/images/results_storm_slab/mwhs/roc_poc_dl2.png" class="glightbox image-zoom" data-gallery="status-storm-slab-mwhs" data-type="image" data-title="ROC / POC · MWHS · InfoEx Storm vs NAP · DL≥2">
        <img src="../assets/images/results_storm_slab/mwhs/roc_poc_dl2.png" alt="ROC POC MWHS Storm vs NAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC · DL≥2</span>
    </div>
  </div>
</div>

<p class="fig-caption"><strong>Figure 2.</strong> Storm Slab results — Whistler, Bow Summit, Fidelity, and MWHS (overview, N/E/S/W detail, trend diagnostics, confusion / ROC; DL≥2 variants). Same set as Point Location §3.4. Click a miniature to maximize.</p>

### 3.2 Wind Slab

<p class="section-updated">Last updated: 6 Aug 2026</p>

InfoEx Wind vs model WSAP (AM/PM) for the four NWP stations. Miniatures use the small preview scale; click any panel to maximize.

<div class="station-col-grid">
  <div class="station-col">
    <p class="station-col__title">Whistler</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wind_slab/whistler/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Wind Slab (AM/PM) · Whistler_Rendezvous · Alpine wind aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_wind_slab/whistler/overview_ampm.png" alt="Wind Slab (AM/PM) Whistler_Rendezvous Alpine wind aspects + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Alpine aspects + hazard</span>
      <a href="../assets/images/results_wind_slab/whistler/detail_N.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Whistler_Rendezvous · N">
        <img src="../assets/images/results_wind_slab/whistler/detail_N.png" alt="Wind / WSAP detail (AM/PM) Whistler_Rendezvous N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_wind_slab/whistler/detail_E.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Whistler_Rendezvous · E">
        <img src="../assets/images/results_wind_slab/whistler/detail_E.png" alt="Wind / WSAP detail (AM/PM) Whistler_Rendezvous E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_wind_slab/whistler/detail_S.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Whistler_Rendezvous · S">
        <img src="../assets/images/results_wind_slab/whistler/detail_S.png" alt="Wind / WSAP detail (AM/PM) Whistler_Rendezvous S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_wind_slab/whistler/detail_W.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Whistler_Rendezvous · W">
        <img src="../assets/images/results_wind_slab/whistler/detail_W.png" alt="Wind / WSAP detail (AM/PM) Whistler_Rendezvous W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_wind_slab/whistler/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Trend diagnostics · Whistler_Rendezvous · InfoEx Wind vs WSAP">
        <img src="../assets/images/results_wind_slab/whistler/trend_diagnostics.png" alt="Trend diagnostics Whistler_Rendezvous InfoEx Wind vs WSAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
      <a href="../assets/images/results_wind_slab/whistler/confusion.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Confusion matrix · Whistler_Rendezvous · InfoEx Wind vs WSAP">
        <img src="../assets/images/results_wind_slab/whistler/confusion.png" alt="Confusion matrix Whistler_Rendezvous InfoEx Wind vs WSAP" />
      </a>
      <span class="pro-evo-grid__label">Confusion matrix</span>
      <a href="../assets/images/results_wind_slab/whistler/roc_poc.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="ROC / POC · Whistler_Rendezvous · InfoEx Wind vs WSAP (soft=7d)">
        <img src="../assets/images/results_wind_slab/whistler/roc_poc.png" alt="ROC / POC Whistler_Rendezvous InfoEx Wind vs WSAP (soft=7d)" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC</span>
      <a href="../assets/images/results_wind_slab/whistler/confusion_dl2.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="Confusion matrix · Whistler_Rendezvous · InfoEx Wind vs WSAP · DL≥2">
        <img src="../assets/images/results_wind_slab/whistler/confusion_dl2.png" alt="Confusion matrix Whistler_Rendezvous InfoEx Wind vs WSAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">Confusion · DL≥2</span>
      <a href="../assets/images/results_wind_slab/whistler/roc_poc_dl2.png" class="glightbox image-zoom" data-gallery="status-wind-slab-whistler" data-type="image" data-title="ROC / POC · Whistler_Rendezvous · InfoEx Wind vs WSAP · DL≥2">
        <img src="../assets/images/results_wind_slab/whistler/roc_poc_dl2.png" alt="ROC / POC Whistler_Rendezvous InfoEx Wind vs WSAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC · DL≥2</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Bow Summit</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wind_slab/bow_summit/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Wind Slab (AM/PM) · Bow_Summit · Alpine wind aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_wind_slab/bow_summit/overview_ampm.png" alt="Wind Slab (AM/PM) Bow_Summit Alpine wind aspects + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Alpine aspects + hazard</span>
      <a href="../assets/images/results_wind_slab/bow_summit/detail_N.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Bow_Summit · N">
        <img src="../assets/images/results_wind_slab/bow_summit/detail_N.png" alt="Wind / WSAP detail (AM/PM) Bow_Summit N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_wind_slab/bow_summit/detail_E.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Bow_Summit · E">
        <img src="../assets/images/results_wind_slab/bow_summit/detail_E.png" alt="Wind / WSAP detail (AM/PM) Bow_Summit E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_wind_slab/bow_summit/detail_S.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Bow_Summit · S">
        <img src="../assets/images/results_wind_slab/bow_summit/detail_S.png" alt="Wind / WSAP detail (AM/PM) Bow_Summit S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_wind_slab/bow_summit/detail_W.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Bow_Summit · W">
        <img src="../assets/images/results_wind_slab/bow_summit/detail_W.png" alt="Wind / WSAP detail (AM/PM) Bow_Summit W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_wind_slab/bow_summit/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Trend diagnostics · Bow_Summit · InfoEx Wind vs WSAP">
        <img src="../assets/images/results_wind_slab/bow_summit/trend_diagnostics.png" alt="Trend diagnostics Bow_Summit InfoEx Wind vs WSAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
      <a href="../assets/images/results_wind_slab/bow_summit/confusion.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Confusion matrix · Bow_Summit · InfoEx Wind vs WSAP">
        <img src="../assets/images/results_wind_slab/bow_summit/confusion.png" alt="Confusion matrix Bow_Summit InfoEx Wind vs WSAP" />
      </a>
      <span class="pro-evo-grid__label">Confusion matrix</span>
      <a href="../assets/images/results_wind_slab/bow_summit/roc_poc.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="ROC / POC · Bow_Summit · InfoEx Wind vs WSAP (soft=7d)">
        <img src="../assets/images/results_wind_slab/bow_summit/roc_poc.png" alt="ROC / POC Bow_Summit InfoEx Wind vs WSAP (soft=7d)" />
      </a>
      <span class="pro-evo-grid__label">ROC / POC</span>
      <a href="../assets/images/results_wind_slab/bow_summit/confusion_dl2.png" class="glightbox image-zoom" data-gallery="status-wind-slab-bow" data-type="image" data-title="Confusion matrix · Bow_Summit · InfoEx Wind vs WSAP · DL≥2">
        <img src="../assets/images/results_wind_slab/bow_summit/confusion_dl2.png" alt="Confusion matrix Bow_Summit InfoEx Wind vs WSAP DL≥2" />
      </a>
      <span class="pro-evo-grid__label">Confusion · DL≥2</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Fidelity</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wind_slab/fidelity/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wind-slab-fidelity" data-type="image" data-title="Wind Slab (AM/PM) · Fidelity · Alpine wind aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_wind_slab/fidelity/overview_ampm.png" alt="Wind Slab (AM/PM) Fidelity Alpine wind aspects + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Alpine aspects + hazard</span>
      <a href="../assets/images/results_wind_slab/fidelity/detail_N.png" class="glightbox image-zoom" data-gallery="status-wind-slab-fidelity" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Fidelity · N">
        <img src="../assets/images/results_wind_slab/fidelity/detail_N.png" alt="Wind / WSAP detail (AM/PM) Fidelity N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_wind_slab/fidelity/detail_E.png" class="glightbox image-zoom" data-gallery="status-wind-slab-fidelity" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Fidelity · E">
        <img src="../assets/images/results_wind_slab/fidelity/detail_E.png" alt="Wind / WSAP detail (AM/PM) Fidelity E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_wind_slab/fidelity/detail_S.png" class="glightbox image-zoom" data-gallery="status-wind-slab-fidelity" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Fidelity · S">
        <img src="../assets/images/results_wind_slab/fidelity/detail_S.png" alt="Wind / WSAP detail (AM/PM) Fidelity S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_wind_slab/fidelity/detail_W.png" class="glightbox image-zoom" data-gallery="status-wind-slab-fidelity" data-type="image" data-title="Wind / WSAP detail (AM/PM) · Fidelity · W">
        <img src="../assets/images/results_wind_slab/fidelity/detail_W.png" alt="Wind / WSAP detail (AM/PM) Fidelity W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_wind_slab/fidelity/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-wind-slab-fidelity" data-type="image" data-title="Trend diagnostics · Fidelity · InfoEx Wind vs WSAP">
        <img src="../assets/images/results_wind_slab/fidelity/trend_diagnostics.png" alt="Trend diagnostics Fidelity InfoEx Wind vs WSAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">MWHS</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wind_slab/mwhs/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wind-slab-mwhs" data-type="image" data-title="Wind Slab (AM/PM) · MWHS · Alpine wind aspects + TL hazard (InfoEx)">
        <img src="../assets/images/results_wind_slab/mwhs/overview_ampm.png" alt="Wind Slab (AM/PM) MWHS Alpine wind aspects + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Alpine aspects + hazard</span>
      <a href="../assets/images/results_wind_slab/mwhs/detail_N.png" class="glightbox image-zoom" data-gallery="status-wind-slab-mwhs" data-type="image" data-title="Wind / WSAP detail (AM/PM) · MWHS · N">
        <img src="../assets/images/results_wind_slab/mwhs/detail_N.png" alt="Wind / WSAP detail (AM/PM) MWHS N" />
      </a>
      <span class="pro-evo-grid__label">Detail · N</span>
      <a href="../assets/images/results_wind_slab/mwhs/detail_E.png" class="glightbox image-zoom" data-gallery="status-wind-slab-mwhs" data-type="image" data-title="Wind / WSAP detail (AM/PM) · MWHS · E">
        <img src="../assets/images/results_wind_slab/mwhs/detail_E.png" alt="Wind / WSAP detail (AM/PM) MWHS E" />
      </a>
      <span class="pro-evo-grid__label">Detail · E</span>
      <a href="../assets/images/results_wind_slab/mwhs/detail_S.png" class="glightbox image-zoom" data-gallery="status-wind-slab-mwhs" data-type="image" data-title="Wind / WSAP detail (AM/PM) · MWHS · S">
        <img src="../assets/images/results_wind_slab/mwhs/detail_S.png" alt="Wind / WSAP detail (AM/PM) MWHS S" />
      </a>
      <span class="pro-evo-grid__label">Detail · S</span>
      <a href="../assets/images/results_wind_slab/mwhs/detail_W.png" class="glightbox image-zoom" data-gallery="status-wind-slab-mwhs" data-type="image" data-title="Wind / WSAP detail (AM/PM) · MWHS · W">
        <img src="../assets/images/results_wind_slab/mwhs/detail_W.png" alt="Wind / WSAP detail (AM/PM) MWHS W" />
      </a>
      <span class="pro-evo-grid__label">Detail · W</span>
      <a href="../assets/images/results_wind_slab/mwhs/trend_diagnostics.png" class="glightbox image-zoom" data-gallery="status-wind-slab-mwhs" data-type="image" data-title="Trend diagnostics · MWHS · InfoEx Wind vs WSAP">
        <img src="../assets/images/results_wind_slab/mwhs/trend_diagnostics.png" alt="Trend diagnostics MWHS InfoEx Wind vs WSAP" />
      </a>
      <span class="pro-evo-grid__label">Trend diagnostics</span>
      <a href="../assets/images/results_wind_slab/mwhs/confusion.png" class="glightbox image-zoom" data-gallery="status-wind-slab-mwhs" data-type="image" data-title="Confusion matrix · MWHS · InfoEx Wind vs WSAP">
        <img src="../assets/images/results_wind_slab/mwhs/confusion.png" alt="Confusion matrix MWHS InfoEx Wind vs WSAP" />
      </a>
      <span class="pro-evo-grid__label">Confusion matrix</span>
    </div>
  </div>
</div>

<p class="fig-caption"><strong>Figure 3.</strong> Wind Slab results — Whistler, Bow Summit, Fidelity, and MWHS (overview, N/E/S/W detail, trend; confusion / ROC where available). Click a miniature to maximize.</p>

### 3.3 Wet Problems

<p class="section-updated">Last updated: 6 Aug 2026</p>

InfoEx Loose wet + Wet slab vs model WAP (AM/PM) for the four NWP stations. Miniatures use the small preview scale; click any panel to maximize.

<div class="station-col-grid">
  <div class="station-col">
    <p class="station-col__title">Whistler</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wet_problems/whistler/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wet-problems-whistler" data-type="image" data-title="Wet snow (AM/PM) · Whistler_Rendezvous · Treeline Loose wet + Wet slab + TL hazard (InfoEx)">
        <img src="../assets/images/results_wet_problems/whistler/overview_ampm.png" alt="Wet snow (AM/PM) Whistler_Rendezvous Treeline Loose wet + Wet slab + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Treeline aspects + hazard</span>
      <a href="../assets/images/results_wet_problems/whistler/detail_lwc.png" class="glightbox image-zoom" data-gallery="status-wet-problems-whistler" data-type="image" data-title="Wet / WAP detail (AM/PM) · Whistler_Rendezvous · Treeline InfoEx Loose wet + Wet slab">
        <img src="../assets/images/results_wet_problems/whistler/detail_lwc.png" alt="Wet / WAP detail (AM/PM) Whistler_Rendezvous Treeline InfoEx Loose wet + Wet slab" />
      </a>
      <span class="pro-evo-grid__label">Detail · LWC by aspect</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Bow Summit</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wet_problems/bow_summit/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wet-problems-bow" data-type="image" data-title="Wet snow (AM/PM) · Bow_Summit · Treeline Loose wet + Wet slab + TL hazard (InfoEx)">
        <img src="../assets/images/results_wet_problems/bow_summit/overview_ampm.png" alt="Wet snow (AM/PM) Bow_Summit Treeline Loose wet + Wet slab + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Treeline aspects + hazard</span>
      <a href="../assets/images/results_wet_problems/bow_summit/detail_lwc.png" class="glightbox image-zoom" data-gallery="status-wet-problems-bow" data-type="image" data-title="Wet / WAP detail (AM/PM) · Bow_Summit · Treeline InfoEx Loose wet + Wet slab">
        <img src="../assets/images/results_wet_problems/bow_summit/detail_lwc.png" alt="Wet / WAP detail (AM/PM) Bow_Summit Treeline InfoEx Loose wet + Wet slab" />
      </a>
      <span class="pro-evo-grid__label">Detail · LWC by aspect</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">Fidelity</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wet_problems/fidelity/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wet-problems-fidelity" data-type="image" data-title="Wet snow (AM/PM) · Fidelity · Treeline Loose wet + Wet slab + TL hazard (InfoEx)">
        <img src="../assets/images/results_wet_problems/fidelity/overview_ampm.png" alt="Wet snow (AM/PM) Fidelity Treeline Loose wet + Wet slab + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Treeline aspects + hazard</span>
      <a href="../assets/images/results_wet_problems/fidelity/detail_lwc.png" class="glightbox image-zoom" data-gallery="status-wet-problems-fidelity" data-type="image" data-title="Wet / WAP detail (AM/PM) · Fidelity · Treeline InfoEx Loose wet + Wet slab">
        <img src="../assets/images/results_wet_problems/fidelity/detail_lwc.png" alt="Wet / WAP detail (AM/PM) Fidelity Treeline InfoEx Loose wet + Wet slab" />
      </a>
      <span class="pro-evo-grid__label">Detail · LWC by aspect</span>
    </div>
  </div>
  <div class="station-col">
    <p class="station-col__title">MWHS</p>
    <div class="station-col__figs">
      <a href="../assets/images/results_wet_problems/mwhs/overview_ampm.png" class="glightbox image-zoom" data-gallery="status-wet-problems-mwhs" data-type="image" data-title="Wet snow (AM/PM) · MWHS · Treeline Loose wet + Wet slab + TL hazard (InfoEx)">
        <img src="../assets/images/results_wet_problems/mwhs/overview_ampm.png" alt="Wet snow (AM/PM) MWHS Treeline Loose wet + Wet slab + TL hazard (InfoEx)" />
      </a>
      <span class="pro-evo-grid__label">Overview · Treeline aspects + hazard</span>
      <a href="../assets/images/results_wet_problems/mwhs/detail_lwc.png" class="glightbox image-zoom" data-gallery="status-wet-problems-mwhs" data-type="image" data-title="Wet / WAP detail (AM/PM) · MWHS · Treeline InfoEx Loose wet + Wet slab">
        <img src="../assets/images/results_wet_problems/mwhs/detail_lwc.png" alt="Wet / WAP detail (AM/PM) MWHS Treeline InfoEx Loose wet + Wet slab" />
      </a>
      <span class="pro-evo-grid__label">Detail · LWC by aspect</span>
    </div>
  </div>
</div>

<p class="fig-caption"><strong>Figure 4.</strong> Wet Problems results — Whistler, Bow Summit, Fidelity, and MWHS (overview + LWC-by-aspect detail). Click a miniature to maximize.</p>

