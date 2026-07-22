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

<p class="section-updated">Last updated: 15 Jul 2026</p>

<div class="note-box">
<p class="note-box__title">Project Simulations Folder</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26">/Users/machtl/Documents/Projects_PhD/SNP_runs_for_ISSW26</a>
</div>
</div>

Snowpack is simulated at point locations with a physics-based model (e.g. SNOWPACK / CROCUS-class setup) forced by:

1. **AWS** — observed station meteorology (temperature, humidity, wind, precipitation / snow height)
2. **HRDPS** — downscaled numerical weather prediction fields for the same points

Simulations produce the layered snowpack state (grain type, hardness, density, weak layers) that Avapro uses to flag avalanche problems over the season.

#### Simulations Inputs

##### .sno Files

### 1.3 Validation Dataset

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
