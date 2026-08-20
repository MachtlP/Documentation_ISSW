# X. Results / Discussion figures plan

<p class="section-updated">Last updated: 19 Aug 2026</p>

**Date:** 2026-08-19  
**Purpose:** Align on which figures already exist, which still need to be made, and meeting priority for two ISSW 2026 papers.

| Paper | Draft PDF | Primary analysis home |
|-------|-----------|------------------------|
| **P1 — Grid configurations** | [`Grid_Configuarations.pdf`](file:///Users/machtl/Downloads/Grid_Configuarations.pdf) *(filename typo kept)* | AWSOME / hex–grid ops in [`docker_fun`](file:///Users/machtl/Documents/docker_fun), method figures in [`Documentation_ISSW`](spatial-config.md) |
| **P2 — AvAPro stations** | [`AvaPro_Stations.pdf`](file:///Users/machtl/Downloads/AvaPro_Stations.pdf) | [`avapro_jul26`](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26) |

**Dashboard (Dec 2025 showcase window, ~20–24 Dec):**

- **Demo / sharing for supervisor:** open the live ops dashboard on **localhost `:8003`** (user will screen-share localhost). Pages mirror is secondary backup: [https://MachtlP.github.io/awsome_bc/](https://MachtlP.github.io/awsome_bc/).
- Local static site checkout: [`awsome_bc_site/`](file:///Users/machtl/Documents/docker_fun/awsome_bc_site) — README still mentions `python3 -m http.server 8080`; container docs use **:8002** ([`AWSOME_LOCAL_RUN.md`](file:///Users/machtl/Documents/docker_fun/AWSOME_LOCAL_RUN.md)). **Meeting decision: use `:8003`.**
- Showcase includes **hex aggregates** + **point-grid** layers for Whistler / Rogers / Banff / MWHS ([README](file:///Users/machtl/Documents/docker_fun/awsome_bc_site/README.md))

**Supporting docs:** [`Documentation_ISSW/docs/spatial-config.md`](spatial-config.md) · [`status-update-aug-6.md`](status-update-aug-6.md) · Overleaf (spatial): linked from spatial-config.md

**New Paper-1 analysis notebooks (this prep):**

| Notebook | Paper § | Relative | Absolute |
|----------|---------|----------|----------|
| Grid vs hex vs station SK38/Punstable ECDFs + percentiles | §4.2 | [`notebooks/grid_vs_hex_stability_cdf.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb) | [`file:///…/docs/notebooks/grid_vs_hex_stability_cdf.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb) |
| AvAPro prevalence grid vs hex (+ Dec timeline) | §4.3 | [`notebooks/grid_vs_hex_avapro_prevalence.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb) | [`file:///…/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb) |

Figure outputs: [`docs/figures/`](file:///Users/machtl/Documents/docker_fun/docs/figures/) · [`file:///Users/machtl/Documents/docker_fun/docs/figures`](file:///Users/machtl/Documents/docker_fun/docs/figures)

---

## At-a-glance counts (for the meeting)

| | **Existing usable assets** | **Still needed (paper Results/Discussion)** |
|--|---------------------------|-----------------------------------------------|
| **Paper 1** | ~**21** method / setup PNGs + dashboard GeoJSON showcase + **Results notebooks** (ECDF + prevalence) writing to `docs/figures/` — §4.2 Banff QMAH GeoJSON restored & figures re-run; grid AvAPro→GeoJSON merge **complete** (all 4 ops) | **~6–8** remaining polish figures (sim-count graphic, InfoEx overlay, four-op plate polish, dashboard screenshot plate) |
| **Paper 2** | **~80** curated InfoEx-comparison PNGs + **~97** station gallery PNGs + **18** station AM/PM MAIN + **18** NWP-vs-station + **4** decision-tree SVGs + **37** SARP evo stacks | **~8–10** synthesis figures (metrics tables/heatmaps all ops, timing/onset with **±1** tolerance, persistent package polish, forcing sensitivity summary) |

---

# Paper 1 — Grid configurations

**Working title (from PDF):** *How does grid configuration influence snowpack representation? Exploring spatial sampling strategies for distributed snowpack modelling*

**Configs in draft:** (I) full HRDPS grid · (II) semi-distributed **15 km hex** + elevation bands · (III) **single-point = downscaled data for 1 location** (station / nearest-cell extract — **not** terrain-informed). Ops: WB, GNP/Rogers, MWHS, Banff.

**Earlier analysis intent (critical window):** compare full-grid vs hex vs stations on SK38 / Punstable (+ AvAPro problems); place station as **percentile within grid/hex CDF**; use Dec 2025 showcase data on the dashboard.

## Results / Discussion outline (from PDF placeholders)

| § | PDF heading | Figure job |
|---|-------------|---------|
| **4.1** | Spatial representation and reduction in simulations | Counts of forcing locations / SNOWPACK runs; % reduction hex & single-point vs full grid |
| **4.2** | Representation of snowpack stability | CDFs / violins of SK38, CCL, Punstable by config × elev band × aspect; unstable-tail capture by hex; **station percentile on full-grid (and hex) CDF** |
| **4.3** | Representation of avalanche problems | Prevalence (fraction of cells/sims with problem) full-grid vs hex; single-point hit/miss vs domain prevalence |
| **4.4** | Comparison with operational assessments | InfoEx / CMAH for selected instability periods (incl. Dec 2025 window) |
| **4.5** | Comparison across study regions | Same metrics across maritime → continental |
| **5.1–5.4** | Discussion | Aggregation information loss; single-point representativeness; ops compute trade-off (**single-machine** runs — no multi-node comparison); limitations (Banff QMAH, AvAPro grid coverage) |

### Interpretation by Results subsection

- **§4.1** — Hex and 1-location configs exist to cut SNOWPACK count vs full HRDPS; the figure should make the % reduction claim visual and domain-comparable.
- **§4.2** — Grid CDF = reference stability distribution; hex should retain shape + **unstable wing**; station value = **percentile** in that distribution (representativeness of one location).
- **§4.3** — Problem **prevalence** (fraction of aspect-samples with AvAPro flag) should be similar for hex vs grid if aggregation preserves occurrence rates; station is hit/miss against domain prevalence.
- **§4.4–4.5** — Same diagnostics across ops / vs InfoEx for the Dec 2025 window; Banff panels may need a post-retry refresh.

## Existing plots / notebooks (Paper 1)

### A. Method / study-area figures (ready for Methods; some usable as Results setup)

Base dir: [`Documentation_ISSW/docs/assets/images/`](assets/images/)  
Catalogued in: [`spatial-config.md`](spatial-config.md)

| ID | Description | Figure file | Notebook / script |
|----|-------------|----------------|-------------------|
| G1 | HRDPS orography, 4 ops | [dem_hrdps_orography_sites.png](assets/images/dem_hrdps_orography_sites.png) | [explore_dem_topography.ipynb](file:///Users/machtl/Documents/Projects_Data/DEM/explore_dem_topography.ipynb) |
| G2 | HRDPS elevation bands | [dem_elevation_bands.png](assets/images/dem_elevation_bands.png) | same |
| G3 | HRDPS hypsometry | [dem_hypsometry.png](assets/images/dem_hypsometry.png) | same |
| G4–G6 | MRDEM-30 orography / bands / hypsometry | [mrdem30_orography_sites.png](assets/images/mrdem30_orography_sites.png) · [mrdem30_elevation_bands.png](assets/images/mrdem30_elevation_bands.png) · [mrdem30_hypsometry.png](assets/images/mrdem30_hypsometry.png) | [download_mrdem30…](file:///Users/machtl/Documents/Projects_Data/DEM/download_mrdem30_for_research_areas.ipynb) + explore DEM |
| G7–G10 | Elevation correction Δz, corrected orography/bands, hypsometry compare | [hrdps_elevation_correction_delta.png](assets/images/hrdps_elevation_correction_delta.png) · [hrdps_corrected_orography.png](assets/images/hrdps_corrected_orography.png) · [hrdps_corrected_elevation_bands.png](assets/images/hrdps_corrected_elevation_bands.png) · [hypsometry_hrdps_mrdem30_corrected.png](assets/images/hypsometry_hrdps_mrdem30_corrected.png) | DEM notebooks |
| G13–G14 | Lapse-rate TA/RH example (Whistler) | [lapse_rate_ta_whistler_example.png](assets/images/lapse_rate_ta_whistler_example.png) · [lapse_rate_rh_whistler_example.png](assets/images/lapse_rate_rh_whistler_example.png) | [Lapsrate_correction.ipynb](file:///Users/machtl/Documents/Projects_Data/DEM/Lapsrate_correction.ipynb) · [`grib2smet.py`](file:///Users/machtl/Documents/Projects_Data/DEM/grib2smet.py) |
| G16–G18 | Hex domain three-zone, HRDPS-in-hex, Whistler per-hex hypsometry | [semidist_hex_three_zone.png](assets/images/semidist_hex_three_zone.png) · [semidist_hex_hrdps_points.png](assets/images/semidist_hex_hrdps_points.png) · [semidist_hex_hypsometry_whistler.png](assets/images/semidist_hex_hypsometry_whistler.png) | [Semi_distributed_initial_investigation.ipynb](file:///Users/machtl/Documents/Projects_Data/DEM/Semi_distributed_initial_investigation.ipynb) · also [HRDPS_hex_grid_to_SMET.ipynb](file:///Users/machtl/Documents/Projects_Data/DEM/HRDPS_hex_grid_to_SMET.ipynb) |
| G20 | Single-point / 1-location anchors (Whistler) | [singlepoint_band_whistler.png](assets/images/singlepoint_band_whistler.png) | [Spatial_to_single_point.ipynb](file:///Users/machtl/Documents/Projects_Data/DEM/Spatial_to_single_point.ipynb) · [extract_single_point_HRDPS_to_SMET_elevation_corrected.ipynb](file:///Users/machtl/Documents/Projects_Data/DEM/extract_single_point_HRDPS_to_SMET_elevation_corrected.ipynb) |

**Interpretation (Methods group A):** These establish *how* configs are built (orography, bands, hex aggregation, 1-location downscale). They support Methods and §4.1 setup — they do **not** replace Results CDFs/prevalence.

~~G21 PRA / terrain-informed (Lake Louise)~~ — **dropped from needed figures** (we do not do terrain-informed for these papers). Placeholder PNG may remain in assets but is not a Results target.

### B. Ops / dashboard pipeline (data + interactive viz)

| Asset | Path | Notes |
|-------|------|-------|
| Hex staging / QMAH runners | [`stage_hex_ops.py`](file:///Users/machtl/Documents/docker_fun/stage_hex_ops.py), [`run_hex_ops.py`](file:///Users/machtl/Documents/docker_fun/run_hex_ops.py), [`run_whistler_hex.py`](file:///Users/machtl/Documents/docker_fun/run_whistler_hex.py) | Dec-window hex SNOWPACK + QMAH |
| Publish hex Pros → Pages | [`publish_hex_pros_to_pages.py`](file:///Users/machtl/Documents/docker_fun/publish_hex_pros_to_pages.py) | NiViz-style aspects |
| Stage / merge AvAPro into hex & grid GeoJSON | [`stage_hex_for_avapro.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/stage_hex_for_avapro.py), [`merge_avapro_into_hex_geojson.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/merge_avapro_into_hex_geojson.py), [`stage_grid_for_avapro.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/stage_grid_for_avapro.py), [`run_grid_avapro_F4.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/run_grid_avapro_F4.py) | Full-grid AvAPro F+4 |
| AvAPro outputs (grid) | [`avapro_jul26_stations/output_grid/`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/output_grid) | Counts evolve during retry |
| AvAPro outputs (hex) | [`avapro_jul26_stations/output_hex/`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/output_hex) | Smaller: ~6–14 vstations/domain |
| External domain data | [`~/awsome_external/`](file:///Users/machtl/awsome_external) | `*_hex` and point domains present |
| Live www mount | [`~/awsome/jul26_www/`](file:///Users/machtl/awsome/jul26_www) | Preferred live GeoJSON; Rogers grid may fall back to site snapshot |
| Static dashboard | **localhost `:8003`** (demo) · [Pages](https://MachtlP.github.io/awsome_bc/) · [`awsome_bc_site/`](file:///Users/machtl/Documents/docker_fun/awsome_bc_site) | Dec 20–24 2025 GeoJSON time steps |

**Interpretation (group B):** Interactive layers are the Dec 2025 evidence base for §4.2–4.5; static paper figures are produced from the same GeoJSON via the notebooks below.

### C. Paper-1 Results analysis notebooks (CREATED)

| Notebook | Role | Example outputs |
|----------|------|-----------------|
| [`grid_vs_hex_stability_cdf.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb) ([abs](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb)) | §4.2 ECDFs + station percentiles + unstable-tail bars | [`p1_grid_hex_station_ecdf_2025-12-22_12-00-00.png`](file:///Users/machtl/Documents/docker_fun/docs/figures/p1_grid_hex_station_ecdf_2025-12-22_12-00-00.png) · [`p1_unstable_tail_….png`](file:///Users/machtl/Documents/docker_fun/docs/figures/p1_unstable_tail_2025-12-22_12-00-00.png) · [`p1_station_percentiles_….csv`](file:///Users/machtl/Documents/docker_fun/docs/figures/p1_station_percentiles_2025-12-22_12-00-00.csv) |
| [`grid_vs_hex_avapro_prevalence.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb) ([abs](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb)) | §4.3 prevalence bars + Dec timeline + station hit/miss | [`p1_avapro_prevalence_bars_….png`](file:///Users/machtl/Documents/docker_fun/docs/figures/p1_avapro_prevalence_bars_2025-12-22_12-00-00.png) · [`p1_avapro_prevalence_timeline_dec2025.png`](file:///Users/machtl/Documents/docker_fun/docs/figures/p1_avapro_prevalence_timeline_dec2025.png) |

**Interpretation:** These notebooks implement the core Results claims for stability distributions and problem prevalence. Status: [`qmah_avapro_retry_status.json`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/qmah_avapro_retry_status.json) — original retry PIDs are **not alive**; Banff Dec-window QMAH GeoJSON usable for §4.2. Grid AvAPro→GeoJSON merge via [`merge_avapro_into_grid_geojson.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/merge_avapro_into_grid_geojson.py) **finished for all 4 ops**; prevalence figures refreshed.

### D. Related stability stacks (station/NWP points — support narrative)

| Description | Path | Notebook |
|-------------|------|----------|
| SK38 / Punstable SARP evo stacks (4 stations × aspects) | [`plots_for_ISSW26/pngs/`](file:///Users/machtl/Documents/Projects_PhD/plots_for_ISSW26/pngs) (37 PNGs) | [`initial_snowpack_investigation.ipynb`](file:///Users/machtl/Documents/Projects_PhD/plots_for_ISSW26/initial_snowpack_investigation.ipynb) |

### E. Single-point / 1-location config assets (Config III) — already exist

| Asset | Link |
|-------|------|
| Method map | [`singlepoint_band_whistler.png`](assets/images/singlepoint_band_whistler.png) |
| Spatial → single-point notebook | [`Spatial_to_single_point.ipynb`](file:///Users/machtl/Documents/Projects_Data/DEM/Spatial_to_single_point.ipynb) |
| Extract 1-location HRDPS→SMET | [`extract_single_point_HRDPS_to_SMET_elevation_corrected.ipynb`](file:///Users/machtl/Documents/Projects_Data/DEM/extract_single_point_HRDPS_to_SMET_elevation_corrected.ipynb) |
| Band-median SMETs (per op) | [`/Volumes/Machtl_1.1/SMET/band_medians/`](file:///Volumes/Machtl_1.1/SMET/band_medians/) (e.g. `whistler_combined/{BTL,TL,ALP}.smet`) |
| Dashboard station layers | `whistler_station`, `fidelity_station`, `lookout_station`, `bowsummit_station` under [`jul26_www`](file:///Users/machtl/awsome/jul26_www) / [`awsome_bc_site`](file:///Users/machtl/Documents/docker_fun/awsome_bc_site) |

**Interpretation:** Config III is **one location’s downscaled forcing**, not a PRA/terrain-informed sampler. Station GeoJSON layers are the operational single-point QMAH surfaces used in §4.2 percentile overlays.

## Still needed (Paper 1) — purpose + suggested home

| Priority | Figure (Results) | Purpose | Suggested create-in | Status |
|----------|----------------|---------|---------------------|--------|
| **P1-1** | Simulation-count bar / table graphic | §4.1 — XX–XX% reduction claim | New small notebook under `docs/notebooks/` reading vstations counts | Still open |
| **P1-2** | SK38 & Punstable CDFs (grid vs hex vs single-point) | §4.2 core | [`grid_vs_hex_stability_cdf.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb) | **Done** (incl. Banff QMAH) — re-run if GeoJSON updates |
| **P1-3** | Station **percentile markers on CDFs** | §4.2 | Same notebook | **Done** |
| **P1-4** | Unstable-tail panel | Does hex retain unstable wing? | Same notebook | **Done** |
| **P1-5** | AvAPro prevalence bars by problem | §4.3 | [`grid_vs_hex_avapro_prevalence.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb) | **Done** (all 4 ops grid-merged) |
| **P1-6** | Timeline: problem prevalence grid vs hex | Temporal evolution | Same notebook | **Done** (all 4 ops) |
| **P1-7** | InfoEx / forecast comparison for showcase period | §4.4 | Pull InfoEx pickles + overlay prevalence | Still open |
| **P1-8** | Four-op small-multiple polish of P1-2/P1-3 | §4.5 | Facet polish in CDF notebook | Partial (already faceted) |
| **P1-9** | Dashboard screenshot plate (hex + grid + station pins) | Discussion / graphical abstract | Manual from **localhost `:8003`** (Pages backup) | Still open |
| ~~**P1-10**~~ | ~~PRA terrain-informed sampling~~ | — | — | **Removed** — we don’t do terrain-informed |

---

# Paper 2 — AvAPro stations

**Working title (from PDF):** *Exploring physics-based avalanche problem identification from SNOWPACK simulations across multiple snow climates in western Canada*

**Setup:** Point SNOWPACK at WB / Rogers (Fidelity) / MWHS / Banff (Bow Summit); station-driven vs HRDPS-driven; verify vs InfoEx; timing of onset/end; metrics POD/FAR/CSI/bias.

## Results / Discussion outline (from PDF)

| § | PDF heading | Figure job |
|---|-------------|---------|
| **4.1** | Seasonal evolution across snow climates | Multi-op AM/PM problem timelines + InfoEx |
| **4.2** | Day-exact agreement | Contingency / POD–FAR–CSI by problem × aspect (± pooled) |
| **4.3** | Timing and persistence | Onset Δt histograms; spell IoU; **timing tolerance ±1** (day / AM–PM period as used in notebooks — document ±1 clearly in captions) |
| **4.4** | Sensitivity to meteorological forcing | NWP vs station agreement / Jaccard / disagreement case |
| **5.x** | Discussion | Physics-based ID, climate differences, temporal value, forcing, ops value, limits |

### Interpretation by Results subsection

- **§4.1** — Seasonal AM/PM problem timelines show climate contrast; InfoEx elev bands are the verification backdrop.
- **§4.2** — Day-exact contingency metrics answer “does AvAPro fire on the right days?”
- **§4.3** — Timing value beyond exact-day: use **±1** tolerant scores as the finalized window (not ±3/±7 for the main paper claim unless supplement).
- **§4.4** — Station vs NWP forcing: agreement heatmaps + 1–2 disagreement cases.

## Existing plots / notebooks (Paper 2)

### A. Curated status-update / ISSW doc figures (best “paper-ready” set)

Base: [`Documentation_ISSW/docs/assets/images/`](assets/images/)  
Narrated in: [`status-update-aug-6.md`](status-update-aug-6.md)

| Set | Description | Example links | Approx. n |
|-----|-------------|---------------|-----------|
| Storm slab vs InfoEx | overview AM/PM, aspect detail, trend, confusion, ROC | [whistler/overview_ampm.png](assets/images/results_storm_slab/whistler/overview_ampm.png) · folder [results_storm_slab/](assets/images/results_storm_slab) | **40** |
| Wind slab vs InfoEx | same structure | [results_wind_slab/](assets/images/results_wind_slab) | **32** |
| Wet problems vs InfoEx | overview-focused | [results_wet_problems/](assets/images/results_wet_problems) | **8** |
| Station galleries (overview / NAP / PAP / wind / wet) | per-op aspect panels | [avapro_whistler/](assets/images/avapro_whistler) · [avapro_fidelity/](assets/images/avapro_fidelity) · [avapro_bow_summit/](assets/images/avapro_bow_summit) · [avapro_mwhs/](assets/images/avapro_mwhs) | **~97** |
| AvaPro v0 flowcharts | methods schematic | [avapro_v0_flowcharts/](assets/images/avapro_v0_flowcharts) | **4** |
| NWP PRO galleries | profile stacks | [nwp_pro_whistler_rendezvous/](assets/images/nwp_pro_whistler_rendezvous) (+ bow/fidelity/mwhs) | **36** |

**Interpretation (curated P2 set):** Storm/wind packages are the strongest paper-ready evidence; wet/persistent need parity; galleries support Methods/supplement.

### B. Active figure notebooks (`avapro_jul26`)

| Notebook | Role | Saved outputs |
|----------|------|---------------|
| [Avapro_AMPM_MAIN.ipynb](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_AMPM_MAIN.ipynb) | §4.1 seasonal AM/PM + InfoEx elev bands | [output_plots/AMPM_MAIN_station/](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/output_plots/AMPM_MAIN_station) (**18** PNGs: Whistler, Fidelity, Bow_Summit) · `AMPM_MAIN/` dir exists but empty (NWP save not flushed) |
| [Avapro_NWP_vs_Station_compare.ipynb](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_NWP_vs_Station_compare.ipynb) | §4.4 forcing sensitivity | [output_plots/nwp_vs_station/](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/output_plots/nwp_vs_station) — e.g. [heatmap_agree.png](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/output_plots/nwp_vs_station/heatmap_agree.png), [heatmap_jaccard.png](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/output_plots/nwp_vs_station/heatmap_jaccard.png), bars + diff timelines + CSVs |
| [Whistler/Avapro_AMPM_*_infoex_stats.ipynb](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Whistler) (Storm / Wind / Wet / Persistent) | §4.2–4.3 Whistler verification | `SAVE_FIGURES=False` by default; curated copies live under Documentation_ISSW `results_*` |
| [Whistler/Avapro_Persistent_infoex_comp.ipynb](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Whistler/Avapro_Persistent_infoex_comp.ipynb) | Persistent daily companion | No dedicated `results_persistent_slab/` folder found under Documentation_ISSW assets |
| Decision trees | Methods | [decision_tree/*.svg](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/decision_tree) · [generate_avapro_decision_tree.py](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/decision_tree/generate_avapro_decision_tree.py) |
| Legacy / graveyard | Older pap_stack & IGS plots | [figure_notebooks/graveyard/](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/graveyard) — prefer AMPM_MAIN path for ISSW |
| Misc older overviews | | [Read_me_figures/avaprob_overview.png](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/Read_me_figures/avaprob_overview.png) |

### C. Other saved plot dumps

| Location | Notes |
|----------|-------|
| [`figure_notebooks/output_plots/{Whistler_Rendezvous,Fidelity,Bow_Summit,MWHS}/`](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/output_plots) | Large mixed dump (**347** files total under `output_plots`); many numbered overviews — use curated ISSW assets for supervisor walk-through |
| [`plots_for_ISSW26/pngs/`](file:///Users/machtl/Documents/Projects_PhD/plots_for_ISSW26/pngs) | SK38/Punstable evo stacks |

## Still needed (Paper 2)

| Priority | Figure | Purpose | Suggested create-in |
|----------|--------|---------|---------------------|
| **P2-1** | **Persistent slab** curated package (all 4 ops) mirroring storm/wind | Fill §4.1–4.2 gap | Re-run [Avapro_AMPM_Persistent_infoex_stats.ipynb](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Whistler/Avapro_AMPM_Persistent_infoex_stats.ipynb) with `SAVE_FIGURES=True`; generalize beyond Whistler or copy pattern per op |
| **P2-2** | Single **metrics summary** figure/table (POD/FAR/CSI/bias) × problem × climate | §4.2 paper figure | New cell at end of infoex_stats notebooks or small `metrics_summary.ipynb` |
| **P2-3** | Onset/termination Δt histograms + spell overlap | §4.3 | Extend AMPM stats notebooks (PDF already specifies matched periods) |
| **P2-4** | Timing-tolerant scores — **±1 finalized** | §4.3 | Same; captions state ±1 day / ±1 AM–PM period explicitly |
| **P2-5** | NWP vs station: publish **all aspects** heatmaps + 1–2 disagreement case profiles | §4.4 | [Avapro_NWP_vs_Station_compare.ipynb](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_NWP_vs_Station_compare.ipynb) (`SAVE_FIGURES=True`; currently strong on N aspect samples) |
| **P2-6** | Four-climate **AM/PM combined** plate from MAIN | §4.1 hero figure | [Avapro_AMPM_MAIN.ipynb](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_AMPM_MAIN.ipynb) — also save **NWP** under `AMPM_MAIN/` |
| **P2-7** | Wet: expand beyond overviews to confusion/ROC like storm | Parity across problems | Wet infoex_stats + promote into `results_wet_problems/` |
| **P2-8** | Deep persistent (DAP) verification panel if sample allows | Completeness | May be sparse — discuss with supervisor |
| **P2-9** | Updated decision-tree plate (v1 hourly / AM-PM) | Methods clarity | Already have SVGs; confirm they match paper Methods text |

---

# Cross-cutting figure list — meeting priority

Work top-down in the meeting; mark keep / remake / drop.

| # | Paper | Figure | Status | Decision / note |
|---|-------|--------|--------|-----------------|
| 1 | Both | Dashboard Dec 2025 (hex + grid + stations) | **Exists** (interactive) | Share via **localhost `:8003`**; optional screenshot plate |
| 2 | P1 | SK38/Punstable CDFs + station percentile | **Notebook + figures** | [`grid_vs_hex_stability_cdf.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb) — Banff included |
| 3 | P1 | AvAPro prevalence grid vs hex | **Notebook + figures** | [`grid_vs_hex_avapro_prevalence.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb) — grid flags merged all 4 ops; figures refreshed |
| 4 | P1 | Compute-reduction graphic | Counts known in spatial-config tables; plot missing | Full-season vs Dec-window denominator |
| 5 | P2 | Storm / wind curated results | **Strong** | Which ops/aspects make the paper vs supplement |
| 6 | P2 | Persistent curated results | **Weak / incomplete in assets** | Priority rebuild |
| 7 | P2 | Metrics + timing synthesis | Notebooks capable; paper figure missing | **±1** timing tolerance finalized |
| 8 | P2 | NWP vs station heatmaps | **Partial** | Enough for §4.4 or need full aspect matrix |
| 9 | P1 Methods | DEM / hex / single-point PNGs | **Strong** | Trim to ≤6 Methods figures; **no terrain-informed** |
| 10 | P2 Methods | Decision-tree SVGs | **Exists** | One composite vs 3 panels |

---

# Open questions / data gaps

1. **Banff QMAH + AvAPro retry — RESOLVED** — Status: [`qmah_avapro_retry_status.json`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/qmah_avapro_retry_status.json) (original QMAH/AvAPro retry PIDs **not alive**). Banff Dec GeoJSON on [`jul26_www/banff`](file:///Users/machtl/awsome/jul26_www/banff) has snp again; §4.2 notebooks/figures **re-run**. Grid AvAPro→GeoJSON merge via [`merge_avapro_into_grid_geojson.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/merge_avapro_into_grid_geojson.py) **complete for all 4 ops**; §4.3 prevalence figures refreshed. Also: [`qmah_retry_pid_logpath.txt`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/qmah_retry_pid_logpath.txt), [`rerun_banff_vstations.txt`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/rerun_banff_vstations.txt).

2. **Full-grid AvAPro comparison notebook — RESOLVED (created)** — [`notebooks/grid_vs_hex_avapro_prevalence.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb) · [abs](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_avapro_prevalence.ipynb). Runner: [`run_grid_avapro_F4.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/run_grid_avapro_F4.py). Mergers: hex [`merge_avapro_into_hex_geojson.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/merge_avapro_into_hex_geojson.py) · grid [`merge_avapro_into_grid_geojson.py`](file:///Users/machtl/Documents/docker_fun/avapro_jul26_stations/merge_avapro_into_grid_geojson.py) (**all 4 ops merged**; prevalence notebook re-run).

3. **Paper 1 Results figures from AWSOME — RESOLVED (notebooks + figures)** — [`notebooks/grid_vs_hex_stability_cdf.ipynb`](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb) · [abs](file:///Users/machtl/Documents/docker_fun/docs/notebooks/grid_vs_hex_stability_cdf.ipynb) builds ECDFs / percentiles / unstable-tail from Dec 2025 GeoJSON; outputs in [`docs/figures/`](file:///Users/machtl/Documents/docker_fun/docs/figures).

4. **Single-point config — RESOLVED** — Config III = **downscaled data for 1 location** (already have notebooks, SMETs, station layers, G20 map). See §E links above. Do **not** invent terrain-informed.

5. **Terrain-informed / PRA — RESOLVED (out of scope)** — We don’t do terrain-informed; removed from needed figures (former P1-10 / G21 outlook only).

6. **Local dashboard port — RESOLVED** — Demo/sharing via **localhost `:8003`** (user will show localhost). Pages URL remains a useful backup.

7. **Paper 2 Persistent & Deep Persistent** — Storm/Wind well curated; Persistent less so in Documentation_ISSW assets; DAP may lack InfoEx density. *(still open)*

8. **Timing-tolerant windows — RESOLVED** — Use **±1** (day / AM–PM period as implemented in verification notebooks). Document ±1 clearly in figure captions; ±3/±7 not required for the main claim.

9. **PDF filename** — `Grid_Configuarations.pdf` typo; keep path as-is when sharing. *(note only)*

10. **Compute / volumes — RESOLVED for meeting scope** — Analysis is **single-machine / this machine only**; no multi-node compute comparison needed. External volumes under `/Volumes/Machtl_1.1/...` may still be unmounted on other machines — notebooks that need band-median SMETs will fail until remount.

---

## Quick path cheat-sheet

```
PDFs:            /Users/machtl/Downloads/Grid_Configuarations.pdf
                 /Users/machtl/Downloads/AvaPro_Stations.pdf
P2 repo:         /Users/machtl/Documents/Projects_PhD/avapro_jul26
P1 method figs:  /Users/machtl/Documents/Projects_PhD/Documentation_ISSW/docs/assets/images/
P1 method doc:   /Users/machtl/Documents/Projects_PhD/Documentation_ISSW/docs/spatial-config.md
P1 analysis nbs: /Users/machtl/Documents/docker_fun/docs/notebooks/
P1 figure outs:  /Users/machtl/Documents/docker_fun/docs/figures/
P2 curated figs: .../Documentation_ISSW/docs/assets/images/results_*  and avapro_*
DEM notebooks:   /Users/machtl/Documents/Projects_Data/DEM/*.ipynb
Ops / dashboard: /Users/machtl/Documents/docker_fun/
Live www:        /Users/machtl/awsome/jul26_www/
External data:   /Users/machtl/awsome_external/
Retry status:    /Users/machtl/Documents/docker_fun/avapro_jul26_stations/qmah_avapro_retry_status.json
Demo URL:        http://localhost:8003/
Pages backup:    https://MachtlP.github.io/awsome_bc/
```

*Updated after supervisor Q&A mapping + resume pass (2026-08-19): §4.2–4.3 notebooks/figures refreshed; grid AvAPro→GeoJSON merge complete for all 4 ops. Open Qs 1,2,3,4,5,6,8,10 marked resolved.*
