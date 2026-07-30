# Avapro Point Location

This project evaluates the use of physics-based snowpack simulations to automatically identify avalanche problems and support operational avalanche forecasting. Using the AvaPro algorithm with SNOWPACK simulations, the study compares algorithm-derived avalanche problems with expert hazard assessments and observed avalanche activity across four representative snow climates in western Canada under both weather-station-driven and fully numerical weather prediction forcing. The goal of this documentation is to summarize the project's development, methodology, preliminary findings, and ongoing progress throughout the research.

<div class="note-box" markdown="1">
<p class="note-box__title">Overleaf Paper Draft</p>
<div class="note-box__body">
<a href="https://www.overleaf.com/1521811837ybdtgdbhbyth#cb180e" target="_blank" rel="noopener">https://www.overleaf.com/1521811837ybdtgdbhbyth#cb180e</a>
</div>
</div>

## 1. Data

<p class="section-updated">Last updated: 15 Jul 2026</p>
### 1.1 Study Areas

<p class="section-updated">Last updated: 15 Jul 2026</p>
Study areas span four representative snow climates in western Canada:

- Whistler Blackcomb & Whistler Heliskiing
- Rogers Pass / Glacier National Park
- Banff National Park
- Mike Wiegele Heliskiing

Notebook link: [`/Users/machtl/Documents/Projects_PhD/maps_proposal/location_map.ipynb`](file:///Users/machtl/Documents/Projects_PhD/maps_proposal/location_map.ipynb)

<iframe class="map-frame" src="../assets/maps/overview_clipped.html" title="Study areas overview map" loading="lazy"></iframe>

<p class="fig-caption"><strong>Figure 1.</strong> Interactive overview map of the four study areas (Whistler Blackcomb & Whistler Heliskiing, Rogers Pass / Glacier National Park, Banff National Park, Mike Wiegele Heliskiing).</p>

#### 1.1.1 Meteo Data

<p class="section-updated">Last updated: 16 Jul 2026</p>

See the [HRDPS](../hrdps/) page for data handling and crushing (download, GRIB processing, and SMET conversion).

<p class="table-caption"><strong>Table 1.</strong> Meteo data sources and local paths used for AvaPro point-location runs.</p>

| Data | Path | Script / Documentation |
|------|------|------------------------|
| RAW HRDPS DATA | [`/Users/machtl/Documents/Projects_Data/FirAliance download/smet_output`](file:///Users/machtl/Documents/Projects_Data/FirAliance%20download/smet_output) | [HRDPS](../hrdps/) |
| HRDPS Downscaled Data | Path | [Local HRDPS to Single Location Elevation Corrected](../hrdps/#5-local-hrdps-to-single-location-elevation-corrected) |
| RAW Station data | `folderpath` | |
| Weather stations raw | Path | |
| Weatherstation patched | Path | |

### 1.2 Snowpack Simulations

<p class="section-updated">Last updated: 23 Jul 2026</p>

<div class="note-box">
<p class="note-box__title">Project Simulations Folder</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26">/Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26</a>
</div>
</div>

Snowpack is simulated at point locations with a physics-based model forced by:

1. **AWS** — observed station meteorology (temperature, humidity, wind, precipitation / snow height)
2. **HRDPS** — downscaled numerical weather prediction fields for the same points

Simulations produce the layered snowpack state (grain type, hardness, density, weak layers) that Avapro uses to flag avalanche problems over the season.

#### SNP Runs for ISSW26

SNOWPACK research runs for ISSW26. The **SNOWPACK binary stays** in the install tree (`snowpack_vGitMaster`); this repo holds configs, forcing (SMET), initial profiles (`.sno`), and outputs.

Default binary path used by the runners:

[`/Users/machtl/Documents/snowpack_vGitMaster/snowpack/bin/snowpack`](file:///Users/machtl/Documents/snowpack_vGitMaster/snowpack/bin/snowpack)

Override with `SNOWPACK_BIN=/path/to/snowpack` if needed.

##### Repo Structure

```text
SNP_runs_for_ISSW26/
├── config/
│   ├── snp_template_debug.ini          # shared defaults (IMPORT_BEFORE)
│   ├── snp_Rendezvous25_nwp.ini        # legacy 2025 site ini
│   ├── snp_Rendezvous26_nwp.ini        # legacy 2026 site ini
│   └── 2026/
│       ├── NWP_stations/               # one ini per station (main workflow)
│       │   ├── Whistler_Rendezvous_HRDPS_2026.ini
│       │   ├── Banff_Bowsumit_HRDPS_2026.ini
│       │   ├── MWHS_MtStAnn_HRDPS_2026.ini
│       │   └── Rogers_Fidelity_HRDPS_2026.ini
│       └── NWP_singleop/               # reserved for single-op setups
├── smet/
│   ├── 2025/                           # legacy forcing
│   └── 2026/
│       ├── NWP_stations/               # HRDPS station SMETs (*_1.smet)
│       └── NWP_singleop/               # regional ALP/BTL/TL SMETs
├── sno/
│   ├── 2025/
│   └── 2026/
│       ├── NWP_stations/               # flat + virtual slopes (*_1 … *_18)
│       └── NWP_singleop/
├── out/
│   └── 2026/
│       └── NWP_stations/               # .pro / .smet outputs
├── run_snowpack.sh                     # single-run wrapper (auto -e)
└── run_snowpack_all_stations_year.sh   # batch by year (all or one op)
```

**Layout idea:** `YEAR / EXPERIMENT / …` so paths stay parallel across `config`, `smet`, `sno`, and `out`.

##### How to Run

###### Single Operation

```bash
cd /Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26

# recommended: year + station batch helper
./run_snowpack_all_stations_year.sh 2026 Whistler_Rendezvous_HRDPS_2026

# or call the low-level runner with an ini path
./run_snowpack.sh config/2026/NWP_stations/Whistler_Rendezvous_HRDPS_2026.ini

# optional: override end date (default = last SMET timestamp)
./run_snowpack.sh config/2026/NWP_stations/Whistler_Rendezvous_HRDPS_2026.ini 2026-01-01T00:00:00
```

Short names work if unique, e.g. `./run_snowpack_all_stations_year.sh 2026 Fidelity`.

###### All Operations for a Year

```bash
./run_snowpack_all_stations_year.sh 2026 all
```

- Finds all `config/2026/**/*.ini` (excluding `*template*`)
- Runs up to **4 in parallel** (`NCORES=4` by default)
- Each job uses auto `-e` from the station SMET last row

```bash
NCORES=2 ./run_snowpack_all_stations_year.sh 2026 all
```

##### Required Input Files (Per Station)

Example station stem: `Whistler_Rendezvous_HRDPS_2026`  
Forcing / snow file stem: `Whistler_Rendezvous_HRDPS_2026_1`

<p class="table-caption"><strong>Table 1b.</strong> Required input files per station for SNP runs (ISSW26).</p>

| Role | Path / file | Notes |
|------|-------------|-------|
| Site ini | `config/2026/NWP_stations/<STEM>.ini` | Paths, `METEOFILE1`, `SNOWFILE1`, `NUMBER_SLOPES`, `EXPERIMENT` |
| Shared template | `config/snp_template_debug.ini` | Pulled via `IMPORT_BEFORE = ../../snp_template_debug.ini` |
| Forcing SMET | `smet/2026/NWP_stations/<STEM>_1.smet` | Hourly meteo; must include units |
| Flat `.sno` | `sno/2026/NWP_stations/<STEM>_1.sno` | Empty start profile; `ProfileDate` |
| Slope `.sno` | `sno/2026/NWP_stations/<STEM>_11` … `_18.sno` | Needed if `NUMBER_SLOPES = 9` |
| Output dir | `out/2026/NWP_stations/` | Created/used by ini `[Output] METEOPATH` |
| Binary | `…/snowpack/bin/snowpack` | Not in this repo |

##### Quick Checklist Before a Run

- [ ] Ini paths point to this repo (`smet` / `sno` / `out`)
- [ ] SMET has `units_offset` / `units_multiplier`
- [ ] Matching `.sno` set for `NUMBER_SLOPES`
- [ ] `METEOFILE1` + `SNOWFILE1` match file stems
- [ ] `EXPERIMENT` set if you want labeled outputs
- [ ] Binary path correct (`SNOWPACK_BIN` if not default)

#### 1.2.1 .pro Simulations for NWP Run

<p class="section-updated">Last updated: 23 Jul 2026</p>

NWP-station SNOWPACK outputs (`.pro` / `.smet`) live here:

<div class="note-box">
<p class="note-box__title">NWP Station Outputs</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26/out/2026/NWP_stations">/Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26/out/2026/NWP_stations</a>
</div>
</div>

`.pro` evolution explorer notebook:

<div class="note-box">
<p class="note-box__title">.pro Evolution Explorer</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/plots_for_ISSW26/initial_snowpack_investigation.ipynb">/Users/machtl/Documents/Projects_PhD/plots_for_ISSW26/initial_snowpack_investigation.ipynb</a>
</div>
</div>

**Banff Bow Summit** (`Banff_Bowsumit_HRDPS_2026`): flat + eight virtual slopes. Miniatures below; click any panel to maximize (grain type, Sk38, P_unstable).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/00_flat.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — flat (0° / azi 0° N)">
      <img src="../assets/images/nwp_pro_bow_summit/00_flat.png" alt="Bow Summit flat snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">Flat · 0° / azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/01.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 0° N">
      <img src="../assets/images/nwp_pro_bow_summit/01.png" alt="Bow Summit 38° aspect 0° N snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/02.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 45° NE">
      <img src="../assets/images/nwp_pro_bow_summit/02.png" alt="Bow Summit 38° aspect 45° NE snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 45° NE</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/03.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 90° E">
      <img src="../assets/images/nwp_pro_bow_summit/03.png" alt="Bow Summit 38° aspect 90° E snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/04.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_bow_summit/04.png" alt="Bow Summit 38° aspect 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/05.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 180° S">
      <img src="../assets/images/nwp_pro_bow_summit/05.png" alt="Bow Summit 38° aspect 180° S snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/06.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 225° SW">
      <img src="../assets/images/nwp_pro_bow_summit/06.png" alt="Bow Summit 38° aspect 225° SW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 225° SW</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/07.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_bow_summit/07.png" alt="Bow Summit 38° aspect 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_bow_summit/08.png" class="glightbox image-zoom" data-gallery="bow-summit-pro" data-type="image" data-title="Bow Summit — 38° / azi 315° NW">
      <img src="../assets/images/nwp_pro_bow_summit/08.png" alt="Bow Summit 38° aspect 315° NW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 315° NW</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 2.</strong> Banff Bow Summit NWP run — flat + eight virtual-slope <code>.pro</code> stacks (grain type, Sk38, <em>P</em><sub>unstable</sub>). Click a miniature to maximize.</p>

**Rogers Pass Fidelity** (`Rogers_Fidelity_HRDPS_2026`): flat + eight virtual slopes. Miniatures below; click any panel to maximize (grain type, Sk38, P_unstable).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/00_flat.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — flat (0° / azi 0° N)">
      <img src="../assets/images/nwp_pro_fidelity/00_flat.png" alt="Fidelity Flat · 0° / azi 0° N snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">Flat · 0° / azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/01.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 0° N">
      <img src="../assets/images/nwp_pro_fidelity/01.png" alt="Fidelity 38° · azi 0° N snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/02.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 45° NE">
      <img src="../assets/images/nwp_pro_fidelity/02.png" alt="Fidelity 38° · azi 45° NE snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 45° NE</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/03.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 90° E">
      <img src="../assets/images/nwp_pro_fidelity/03.png" alt="Fidelity 38° · azi 90° E snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/04.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_fidelity/04.png" alt="Fidelity 38° · azi 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/05.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 180° S">
      <img src="../assets/images/nwp_pro_fidelity/05.png" alt="Fidelity 38° · azi 180° S snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/06.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 225° SW">
      <img src="../assets/images/nwp_pro_fidelity/06.png" alt="Fidelity 38° · azi 225° SW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 225° SW</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/07.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_fidelity/07.png" alt="Fidelity 38° · azi 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_fidelity/08.png" class="glightbox image-zoom" data-gallery="fidelity-pro" data-type="image" data-title="Fidelity — 38° / azi 315° NW">
      <img src="../assets/images/nwp_pro_fidelity/08.png" alt="Fidelity 38° · azi 315° NW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 315° NW</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 3.</strong> Rogers Pass Fidelity NWP run — flat + eight virtual-slope <code>.pro</code> stacks (grain type, Sk38, <em>P</em><sub>unstable</sub>). Click a miniature to maximize.</p>

**Mike Wiegele (Mt St Ann)** (`MWHS_MtStAnn_HRDPS_2026`): flat + eight virtual slopes. Miniatures below; click any panel to maximize (grain type, Sk38, P_unstable).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/00_flat.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — flat (0° / azi 0° N)">
      <img src="../assets/images/nwp_pro_mwhs/00_flat.png" alt="MWHS Mt St Ann Flat · 0° / azi 0° N snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">Flat · 0° / azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/01.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 0° N">
      <img src="../assets/images/nwp_pro_mwhs/01.png" alt="MWHS Mt St Ann 38° · azi 0° N snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/02.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 45° NE">
      <img src="../assets/images/nwp_pro_mwhs/02.png" alt="MWHS Mt St Ann 38° · azi 45° NE snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 45° NE</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/03.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 90° E">
      <img src="../assets/images/nwp_pro_mwhs/03.png" alt="MWHS Mt St Ann 38° · azi 90° E snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/04.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_mwhs/04.png" alt="MWHS Mt St Ann 38° · azi 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/05.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 180° S">
      <img src="../assets/images/nwp_pro_mwhs/05.png" alt="MWHS Mt St Ann 38° · azi 180° S snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/06.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 225° SW">
      <img src="../assets/images/nwp_pro_mwhs/06.png" alt="MWHS Mt St Ann 38° · azi 225° SW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 225° SW</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/07.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_mwhs/07.png" alt="MWHS Mt St Ann 38° · azi 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_mwhs/08.png" class="glightbox image-zoom" data-gallery="mwhs-pro" data-type="image" data-title="MWHS Mt St Ann — 38° / azi 315° NW">
      <img src="../assets/images/nwp_pro_mwhs/08.png" alt="MWHS Mt St Ann 38° · azi 315° NW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 315° NW</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 4.</strong> Mike Wiegele Mt St Ann NWP run — flat + eight virtual-slope <code>.pro</code> stacks (grain type, Sk38, <em>P</em><sub>unstable</sub>). Click a miniature to maximize.</p>

**Whistler Rendezvous** (`Whistler_Rendezvous_HRDPS_2026`): flat + eight virtual slopes. Miniatures below; click any panel to maximize (grain type, Sk38, P_unstable).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/00_flat.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — flat (0° / azi 0° N)">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/00_flat.png" alt="Whistler Rendezvous Flat · 0° / azi 0° N snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">Flat · 0° / azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/01.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 0° N">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/01.png" alt="Whistler Rendezvous 38° · azi 0° N snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/02.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 45° NE">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/02.png" alt="Whistler Rendezvous 38° · azi 45° NE snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 45° NE</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/03.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 90° E">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/03.png" alt="Whistler Rendezvous 38° · azi 90° E snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/04.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/04.png" alt="Whistler Rendezvous 38° · azi 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/05.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 180° S">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/05.png" alt="Whistler Rendezvous 38° · azi 180° S snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/06.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 225° SW">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/06.png" alt="Whistler Rendezvous 38° · azi 225° SW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 225° SW</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/07.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 270° W">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/07.png" alt="Whistler Rendezvous 38° · azi 270° W snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 270° W</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/nwp_pro_whistler_rendezvous/08.png" class="glightbox image-zoom" data-gallery="whistler-rendezvous-pro" data-type="image" data-title="Whistler Rendezvous — 38° / azi 315° NW">
      <img src="../assets/images/nwp_pro_whistler_rendezvous/08.png" alt="Whistler Rendezvous 38° · azi 315° NW snowpack evolution stack" />
    </a>
    <span class="pro-evo-grid__label">38° · azi 315° NW</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 5.</strong> Whistler Rendezvous NWP run — flat + eight virtual-slope <code>.pro</code> stacks (grain type, Sk38, <em>P</em><sub>unstable</sub>). Click a miniature to maximize.</p>

### 1.3 Avapro v1

<p class="section-updated">Last updated: 29 Jul 2026</p>

**Avapro v1** is the current AvaPro pipeline in [`avapro_jul26`](file:///Users/machtl/Documents/Projects_PhD/avapro_jul26) (AvaPro:Jul26). It reads SNOWPACK `.pro` / `.smet` pairs for flat + virtual slopes, tracks weak layers over the season (`find_aps`), and assigns daily avalanche problems (new snow, wind slab, persistent / aging-persistent, wet) via threshold-based post-processing. Aspect selects which SNP file to load; azimuth is unused; slope angle projects heights; instability uses a fixed `alp = 38°`.

For setup, slope/aspect rules, `SNP_NAMING = insert`, and the four NWP-station inis, see **[AvaPro v1 › AvaPro_Jul26](v1.md#2-avapro_jul26)**. Redesign: **[AvaPro v2](v2.md)**.

NWP-station pickle outputs (Bow Summit, Fidelity, MWHS, Whistler Rendezvous):

<div class="note-box">
<p class="note-box__title">Avapro v1 Outputs (NWP Stations)</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/output/2026/NWP_stations">/Users/machtl/Documents/Projects_PhD/avapro_jul26/output/2026/NWP_stations</a>
</div>
</div>

#### Whistler

<p class="section-updated">Last updated: 29 Jul 2026</p>

Combined AvAPro overview for Whistler Rendezvous (flatfield snowpack evolution + avalanche problems across aspects, excluding flat).

<div class="note-box">
<p class="note-box__title">Whistler Rendezvous Combined Plot Notebook</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_Whistler_Rendezvous_NESW.ipynb">/Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_Whistler_Rendezvous_NESW.ipynb</a>
</div>
</div>

![AvAPro combined — Whistler Rendezvous flatfield snowpack and avalanche problems](../assets/images/avapro_whistler/combined.png)

<p class="fig-caption"><strong>Figure 6.</strong> Whistler Rendezvous — flatfield snowpack evolution (SARP) and combined-aspect AvAPro avalanche problems (model rows; forecaster rows empty).</p>

**Whistler Rendezvous** (`Whistler_Rendezvous_HRDPS_2026`): AvAPro overview for N / E / S / W. Miniatures below; click any panel to maximize (SARP snowpack + problem lanes).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/overview_N.png" class="glightbox image-zoom" data-gallery="whistler-overview" data-type="image" data-title="AvAPro overview · Whistler Rendezvous · N">
      <img src="../assets/images/avapro_whistler/overview_N.png" alt="AvAPro overview Whistler Rendezvous N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/overview_E.png" class="glightbox image-zoom" data-gallery="whistler-overview" data-type="image" data-title="AvAPro overview · Whistler Rendezvous · E">
      <img src="../assets/images/avapro_whistler/overview_E.png" alt="AvAPro overview Whistler Rendezvous E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/overview_S.png" class="glightbox image-zoom" data-gallery="whistler-overview" data-type="image" data-title="AvAPro overview · Whistler Rendezvous · S">
      <img src="../assets/images/avapro_whistler/overview_S.png" alt="AvAPro overview Whistler Rendezvous S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/overview_W.png" class="glightbox image-zoom" data-gallery="whistler-overview" data-type="image" data-title="AvAPro overview · Whistler Rendezvous · W">
      <img src="../assets/images/avapro_whistler/overview_W.png" alt="AvAPro overview Whistler Rendezvous W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 7.</strong> Whistler Rendezvous AvAPro overview — N / E / S / W. Click a miniature to maximize.</p>

##### New Snow

**Whistler Rendezvous** (`Whistler_Rendezvous_HRDPS_2026`): new-snow detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, HS & HN, slab props, stability criteria).

![New snow overview — Whistler Rendezvous flat/N/E/S/W](../assets/images/avapro_whistler/newsnow_overview.png)

<p class="fig-caption"><strong>Figure 8.</strong> New snow · Whistler Rendezvous · flat / N / E / S / W — overview of model events and WL / coherent slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/newsnow_N.png" class="glightbox image-zoom" data-gallery="whistler-newsnow" data-type="image" data-title="New snow detail · Whistler Rendezvous · N">
      <img src="../assets/images/avapro_whistler/newsnow_N.png" alt="New snow detail Whistler Rendezvous N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/newsnow_E.png" class="glightbox image-zoom" data-gallery="whistler-newsnow" data-type="image" data-title="New snow detail · Whistler Rendezvous · E">
      <img src="../assets/images/avapro_whistler/newsnow_E.png" alt="New snow detail Whistler Rendezvous E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/newsnow_S.png" class="glightbox image-zoom" data-gallery="whistler-newsnow" data-type="image" data-title="New snow detail · Whistler Rendezvous · S">
      <img src="../assets/images/avapro_whistler/newsnow_S.png" alt="New snow detail Whistler Rendezvous S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/newsnow_W.png" class="glightbox image-zoom" data-gallery="whistler-newsnow" data-type="image" data-title="New snow detail · Whistler Rendezvous · W">
      <img src="../assets/images/avapro_whistler/newsnow_W.png" alt="New snow detail Whistler Rendezvous W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 9.</strong> Whistler Rendezvous new-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wind

**Whistler Rendezvous** (`Whistler_Rendezvous_HRDPS_2026`): wind / WSAP detail for N / E / S / W. Miniatures below; click any panel to maximize (winex, count/drft, wind speed, HN24/48).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wind_N.png" class="glightbox image-zoom" data-gallery="whistler-wind" data-type="image" data-title="Wind / WSAP detail · Whistler Rendezvous · N">
      <img src="../assets/images/avapro_whistler/wind_N.png" alt="Wind WSAP detail Whistler Rendezvous N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wind_E.png" class="glightbox image-zoom" data-gallery="whistler-wind" data-type="image" data-title="Wind / WSAP detail · Whistler Rendezvous · E">
      <img src="../assets/images/avapro_whistler/wind_E.png" alt="Wind WSAP detail Whistler Rendezvous E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wind_S.png" class="glightbox image-zoom" data-gallery="whistler-wind" data-type="image" data-title="Wind / WSAP detail · Whistler Rendezvous · S">
      <img src="../assets/images/avapro_whistler/wind_S.png" alt="Wind WSAP detail Whistler Rendezvous S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wind_W.png" class="glightbox image-zoom" data-gallery="whistler-wind" data-type="image" data-title="Wind / WSAP detail · Whistler Rendezvous · W">
      <img src="../assets/images/avapro_whistler/wind_W.png" alt="Wind WSAP detail Whistler Rendezvous W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 10.</strong> Whistler Rendezvous wind / WSAP detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wet

**Whistler Rendezvous** (`Whistler_Rendezvous_HRDPS_2026`): wet-snow / LWC detail for flat + N–NW, plus N / E / S / W panels. Miniatures below; click any panel to maximize (model vs forecaster events, LWC).

![Wet snow overview — Whistler Rendezvous flat + N–NW](../assets/images/avapro_whistler/wet_overview.png)

<p class="fig-caption"><strong>Figure 11.</strong> Wet snow · Whistler Rendezvous · flat + N–NW — LWC and model wet-snow events by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wet_N.png" class="glightbox image-zoom" data-gallery="whistler-wet" data-type="image" data-title="Wet snow detail · Whistler Rendezvous · N">
      <img src="../assets/images/avapro_whistler/wet_N.png" alt="Wet snow detail Whistler Rendezvous N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wet_E.png" class="glightbox image-zoom" data-gallery="whistler-wet" data-type="image" data-title="Wet snow detail · Whistler Rendezvous · E">
      <img src="../assets/images/avapro_whistler/wet_E.png" alt="Wet snow detail Whistler Rendezvous E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wet_S.png" class="glightbox image-zoom" data-gallery="whistler-wet" data-type="image" data-title="Wet snow detail · Whistler Rendezvous · S">
      <img src="../assets/images/avapro_whistler/wet_S.png" alt="Wet snow detail Whistler Rendezvous S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/wet_W.png" class="glightbox image-zoom" data-gallery="whistler-wet" data-type="image" data-title="Wet snow detail · Whistler Rendezvous · W">
      <img src="../assets/images/avapro_whistler/wet_W.png" alt="Wet snow detail Whistler Rendezvous W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 12.</strong> Whistler Rendezvous wet-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Persistent

**Whistler Rendezvous** (`Whistler_Rendezvous_HRDPS_2026`): PAP detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, slab props, stability criteria).

![PAP overview — Whistler Rendezvous flat + N–NW](../assets/images/avapro_whistler/pap_overview.png)

<p class="fig-caption"><strong>Figure 13.</strong> PAP · Whistler Rendezvous · flat + N–NW — overview of model events and WL / healthy slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/pap_N.png" class="glightbox image-zoom" data-gallery="whistler-pap" data-type="image" data-title="PAP detail · Whistler Rendezvous · N">
      <img src="../assets/images/avapro_whistler/pap_N.png" alt="PAP detail Whistler Rendezvous N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/pap_E.png" class="glightbox image-zoom" data-gallery="whistler-pap" data-type="image" data-title="PAP detail · Whistler Rendezvous · E">
      <img src="../assets/images/avapro_whistler/pap_E.png" alt="PAP detail Whistler Rendezvous E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/pap_S.png" class="glightbox image-zoom" data-gallery="whistler-pap" data-type="image" data-title="PAP detail · Whistler Rendezvous · S">
      <img src="../assets/images/avapro_whistler/pap_S.png" alt="PAP detail Whistler Rendezvous S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_whistler/pap_W.png" class="glightbox image-zoom" data-gallery="whistler-pap" data-type="image" data-title="PAP detail · Whistler Rendezvous · W">
      <img src="../assets/images/avapro_whistler/pap_W.png" alt="PAP detail Whistler Rendezvous W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 14.</strong> Whistler Rendezvous PAP detail — N / E / S / W. Click a miniature to maximize.</p>

#### Bow Summit

<p class="section-updated">Last updated: 29 Jul 2026</p>

AvAPro overview for Banff Bow Summit (per-aspect snowpack evolution + avalanche problems for N / E / S / W).

<div class="note-box">
<p class="note-box__title">Bow Summit Combined Plot Notebook</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_Bow_Summit_NESW.ipynb">/Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_Bow_Summit_NESW.ipynb</a>
</div>
</div>

**Banff Bow Summit** (`Banff_Bowsumit_HRDPS_2026`): AvAPro overview for N / E / S / W. Miniatures below; click any panel to maximize (SARP snowpack + problem lanes).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/overview_N.png" class="glightbox image-zoom" data-gallery="bow-summit-overview" data-type="image" data-title="AvAPro overview · Banff Bow Summit · N">
      <img src="../assets/images/avapro_bow_summit/overview_N.png" alt="AvAPro overview Banff Bow Summit N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/overview_E.png" class="glightbox image-zoom" data-gallery="bow-summit-overview" data-type="image" data-title="AvAPro overview · Banff Bow Summit · E">
      <img src="../assets/images/avapro_bow_summit/overview_E.png" alt="AvAPro overview Banff Bow Summit E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/overview_S.png" class="glightbox image-zoom" data-gallery="bow-summit-overview" data-type="image" data-title="AvAPro overview · Banff Bow Summit · S">
      <img src="../assets/images/avapro_bow_summit/overview_S.png" alt="AvAPro overview Banff Bow Summit S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/overview_W.png" class="glightbox image-zoom" data-gallery="bow-summit-overview" data-type="image" data-title="AvAPro overview · Banff Bow Summit · W">
      <img src="../assets/images/avapro_bow_summit/overview_W.png" alt="AvAPro overview Banff Bow Summit W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 15.</strong> Banff Bow Summit AvAPro overview — N / E / S / W. Click a miniature to maximize.</p>

##### New Snow

**Banff Bow Summit** (`Banff_Bowsumit_HRDPS_2026`): new-snow detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, HS & HN, slab props, stability criteria).

![New snow overview — Banff Bow Summit flat/N/E/S/W](../assets/images/avapro_bow_summit/newsnow_overview.png)

<p class="fig-caption"><strong>Figure 16.</strong> New snow · Banff Bow Summit · flat / N / E / S / W — overview of model events and WL / coherent slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/newsnow_N.png" class="glightbox image-zoom" data-gallery="bow-summit-newsnow" data-type="image" data-title="New snow detail · Banff Bow Summit · N">
      <img src="../assets/images/avapro_bow_summit/newsnow_N.png" alt="New snow detail Banff Bow Summit N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/newsnow_E.png" class="glightbox image-zoom" data-gallery="bow-summit-newsnow" data-type="image" data-title="New snow detail · Banff Bow Summit · E">
      <img src="../assets/images/avapro_bow_summit/newsnow_E.png" alt="New snow detail Banff Bow Summit E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/newsnow_S.png" class="glightbox image-zoom" data-gallery="bow-summit-newsnow" data-type="image" data-title="New snow detail · Banff Bow Summit · S">
      <img src="../assets/images/avapro_bow_summit/newsnow_S.png" alt="New snow detail Banff Bow Summit S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/newsnow_W.png" class="glightbox image-zoom" data-gallery="bow-summit-newsnow" data-type="image" data-title="New snow detail · Banff Bow Summit · W">
      <img src="../assets/images/avapro_bow_summit/newsnow_W.png" alt="New snow detail Banff Bow Summit W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 17.</strong> Banff Bow Summit new-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wind

**Banff Bow Summit** (`Banff_Bowsumit_HRDPS_2026`): wind / WSAP detail for N / E / S / W. Miniatures below; click any panel to maximize (winex, count/drft, wind speed, HN24/48).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wind_N.png" class="glightbox image-zoom" data-gallery="bow-summit-wind" data-type="image" data-title="Wind / WSAP detail · Banff Bow Summit · N">
      <img src="../assets/images/avapro_bow_summit/wind_N.png" alt="Wind WSAP detail Banff Bow Summit N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wind_E.png" class="glightbox image-zoom" data-gallery="bow-summit-wind" data-type="image" data-title="Wind / WSAP detail · Banff Bow Summit · E">
      <img src="../assets/images/avapro_bow_summit/wind_E.png" alt="Wind WSAP detail Banff Bow Summit E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wind_S.png" class="glightbox image-zoom" data-gallery="bow-summit-wind" data-type="image" data-title="Wind / WSAP detail · Banff Bow Summit · S">
      <img src="../assets/images/avapro_bow_summit/wind_S.png" alt="Wind WSAP detail Banff Bow Summit S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wind_W.png" class="glightbox image-zoom" data-gallery="bow-summit-wind" data-type="image" data-title="Wind / WSAP detail · Banff Bow Summit · W">
      <img src="../assets/images/avapro_bow_summit/wind_W.png" alt="Wind WSAP detail Banff Bow Summit W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 18.</strong> Banff Bow Summit wind / WSAP detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wet

**Banff Bow Summit** (`Banff_Bowsumit_HRDPS_2026`): wet-snow / LWC detail for flat + N–NW, plus N / E / S / W panels. Miniatures below; click any panel to maximize (model vs forecaster events, LWC).

![Wet snow overview — Banff Bow Summit flat + N–NW](../assets/images/avapro_bow_summit/wet_overview.png)

<p class="fig-caption"><strong>Figure 19.</strong> Wet snow · Banff Bow Summit · flat + N–NW — LWC and model wet-snow events by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wet_N.png" class="glightbox image-zoom" data-gallery="bow-summit-wet" data-type="image" data-title="Wet snow detail · Banff Bow Summit · N">
      <img src="../assets/images/avapro_bow_summit/wet_N.png" alt="Wet snow detail Banff Bow Summit N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wet_E.png" class="glightbox image-zoom" data-gallery="bow-summit-wet" data-type="image" data-title="Wet snow detail · Banff Bow Summit · E">
      <img src="../assets/images/avapro_bow_summit/wet_E.png" alt="Wet snow detail Banff Bow Summit E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wet_S.png" class="glightbox image-zoom" data-gallery="bow-summit-wet" data-type="image" data-title="Wet snow detail · Banff Bow Summit · S">
      <img src="../assets/images/avapro_bow_summit/wet_S.png" alt="Wet snow detail Banff Bow Summit S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/wet_W.png" class="glightbox image-zoom" data-gallery="bow-summit-wet" data-type="image" data-title="Wet snow detail · Banff Bow Summit · W">
      <img src="../assets/images/avapro_bow_summit/wet_W.png" alt="Wet snow detail Banff Bow Summit W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 20.</strong> Banff Bow Summit wet-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Persistent

**Banff Bow Summit** (`Banff_Bowsumit_HRDPS_2026`): PAP detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, slab props, stability criteria).

![PAP overview — Banff Bow Summit flat + N–NW](../assets/images/avapro_bow_summit/pap_overview.png)

<p class="fig-caption"><strong>Figure 21.</strong> PAP · Banff Bow Summit · flat + N–NW — overview of model events and WL / healthy slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/pap_N.png" class="glightbox image-zoom" data-gallery="bow-summit-pap" data-type="image" data-title="PAP detail · Banff Bow Summit · N">
      <img src="../assets/images/avapro_bow_summit/pap_N.png" alt="PAP detail Banff Bow Summit N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/pap_E.png" class="glightbox image-zoom" data-gallery="bow-summit-pap" data-type="image" data-title="PAP detail · Banff Bow Summit · E">
      <img src="../assets/images/avapro_bow_summit/pap_E.png" alt="PAP detail Banff Bow Summit E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/pap_S.png" class="glightbox image-zoom" data-gallery="bow-summit-pap" data-type="image" data-title="PAP detail · Banff Bow Summit · S">
      <img src="../assets/images/avapro_bow_summit/pap_S.png" alt="PAP detail Banff Bow Summit S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_bow_summit/pap_W.png" class="glightbox image-zoom" data-gallery="bow-summit-pap" data-type="image" data-title="PAP detail · Banff Bow Summit · W">
      <img src="../assets/images/avapro_bow_summit/pap_W.png" alt="PAP detail Banff Bow Summit W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 22.</strong> Banff Bow Summit PAP detail — N / E / S / W. Click a miniature to maximize.</p>

#### Fidelity

<p class="section-updated">Last updated: 29 Jul 2026</p>

AvAPro overview for Rogers Pass Fidelity (per-aspect snowpack evolution + avalanche problems for N / E / S / W).

<div class="note-box">
<p class="note-box__title">Fidelity Combined Plot Notebook</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_Fidelity_NESW.ipynb">/Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_Fidelity_NESW.ipynb</a>
</div>
</div>

**Rogers Pass Fidelity** (`Rogers_Fidelity_HRDPS_2026`): AvAPro overview for N / E / S / W. Miniatures below; click any panel to maximize (SARP snowpack + problem lanes).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/overview_N.png" class="glightbox image-zoom" data-gallery="fidelity-overview" data-type="image" data-title="AvAPro overview · Rogers Pass Fidelity · N">
      <img src="../assets/images/avapro_fidelity/overview_N.png" alt="AvAPro overview Rogers Pass Fidelity N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/overview_E.png" class="glightbox image-zoom" data-gallery="fidelity-overview" data-type="image" data-title="AvAPro overview · Rogers Pass Fidelity · E">
      <img src="../assets/images/avapro_fidelity/overview_E.png" alt="AvAPro overview Rogers Pass Fidelity E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/overview_S.png" class="glightbox image-zoom" data-gallery="fidelity-overview" data-type="image" data-title="AvAPro overview · Rogers Pass Fidelity · S">
      <img src="../assets/images/avapro_fidelity/overview_S.png" alt="AvAPro overview Rogers Pass Fidelity S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/overview_W.png" class="glightbox image-zoom" data-gallery="fidelity-overview" data-type="image" data-title="AvAPro overview · Rogers Pass Fidelity · W">
      <img src="../assets/images/avapro_fidelity/overview_W.png" alt="AvAPro overview Rogers Pass Fidelity W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 23.</strong> Rogers Pass Fidelity AvAPro overview — N / E / S / W. Click a miniature to maximize.</p>

##### New Snow

**Rogers Pass Fidelity** (`Rogers_Fidelity_HRDPS_2026`): new-snow detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, HS & HN, slab props, stability criteria).

![New snow overview — Rogers Pass Fidelity flat/N/E/S/W](../assets/images/avapro_fidelity/newsnow_overview.png)

<p class="fig-caption"><strong>Figure 24.</strong> New snow · Rogers Pass Fidelity · flat / N / E / S / W — overview of model events and WL / coherent slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/newsnow_N.png" class="glightbox image-zoom" data-gallery="fidelity-newsnow" data-type="image" data-title="New snow detail · Rogers Pass Fidelity · N">
      <img src="../assets/images/avapro_fidelity/newsnow_N.png" alt="New snow detail Rogers Pass Fidelity N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/newsnow_E.png" class="glightbox image-zoom" data-gallery="fidelity-newsnow" data-type="image" data-title="New snow detail · Rogers Pass Fidelity · E">
      <img src="../assets/images/avapro_fidelity/newsnow_E.png" alt="New snow detail Rogers Pass Fidelity E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/newsnow_S.png" class="glightbox image-zoom" data-gallery="fidelity-newsnow" data-type="image" data-title="New snow detail · Rogers Pass Fidelity · S">
      <img src="../assets/images/avapro_fidelity/newsnow_S.png" alt="New snow detail Rogers Pass Fidelity S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/newsnow_W.png" class="glightbox image-zoom" data-gallery="fidelity-newsnow" data-type="image" data-title="New snow detail · Rogers Pass Fidelity · W">
      <img src="../assets/images/avapro_fidelity/newsnow_W.png" alt="New snow detail Rogers Pass Fidelity W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 25.</strong> Rogers Pass Fidelity new-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wind

**Rogers Pass Fidelity** (`Rogers_Fidelity_HRDPS_2026`): wind / WSAP detail for N / E / S / W. Miniatures below; click any panel to maximize (winex, count/drft, wind speed, HN24/48).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wind_N.png" class="glightbox image-zoom" data-gallery="fidelity-wind" data-type="image" data-title="Wind / WSAP detail · Rogers Pass Fidelity · N">
      <img src="../assets/images/avapro_fidelity/wind_N.png" alt="Wind WSAP detail Rogers Pass Fidelity N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wind_E.png" class="glightbox image-zoom" data-gallery="fidelity-wind" data-type="image" data-title="Wind / WSAP detail · Rogers Pass Fidelity · E">
      <img src="../assets/images/avapro_fidelity/wind_E.png" alt="Wind WSAP detail Rogers Pass Fidelity E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wind_S.png" class="glightbox image-zoom" data-gallery="fidelity-wind" data-type="image" data-title="Wind / WSAP detail · Rogers Pass Fidelity · S">
      <img src="../assets/images/avapro_fidelity/wind_S.png" alt="Wind WSAP detail Rogers Pass Fidelity S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wind_W.png" class="glightbox image-zoom" data-gallery="fidelity-wind" data-type="image" data-title="Wind / WSAP detail · Rogers Pass Fidelity · W">
      <img src="../assets/images/avapro_fidelity/wind_W.png" alt="Wind WSAP detail Rogers Pass Fidelity W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 26.</strong> Rogers Pass Fidelity wind / WSAP detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wet

**Rogers Pass Fidelity** (`Rogers_Fidelity_HRDPS_2026`): wet-snow / LWC detail for flat + N–NW, plus N / E / S / W panels. Miniatures below; click any panel to maximize (model vs forecaster events, LWC).

![Wet snow overview — Rogers Pass Fidelity flat + N–NW](../assets/images/avapro_fidelity/wet_overview.png)

<p class="fig-caption"><strong>Figure 27.</strong> Wet snow · Rogers Pass Fidelity · flat + N–NW — LWC and model wet-snow events by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wet_N.png" class="glightbox image-zoom" data-gallery="fidelity-wet" data-type="image" data-title="Wet snow detail · Rogers Pass Fidelity · N">
      <img src="../assets/images/avapro_fidelity/wet_N.png" alt="Wet snow detail Rogers Pass Fidelity N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wet_E.png" class="glightbox image-zoom" data-gallery="fidelity-wet" data-type="image" data-title="Wet snow detail · Rogers Pass Fidelity · E">
      <img src="../assets/images/avapro_fidelity/wet_E.png" alt="Wet snow detail Rogers Pass Fidelity E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wet_S.png" class="glightbox image-zoom" data-gallery="fidelity-wet" data-type="image" data-title="Wet snow detail · Rogers Pass Fidelity · S">
      <img src="../assets/images/avapro_fidelity/wet_S.png" alt="Wet snow detail Rogers Pass Fidelity S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/wet_W.png" class="glightbox image-zoom" data-gallery="fidelity-wet" data-type="image" data-title="Wet snow detail · Rogers Pass Fidelity · W">
      <img src="../assets/images/avapro_fidelity/wet_W.png" alt="Wet snow detail Rogers Pass Fidelity W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 28.</strong> Rogers Pass Fidelity wet-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Persistent

**Rogers Pass Fidelity** (`Rogers_Fidelity_HRDPS_2026`): PAP detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, slab props, stability criteria).

![PAP overview — Rogers Pass Fidelity flat + N–NW](../assets/images/avapro_fidelity/pap_overview.png)

<p class="fig-caption"><strong>Figure 29.</strong> PAP · Rogers Pass Fidelity · flat + N–NW — overview of model events and WL / healthy slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/pap_N.png" class="glightbox image-zoom" data-gallery="fidelity-pap" data-type="image" data-title="PAP detail · Rogers Pass Fidelity · N">
      <img src="../assets/images/avapro_fidelity/pap_N.png" alt="PAP detail Rogers Pass Fidelity N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/pap_E.png" class="glightbox image-zoom" data-gallery="fidelity-pap" data-type="image" data-title="PAP detail · Rogers Pass Fidelity · E">
      <img src="../assets/images/avapro_fidelity/pap_E.png" alt="PAP detail Rogers Pass Fidelity E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/pap_S.png" class="glightbox image-zoom" data-gallery="fidelity-pap" data-type="image" data-title="PAP detail · Rogers Pass Fidelity · S">
      <img src="../assets/images/avapro_fidelity/pap_S.png" alt="PAP detail Rogers Pass Fidelity S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_fidelity/pap_W.png" class="glightbox image-zoom" data-gallery="fidelity-pap" data-type="image" data-title="PAP detail · Rogers Pass Fidelity · W">
      <img src="../assets/images/avapro_fidelity/pap_W.png" alt="PAP detail Rogers Pass Fidelity W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 30.</strong> Rogers Pass Fidelity PAP detail — N / E / S / W. Click a miniature to maximize.</p>

#### MWHS

<p class="section-updated">Last updated: 29 Jul 2026</p>

AvAPro overview for Mike Wiegele (Mt St Ann) (per-aspect snowpack evolution + avalanche problems for N / E / S / W).

<div class="note-box">
<p class="note-box__title">MWHS Combined Plot Notebook</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_MWHS_NESW.ipynb">/Users/machtl/Documents/Projects_PhD/avapro_jul26/figure_notebooks/Avapro_pap_stack_MWHS_NESW.ipynb</a>
</div>
</div>

**Mike Wiegele (Mt St Ann)** (`MWHS_MtStAnn_HRDPS_2026`): AvAPro overview for N / E / S / W. Miniatures below; click any panel to maximize (SARP snowpack + problem lanes).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/overview_N.png" class="glightbox image-zoom" data-gallery="mwhs-overview" data-type="image" data-title="AvAPro overview · Mike Wiegele (Mt St Ann) · N">
      <img src="../assets/images/avapro_mwhs/overview_N.png" alt="AvAPro overview Mike Wiegele (Mt St Ann) N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/overview_E.png" class="glightbox image-zoom" data-gallery="mwhs-overview" data-type="image" data-title="AvAPro overview · Mike Wiegele (Mt St Ann) · E">
      <img src="../assets/images/avapro_mwhs/overview_E.png" alt="AvAPro overview Mike Wiegele (Mt St Ann) E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/overview_S.png" class="glightbox image-zoom" data-gallery="mwhs-overview" data-type="image" data-title="AvAPro overview · Mike Wiegele (Mt St Ann) · S">
      <img src="../assets/images/avapro_mwhs/overview_S.png" alt="AvAPro overview Mike Wiegele (Mt St Ann) S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/overview_W.png" class="glightbox image-zoom" data-gallery="mwhs-overview" data-type="image" data-title="AvAPro overview · Mike Wiegele (Mt St Ann) · W">
      <img src="../assets/images/avapro_mwhs/overview_W.png" alt="AvAPro overview Mike Wiegele (Mt St Ann) W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 31.</strong> Mike Wiegele (Mt St Ann) AvAPro overview — N / E / S / W. Click a miniature to maximize.</p>

##### New Snow

**Mike Wiegele (Mt St Ann)** (`MWHS_MtStAnn_HRDPS_2026`): new-snow detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, HS & HN, slab props, stability criteria).

![New snow overview — Mike Wiegele (Mt St Ann) flat/N/E/S/W](../assets/images/avapro_mwhs/newsnow_overview.png)

<p class="fig-caption"><strong>Figure 32.</strong> New snow · Mike Wiegele (Mt St Ann) · flat / N / E / S / W — overview of model events and WL / coherent slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/newsnow_N.png" class="glightbox image-zoom" data-gallery="mwhs-newsnow" data-type="image" data-title="New snow detail · Mike Wiegele (Mt St Ann) · N">
      <img src="../assets/images/avapro_mwhs/newsnow_N.png" alt="New snow detail Mike Wiegele (Mt St Ann) N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/newsnow_E.png" class="glightbox image-zoom" data-gallery="mwhs-newsnow" data-type="image" data-title="New snow detail · Mike Wiegele (Mt St Ann) · E">
      <img src="../assets/images/avapro_mwhs/newsnow_E.png" alt="New snow detail Mike Wiegele (Mt St Ann) E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/newsnow_S.png" class="glightbox image-zoom" data-gallery="mwhs-newsnow" data-type="image" data-title="New snow detail · Mike Wiegele (Mt St Ann) · S">
      <img src="../assets/images/avapro_mwhs/newsnow_S.png" alt="New snow detail Mike Wiegele (Mt St Ann) S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/newsnow_W.png" class="glightbox image-zoom" data-gallery="mwhs-newsnow" data-type="image" data-title="New snow detail · Mike Wiegele (Mt St Ann) · W">
      <img src="../assets/images/avapro_mwhs/newsnow_W.png" alt="New snow detail Mike Wiegele (Mt St Ann) W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 33.</strong> Mike Wiegele (Mt St Ann) new-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wind

**Mike Wiegele (Mt St Ann)** (`MWHS_MtStAnn_HRDPS_2026`): wind / WSAP detail for N / E / S / W. Miniatures below; click any panel to maximize (winex, count/drft, wind speed, HN24/48).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wind_N.png" class="glightbox image-zoom" data-gallery="mwhs-wind" data-type="image" data-title="Wind / WSAP detail · Mike Wiegele (Mt St Ann) · N">
      <img src="../assets/images/avapro_mwhs/wind_N.png" alt="Wind WSAP detail Mike Wiegele (Mt St Ann) N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wind_E.png" class="glightbox image-zoom" data-gallery="mwhs-wind" data-type="image" data-title="Wind / WSAP detail · Mike Wiegele (Mt St Ann) · E">
      <img src="../assets/images/avapro_mwhs/wind_E.png" alt="Wind WSAP detail Mike Wiegele (Mt St Ann) E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wind_S.png" class="glightbox image-zoom" data-gallery="mwhs-wind" data-type="image" data-title="Wind / WSAP detail · Mike Wiegele (Mt St Ann) · S">
      <img src="../assets/images/avapro_mwhs/wind_S.png" alt="Wind WSAP detail Mike Wiegele (Mt St Ann) S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wind_W.png" class="glightbox image-zoom" data-gallery="mwhs-wind" data-type="image" data-title="Wind / WSAP detail · Mike Wiegele (Mt St Ann) · W">
      <img src="../assets/images/avapro_mwhs/wind_W.png" alt="Wind WSAP detail Mike Wiegele (Mt St Ann) W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 34.</strong> Mike Wiegele (Mt St Ann) wind / WSAP detail — N / E / S / W. Click a miniature to maximize.</p>

##### Wet

**Mike Wiegele (Mt St Ann)** (`MWHS_MtStAnn_HRDPS_2026`): wet-snow / LWC detail for flat + N–NW, plus N / E / S / W panels. Miniatures below; click any panel to maximize (model vs forecaster events, LWC).

![Wet snow overview — Mike Wiegele (Mt St Ann) flat + N–NW](../assets/images/avapro_mwhs/wet_overview.png)

<p class="fig-caption"><strong>Figure 35.</strong> Wet snow · Mike Wiegele (Mt St Ann) · flat + N–NW — LWC and model wet-snow events by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wet_N.png" class="glightbox image-zoom" data-gallery="mwhs-wet" data-type="image" data-title="Wet snow detail · Mike Wiegele (Mt St Ann) · N">
      <img src="../assets/images/avapro_mwhs/wet_N.png" alt="Wet snow detail Mike Wiegele (Mt St Ann) N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wet_E.png" class="glightbox image-zoom" data-gallery="mwhs-wet" data-type="image" data-title="Wet snow detail · Mike Wiegele (Mt St Ann) · E">
      <img src="../assets/images/avapro_mwhs/wet_E.png" alt="Wet snow detail Mike Wiegele (Mt St Ann) E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wet_S.png" class="glightbox image-zoom" data-gallery="mwhs-wet" data-type="image" data-title="Wet snow detail · Mike Wiegele (Mt St Ann) · S">
      <img src="../assets/images/avapro_mwhs/wet_S.png" alt="Wet snow detail Mike Wiegele (Mt St Ann) S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/wet_W.png" class="glightbox image-zoom" data-gallery="mwhs-wet" data-type="image" data-title="Wet snow detail · Mike Wiegele (Mt St Ann) · W">
      <img src="../assets/images/avapro_mwhs/wet_W.png" alt="Wet snow detail Mike Wiegele (Mt St Ann) W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 36.</strong> Mike Wiegele (Mt St Ann) wet-snow detail — N / E / S / W. Click a miniature to maximize.</p>

##### Persistent

**Mike Wiegele (Mt St Ann)** (`MWHS_MtStAnn_HRDPS_2026`): PAP detail for N / E / S / W. Miniatures below; click any panel to maximize (events, WL/slab flags, slab props, stability criteria).

![PAP overview — Mike Wiegele (Mt St Ann) flat + N–NW](../assets/images/avapro_mwhs/pap_overview.png)

<p class="fig-caption"><strong>Figure 37.</strong> PAP · Mike Wiegele (Mt St Ann) · flat + N–NW — overview of model events and WL / healthy slab / initiation / propagation by aspect.</p>

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/pap_N.png" class="glightbox image-zoom" data-gallery="mwhs-pap" data-type="image" data-title="PAP detail · Mike Wiegele (Mt St Ann) · N">
      <img src="../assets/images/avapro_mwhs/pap_N.png" alt="PAP detail Mike Wiegele (Mt St Ann) N" />
    </a>
    <span class="pro-evo-grid__label">azi 0° N</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/pap_E.png" class="glightbox image-zoom" data-gallery="mwhs-pap" data-type="image" data-title="PAP detail · Mike Wiegele (Mt St Ann) · E">
      <img src="../assets/images/avapro_mwhs/pap_E.png" alt="PAP detail Mike Wiegele (Mt St Ann) E" />
    </a>
    <span class="pro-evo-grid__label">azi 90° E</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/pap_S.png" class="glightbox image-zoom" data-gallery="mwhs-pap" data-type="image" data-title="PAP detail · Mike Wiegele (Mt St Ann) · S">
      <img src="../assets/images/avapro_mwhs/pap_S.png" alt="PAP detail Mike Wiegele (Mt St Ann) S" />
    </a>
    <span class="pro-evo-grid__label">azi 180° S</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/avapro_mwhs/pap_W.png" class="glightbox image-zoom" data-gallery="mwhs-pap" data-type="image" data-title="PAP detail · Mike Wiegele (Mt St Ann) · W">
      <img src="../assets/images/avapro_mwhs/pap_W.png" alt="PAP detail Mike Wiegele (Mt St Ann) W" />
    </a>
    <span class="pro-evo-grid__label">azi 270° W</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 38.</strong> Mike Wiegele (Mt St Ann) PAP detail — N / E / S / W. Click a miniature to maximize.</p>

### 1.4 Validation Dataset

<p class="section-updated">Last updated: 15 Jul 2026</p>
The validation set is built from operational forecast products:

- Daily (or bulletin-cycle) avalanche problem types and likelihood / size where available
- Aligned to the same calendar days and locations as the model output
- Quality flags for missing bulletins, special advisories, or incomplete problem fields

This dataset is the ground truth for daily comparison and agreement metrics.

## 2. Methods

<p class="section-updated">Last updated: 15 Jul 2026</p>
### 2.1 Avalanche Problem Identification

<p class="section-updated">Last updated: 15 Jul 2026</p>
Avapro rules are applied to each simulated profile to detect candidate avalanche problems (e.g. persistent slab, wind slab, storm slab, wet snow), using thresholds on weak-layer presence, slab properties, and meteorological drivers.

Output is a daily problem presence / type (and optionally severity) time series per site and forcing source.

### 2.2 Daily Comparison

<p class="section-updated">Last updated: 15 Jul 2026</p>
For each site and day:

1. Extract Avapro problem(s) from the AWS-forced and HRDPS-forced runs
2. Extract the operational problem(s) from the validation dataset
3. Match on problem type (and optionally treat “any problem” vs “no problem” as a binary case)

Comparisons are reported per problem type and pooled across types where useful.

### 2.3 Evaluation Metrics

<p class="section-updated">Last updated: 15 Jul 2026</p>
Core metrics:

<p class="table-caption"><strong>Table 2.</strong> Evaluation metrics used to compare AvaPro avalanche-problem output with operational forecast products.</p>

| Metric | What it measures |
|--------|------------------|
| Hit rate / recall | Fraction of operational problem days recovered by Avapro |
| False alarm ratio | Fraction of Avapro problem days without an operational counterpart |
| Precision / F1 | Balance of correctness and completeness |
| Agreement rate | Day-level match (problem present / absent, or type match) |

Confidence intervals or season-wise breakdowns can be included for robustness.

### 2.4 Operational Feedback

<p class="section-updated">Last updated: 15 Jul 2026</p>
Results are reviewed with operational partners to check:

- Whether disagreements are model errors, forecast subjectivity, or scale mismatch (point vs region)
- Which problem types are most useful operationally
- Practical thresholds and presentation for forecast desks

## 3. Results

<p class="section-updated">Last updated: 15 Jul 2026</p>
### 3.1 Agreement Statistics

<p class="section-updated">Last updated: 15 Jul 2026</p>
Overall day-level agreement between Avapro and operational problems is summarized by site, season, and problem type. Persistent and storm-related problems typically show different skill; report the strongest and weakest categories explicitly once numbers are finalized.

### 3.2 Temporal Behavior

<p class="section-updated">Last updated: 15 Jul 2026</p>
Agreement varies through the season:

- Early season: thinner packs, fewer persistent structures → often lower event counts
- Mid season: persistent weak layers dominate skill / disagreement patterns
- Spring: wet-snow problems and melt–freeze cycles change the error profile

Time-series plots of daily Avapro vs bulletin problems belong in this section.

### 3.3 AWS vs HRDPS

<p class="section-updated">Last updated: 15 Jul 2026</p>
Side-by-side comparison of the two forcings:

- **AWS** — closer to observed meteorology at the station; limited by station representativeness
- **HRDPS** — spatially complete; may bias precipitation / wind and thus slab / weak-layer timing

Report which forcing yields higher agreement overall and for which problem types the gap is largest.

## 4. Discussion

<p class="section-updated">Last updated: 15 Jul 2026</p>
Main interpretation points:

- Point Avapro can track operational problem timing for some types, but regional bulletins are not a perfect point truth
- Forcing choice (AWS vs HRDPS) is a first-order control on snowpack structure and therefore on Avapro output
- Remaining errors mix model physics, Avapro rule design, and human forecast practices

Limitations: sparse sites, bulletin-to-point scale mismatch, and incomplete problem metadata in some seasons.

## 5. Conclusion

<p class="section-updated">Last updated: 15 Jul 2026</p>
Avapro at point locations is a useful diagnostic of automated avalanche problem identification when evaluated against operational products. AWS-forced runs provide a high-quality reference where stations exist; HRDPS extends coverage at some cost in agreement. Next steps include tightening problem-type definitions, expanding sites, and linking point results to the Spatial config workstream.

## 6. Operational Mode

<p class="section-updated">Last updated: 16 Jul 2026</p>

<div class="todo-box">
<p class="todo-box__title">ToDo — Avapro Point Location › 6. Operational Mode</p>
<div class="todo-box__body">no tackel yet</div>
</div>
