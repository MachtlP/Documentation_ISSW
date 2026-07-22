# Avapro General

<p class="section-updated">Last updated: 21 Jul 2026</p>

<details class="table-dropdown">
<summary><strong>1. Old Avapro</strong> — click to expand</summary>

<p class="section-updated">Last updated: 21 Jul 2026</p>

<div class="note-box">
<p class="note-box__title">Project Folder</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Desktop/avaproblemsmatlab2python">/Users/machtl/Desktop/avaproblemsmatlab2python</a>
</div>
</div>

How to run (copy-paste):

```bash
cd Desktop/avaproblemsmatlab2python/py-code
conda activate oldavapro
python MAIN_ava_prob_seasons.py avaprob_RENDEZVOUS25.ini
```

</details>

## 2. AvaPro_Jul26

<p class="section-updated">Last updated: 21 Jul 2026</p>

<div class="note-box">
<p class="note-box__title">Project Folder</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/avapro_jul26">/Users/machtl/Documents/Projects_PhD/avapro_jul26</a>
</div>
</div>

<details class="table-dropdown">
<summary><strong>2.1 Avapro Docu</strong> — click to expand</summary>

AvAPro derives daily avalanche problems (new snow, wind slab, persistent, aging-persistent, wet snow) from numerical snow-cover model output. The pipeline is compatible with [SNOWPACK](https://www.slf.ch/en/services-and-products/snowpack.html) `.pro` / `.smet` files. Crocus support is partially prepared via threshold sections (`scmopt = cro`) but is not the primary path.

Background on avalanche problems: [EAWS avalanche problems](https://avalanche.report/education/avalanche-problems).

#### Repository Layout

```text
avapro_jul26/
├── config_files/              # Ini files (paths, season, thresholds, aspects)
│   ├── avaprob_RENDEZVOUS26.ini
│   ├── avaprob_rWB_NWP_station.ini
│   └── old/                   # Archived configs
├── input/                     # Optional local SNP copies + icons for notebooks
│   ├── 2026/                  # e.g. older RENDEZVOUS1 / BOW_SUMMIT1 runs
│   ├── icon_aspects/          # Aspect icons for figure notebooks
│   └── Icons-Avalanche-Problems-*/  # EAWS problem icons
├── output/                    # Pickle outputs (created/updated by MAIN)
│   └── 2026/
├── py-code/                   # Python pipeline (run from here)
│   ├── MAIN_ava_prob_seasons.py   # Entry point
│   ├── find_aps.py                # Weak-layer detection + instability
│   ├── post_processing.py         # Assign avalanche problems
│   ├── fu_instab.py               # Instability criteria
│   ├── fu_tau_p_CoJ15.py          # Shear strength (Conlan & Jamieson)
│   ├── get_ac_vh16_v2.py          # Critical crack length (ac)
│   ├── get_s_rb15_v2.py           # Slab support / propagation metrics
│   ├── helper_functions.py
│   └── snowpro/                   # Read .pro / .smet
│       ├── snowpro.py
│       └── pro_helper.py
├── figure_notebooks/          # Visualisation (loads output pickles)
├── Read_me_figures/           # Figures used in README
├── DOCUMENTATION.md           # Source notes for this page
└── README.md                  # Short project overview
```

#### Pipeline Overview

```text
.ini config
    │
    ▼
MAIN_ava_prob_seasons.py
    │
    ├─► match aspects → .pro / .smet pairs
    │
    ├─► find_aps.find_aps()
    │       │  (snowpro reads profiles + meteo)
    │       │  (fu_instab, fu_tau_p, get_ac / get_s)
    │       ▼
    │   df_P_*.pkl , df_met_*.pkl
    │
    └─► post_processing.assigne_avaprobs()
            ▼
        df_P_*_avaprobs_.pkl
```

1. **Config** — paths, season window, aspects, WL and problem thresholds.
2. **Aspect selection** — map `SLOPE_ASPECTS` to SNOWPACK file stems.
3. **`find_aps`** — detect and track potential weak layers; compute instability metrics.
4. **`post_processing`** — assign avalanche-problem flags from thresholds (NAP / PAP / DAP / wind / wet).

Each selected aspect is processed independently in a loop.

#### Dependencies

Install into a Python environment that can import:

| Package | Used for |
|---------|----------|
| `pandas`, `numpy` | Dataframes / arrays |
| `matplotlib` | Optional plotting in modules / notebooks |
| `sympy`, `scipy` | Instability / critical crack length |
| `python-dateutil` | Date handling in instability helpers |

Standard library: `os`, `sys`, `glob`, `pickle`, `configparser`, `datetime`, `math`.

**Important:** always run from `py-code/` so local imports (`find_aps`, `post_processing`, `snowpro`, …) resolve.

#### How to Run

##### 1. Prepare SNOWPACK Output

- For **8 aspects + flat**, set `NUMBER_OF_SLOPES = 9` in the SNOWPACK ini.
- Produce matching `.pro` and `.smet` for each slope.

SNOWPACK naming (9 slopes):

| Aspect | Suffix | Example stem |
|--------|--------|----------------|
| flat   | `_1`   | `Whistler_Rendezvous_HRDPS_2026_1` |
| N      | `_11`  | `…_11` |
| NE     | `_12`  | `…_12` |
| E      | `_13`  | `…_13` |
| SE     | `_14`  | `…_14` |
| S      | `_15`  | `…_15` |
| SW     | `_16`  | `…_16` |
| W      | `_17`  | `…_17` |
| NW     | `_18`  | `…_18` |

**Note:** With the older 5-slope setup (`NUMBER_OF_SLOPES = 5`), aspects were only flat + N/E/S/W as `_1`, `_11`–`_14`. With 9 slopes, **E/S/W indices shift** (`_13/_15/_17`). Do not mix 5-slope files with an 8-aspect AvAPro config.

##### 2. Configure the Ini

Edit (or copy) a file under `config_files/`, e.g. `avaprob_RENDEZVOUS26.ini`.

###### `[avaProbs_general]`

| Key | Role |
|-----|------|
| `SNP_INPUT_FOLDER` | Directory containing `.pro` / `.smet` |
| `SNP_STATION` | Basename of the **flat** run (optional; see below) |
| `output_path` | Output root directory |
| `SLOPE_ASPECTS` | Space-separated list, e.g. `flat N NE E SE S SW W NW` |
| `season_start` / `season_end` | Season window (`YYYY-MM-DD`) |
| `initilization_type` | `station` (AWS / no initial snow profile) or `profile` |
| `scmopt` | `snp` or `cro` — selects which threshold section is used |
| `release` | `trigger` or `natural` |
| `drytime` / `wettime` | Time-of-day windows used in WL / wet logic |
| `rerun_find_WL` | `1` = recompute WLs; `0` = load existing `df_P` / `df_met` pickles |
| `rerun_assign_avaprobs` | `1` = re-assign problems; `0` = load existing `*_avaprobs_.pkl` |

**`SNP_STATION`:** required when file stems differ from the input folder name (e.g. folder `Rendezvous/` but files `Whistler_Rendezvous_HRDPS_2026_1.pro`). If omitted, MAIN uses the folder name as the stem (legacy layout such as `RENDEZVOUS1` / `RENDEZVOUS11`).

Output subdirectory name is always the last component of `SNP_INPUT_FOLDER` (e.g. `…/Rendezvous/` → `output/…/Rendezvous/`).

###### Threshold Sections

- `[avaProbs_thresholds_aps]` — weak-layer detection / tracking.
- `[avaProbs_thresholds_avaprob_snp]` — problem assignment when `scmopt = snp`.
- `[avaProbs_thresholds_avaprob_cro]` — same for `scmopt = cro`.

Comments under `[INFO]` document typical meanings of the thresholds.

##### 3. Run MAIN

```bash
cd /Users/machtl/Documents/Projects_PhD/avapro_jul26/py-code
python MAIN_ava_prob_seasons.py ../config_files/avaprob_RENDEZVOUS26.ini
```

Pass any ini path as the first argument. Paths inside the ini may be absolute or relative to the **current working directory** (`py-code/` when following the command above).

##### 4. Outputs

Under `output_path` + input folder name, for each selected aspect:

| File | Content |
|------|---------|
| `df_P_<stem>.pkl` | Tracked weak layers and instability metrics |
| `df_met_<stem>.pkl` | Meteo time series from `.smet` |
| `df_P_<stem>_avaprobs_.pkl` | Same WL table plus assigned avalanche-problem columns |

Example:

```text
output/2026/Rendezvous/
├── df_P_Whistler_Rendezvous_HRDPS_2026_1.pkl
├── df_met_Whistler_Rendezvous_HRDPS_2026_1.pkl
├── df_P_Whistler_Rendezvous_HRDPS_2026_1_avaprobs_.pkl
├── df_P_Whistler_Rendezvous_HRDPS_2026_11.pkl
├── …
└── df_P_Whistler_Rendezvous_HRDPS_2026_18_avaprobs_.pkl
```

##### 5. Visualisation

MAIN does not write the season overview plots (plotting code is commented out). Use notebooks in `figure_notebooks/` and update:

- paths to the new pickle files,
- aspect lists if using 8 aspects (many notebooks still assume N/E/S/W only),
- icon assets under `input/icon_aspects/` (currently N/E/S/W/flat).

#### Aspect Mapping in MAIN

`MAIN_ava_prob_seasons.py` builds file stems from `SNP_STATION` (or the folder name):

```text
flat → SNP_STATION
N    → SNP_STATION + "1"   →  …11
NE   → … + "2"             →  …12
E    → … + "3"             →  …13
SE   → … + "4"             →  …14
S    → … + "5"             →  …15
SW   → … + "6"             →  …16
W    → … + "7"             →  …17
NW   → … + "8"             →  …18
```

Supported keys in `SLOPE_ASPECTS`: `flat`, `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, `NW`.  
You can run a subset (e.g. `SLOPE_ASPECTS= flat N S`) as long as the matching files exist.

#### Main Modules (Quick Reference)

| Script / package | Purpose |
|------------------|---------|
| `MAIN_ava_prob_seasons.py` | Orchestrate season run from ini |
| `find_aps.py` | Detect / track potential weak layers over the season |
| `post_processing.py` | Assign NAP / PAP / DAP / wind / wet problems |
| `fu_instab.py` | Instability criteria for candidate layers |
| `fu_tau_p_CoJ15.py` | Weak-layer shear strength evolution |
| `get_ac_vh16_v2.py` | Critical crack length |
| `get_s_rb15_v2.py` | Slab / propagation support metrics |
| `snowpro/` | Robust read of SNOWPACK `.pro` and `.smet` into pandas structures |

</details>

### Current Rendezvous Example (ISSW26)

- **Input:** [`/Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26/out/2026/Rendezvous/`](file:///Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26/out/2026/Rendezvous/)
- **Station stem (`SNP_STATION`):** `Whistler_Rendezvous_HRDPS_2026_1`
- **Aspects:** `flat N NE E SE S SW W NW`
- **Config:** `config_files/avaprob_RENDEZVOUS26.ini`
- **Output:** `output/2026/Rendezvous/` (relative to `py-code/`)

```bash
cd /Users/machtl/Documents/Projects_PhD/avapro_jul26/py-code
python MAIN_ava_prob_seasons.py ../config_files/avaprob_RENDEZVOUS26.ini
```
