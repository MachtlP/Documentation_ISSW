# Spatial config

<p class="section-updated">Last updated: 15 Jul 2026</p>

This project investigates how different spatial sampling strategies influence avalanche problem identification and regional hazard assessment using distributed SNOWPACK simulations. By comparing multiple HRDPS grid configurations across four forecast regions in western Canada, the study evaluates their effects on the detection, spatial prevalence, and temporal evolution of avalanche problems, as well as their agreement with operational hazard assessments and observed avalanche activity. This documentation summarizes the project's methodology, implementation, analyses, and ongoing progress toward identifying representative and operationally useful simulation strategies.

<div class="note-box">
<p class="note-box__title">Overleaf Paper Draft</p>
<div class="note-box__body">
<a href="https://www.overleaf.com/5937948778fmrynphxshsj#43b1cd" target="_blank" rel="noopener">https://www.overleaf.com/5937948778fmrynphxshsj#43b1cd</a>
</div>
</div>

## 1. Brainstorm Flowchart

<p class="section-updated">Last updated: 16 Jul 2026</p>

### Research idea: Investigate the impact of instability distribution of different spatial grid configs

How does the spatial configuration of snowpack simulations influence the simulated distribution of instability and the resulting identification and regional prominence of avalanche problems?

## 2. Grid configs

<p class="section-updated">Last updated: 15 Jul 2026</p>

### 2.1 Full grid

<p class="section-updated">Last updated: 15 Jul 2026</p>

Full HRDPS orography clipped to the four study areas (from HRDPS DEM analysis):

![HRDPS orography — Whistler-Blackcomb, Rogers Pass, Banff, Mike Wiegele Heliskiing](assets/images/dem_hrdps_orography_sites.png)

<p class="fig-caption"><strong>Figure 1.</strong> HRDPS orography (elevation, m) clipped to the four operation polygons: Whistler Blackcomb Heliskiing, Rogers Pass, Banff, and Mike Wiegele Heliskiing.</p>

Elevation bands (below treeline / treeline / alpine):

![Elevation bands by site — below treeline, treeline, alpine](assets/images/dem_elevation_bands.png)

<p class="fig-caption"><strong>Figure 2.</strong> Elevation-band classification within each operation polygon (below treeline, treeline ±100 m, alpine) using site-specific treeline heights.</p>

Hypsometry inside operation polygons:

![Hypsometry inside operation polygons by elevation band](assets/images/dem_hypsometry.png)

<p class="fig-caption"><strong>Figure 3.</strong> Hypsometry (grid-cell counts by 200 m elevation band) inside the four operation polygons, coloured by treeline class.</p>

<p class="table-caption"><strong>Table 1.</strong> Summary statistics of HRDPS grid cells inside each operation polygon, including elevation range, treeline definition, and area fractions below / at / above treeline.</p>

| region | n_cells | area_km2_approx | z_min | z_median | z_mean | z_max | treeline_m | treeline_band_m | n_below | n_treeline | n_alpine | frac_below | frac_treeline | frac_alpine | area_below_km2 | area_treeline_km2 | area_alpine_km2 |
|--------|--------:|----------------:|------:|---------:|-------:|------:|-----------:|-----------------|--------:|-----------:|---------:|-----------:|--------------:|------------:|---------------:|------------------:|----------------:|
| Whistler Blackcomb Heliskiing | 284 | 1775 | 730 | 1777 | 1730 | 2340 | 1900 | 1800–2000 | 149 | 83 | 52 | 52.5% | 29.2% | 18.3% | 931 | 519 | 325 |
| Rogers Pass | 212 | 1325 | 1255 | 1872 | 1885 | 2678 | 2100 | 2000–2200 | 140 | 39 | 33 | 66.0% | 18.4% | 15.6% | 875 | 244 | 206 |
| Banff | 437 | 2731 | 1452 | 2180 | 2135 | 2695 | 2300 | 2200–2400 | 229 | 138 | 70 | 52.4% | 31.6% | 16.0% | 1431 | 862 | 438 |
| Mike Wiegele Heliskiing | 729 | 4556 | 715 | 1638 | 1611 | 2524 | 2100 | 2000–2200 | 628 | 71 | 30 | 86.1% | 9.7% | 4.1% | 3925 | 444 | 188 |

<p class="table-caption"><strong>Table 2.</strong> Number of SNOWPACK simulations for the full-grid configuration (9 simulations per HRDPS cell).</p>

| region | n_cells | snowpack simulations |
|--------|--------:|---------------------:|
| Whistler Blackcomb Heliskiing | 284 | 2556 |
| Rogers Pass | 212 | 1908 |
| Banff | 437 | 3933 |
| Mike Wiegele Heliskiing | 729 | 6561 |

<div class="todo-box">
<p class="todo-box__title">Next to do's — Spatial config › 2.1 Full grid</p>
<div class="todo-box__body">
<ul>
<li>run awsome for full grid</li>
</ul>
</div>
</div>

### 2.2 Terrain informed grid

<p class="section-updated">Last updated: 15 Jul 2026</p>

For the terrain-informed grid we will use avalanche release areas from **autoATES v3** (PRA model output) to sample HRDPS / SNOWPACK points in likely start-zone terrain rather than every grid cell.

Below: mail from John:

<div class="quote-box">
<div class="quote-box__body">
<p><em>Hey Martin,</em></p>
<p><em>I would be happy to provide the PRA model output for your analysis. Are you working in a specific study area?</em></p>
<p><em>I've been doing a lot of development work on the autoATESv3.0 model the past couple weeks and have made some significant changes to the PRA model output. The biggest change is that I now output two scenarios, one that captures frequent start zones and one for extreme start zones. The frequent ones are targeted at the most likely release areas based on slope angle, forest cover, and wind shelter. The extreme ones include lower angle slopes and start zones in more forested areas. So, depending on how broad of a net you want to cast, you could select one or the other of these scenarios. The frequent scenario would be better for narrowing down the location of the most common start zone locations within the terrain.</em></p>
<p><em>The other major change is that the PRA models outputs polygons for individual start zones for each scenario. This might not be useful for you if you just want to know the location of potential start zones. The polygons are mostly useful for narrowing down the potential size of start zones and assessing the relative likelihood of each polygon being a start zone. Declan and I are using this to identify the most likely release areas from BC MOT control paths and it has been pretty useful.</em></p>
<p><em>The PRA model runs fairly quickly, so I should be able to run it for you in your study area. I haven't run the PRA model for all the AvCan forecast zones yet, still waiting to finalize the validation work before running it on large scales.</em></p>
<p><em>Cheers,<br>John</em></p>
</div>
</div>

<div class="todo-box">
<p class="todo-box__title">Next to do's — Spatial config › 2.2 Terrain informed grid</p>
<div class="todo-box__body">
<ul>
<li>get johns maps</li>
<li>choose grid strategie</li>
<li>run sim</li>
</ul>
</div>
</div>

### 2.3 Aggregated grid

<p class="section-updated">Last updated: 15 Jul 2026</p>

- **Downscale** onto a coarser spatial unit (e.g. hexagon aggregation)
- **Hexagon** tiling as the aggregation geometry
- **Temperature:** CanHydro / Pomeroy-style lapse rate for temp
- **Precipitation:** nothing applied for precip (no lapse / adjustment yet)
- **Pixel size:** ~6–7× HRDPS grid resolution (Y)
- **Open question:** is there actually variability across aggregated units?

<div class="todo-box">
<p class="todo-box__title">Next to do's — Spatial config › 2.3 Aggregated grid</p>
<div class="todo-box__body">
<ul>
<li>define strategy</li>
</ul>
</div>
</div>
