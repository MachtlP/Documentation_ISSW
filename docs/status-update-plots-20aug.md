# XII. Status Update Plots 20 Aug

<p class="section-updated">Last updated: 20 Aug 2026</p>

## 1. Plots for Paper Config (XI)

See **[XI. Plots for Paper Config](plots-for-paper-config.md)** (last updated 19 Aug 2026).

That page collects exploratory plots for how InfoEx / AvCan danger and avalanche problems align across the four study areas, and for comparing **full grid**, **15 km hex**, and **single-point** configurations in the paper window. Outline:

1. **Grid configurations** — full HRDPS grid, semi-distributed hex, and single-point setups; fitted hexes and MWHS domain maps.
2. **Period definition** — InfoEx vs AvCan danger / problem timelines for Whistler, Rogers, Banff, and MWHS (candidate Dec window highlighted).
3. **Precip Analysis** — single-median, hex, and full-grid forcing (TA, HN24/48, HS) for the candidate period.
4. **Precip distribution comparison** — single-point vs hex vs full-grid ranks and envelopes for Whistler, MWHS, GNP, and Banff (PSUM / HN24 / HN48).
5. **Stability distribution analysis** — QMAH SK38, Punstable, CCL, and slab-height distributions (Banff 20–23 Dec 2025, 18Z).
6. **AvAPro** — daily problem prevalence (grid vs hex vs station) for Whistler, plus all-ops snapshot bars and Dec-window timeline.

## 2. Precip

<div class="note-box">
<p class="note-box__title">Precipitation analysis notebook</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/docker_fun/docs/notebooks/Precip_analysis.ipynb">/Users/machtl/Documents/docker_fun/docs/notebooks/Precip_analysis.ipynb</a>
</div>
</div>

- Updating comparison plots to **violin** for full grid, **bee swarm** for hex, and **markers** for medians.
- Included **median run** now.
- **Full-season** values.

### 2.1 Season overview — all aspects — only days where HN24 > 0

**HN24 total**

Full season (1 Sep 2025 → 31 May 2026), HN24 > 0 days only: grid IQR + mean, hex min–max + median, and single-point markers by elevation band.

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24" data-type="image" data-title="Whistler · HN24 · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_whistler.png" alt="Whistler full-season HN24 > 0 days by elevation band" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24" data-type="image" data-title="Rogers / GNP · HN24 · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_rogers.png" alt="Rogers GNP full-season HN24 > 0 days by elevation band" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_banff.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24" data-type="image" data-title="Banff · HN24 · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_banff.png" alt="Banff full-season HN24 > 0 days by elevation band" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_mwhs.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24" data-type="image" data-title="MWHS · HN24 · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_mwhs.png" alt="MWHS full-season HN24 > 0 days by elevation band" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 1.</strong> Season overview — HN24 total on days with HN24 > 0 (all aspects), 1 Sep 2025 → 31 May 2026: Whistler, Rogers / GNP, Banff, MWHS. Click a miniature to maximize.</p>

**HN24 offset mm**

Offset of hex (min/max, median) and single-point relative to the grid mean (μ), same days and window.

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_offset_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24-offset" data-type="image" data-title="Whistler · HN24 offset (config – grid mean) · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_offset_whistler.png" alt="Whistler HN24 offset vs grid mean by elevation band" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_offset_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24-offset" data-type="image" data-title="Rogers / GNP · HN24 offset (config – grid mean) · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_offset_rogers.png" alt="Rogers GNP HN24 offset vs grid mean by elevation band" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_offset_banff.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24-offset" data-type="image" data-title="Banff · HN24 offset (config – grid mean) · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_offset_banff.png" alt="Banff HN24 offset vs grid mean by elevation band" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_hn24_offset_mwhs.png" class="glightbox image-zoom" data-gallery="status-precip-season-hn24-offset" data-type="image" data-title="MWHS · HN24 offset (config – grid mean) · HN24 > 0 days · all aspects · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_hn24_offset_mwhs.png" alt="MWHS HN24 offset vs grid mean by elevation band" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 2.</strong> Season overview — HN24 offset (config − grid mean) on days with HN24 > 0 (all aspects), 1 Sep 2025 → 31 May 2026. Click a miniature to maximize.</p>

**Season summary tables** (filter: precip > 0 days · all aspects)

Means over those days only. `mean_off_*` = config − grid mean (mm); `mean_rel_*` = (config − μ)/μ; `mean_rank_*` ≈ 50 if unbiased; `season_rel_*` from season sums; single-point is flat Config III.

**Whistler**

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 178 | 225 | 25 | −28.577 | −4.747 | 25.526 | 2.993 | −0.279 | 0.036 | 56.464 | 60.733 | 85.955 | 17397.857 | 16552.890 | 17930.57 | −0.049 | 0.031 |
| TL | 173 | 165 | 25 | −21.164 | −1.713 | 22.763 | −1.610 | −0.095 | −0.090 | 60.266 | 56.805 | 85.549 | 17016.298 | 16720.015 | 16737.85 | −0.017 | −0.016 |
| BTL | 168 | 145 | 20 | 5.107 | 26.613 | 48.791 | 2.959 | 0.846 | −0.059 | 79.620 | 64.100 | 54.762 | 12161.496 | 16632.450 | 12658.55 | 0.368 | 0.041 |

**Rogers / GNP**

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 184 | 230 | 10 | −65.428 | −55.613 | −45.798 | −6.358 | −0.679 | −0.076 | 26.846 | 50.556 | 7.609 | 17094.181 | 6861.455 | 15924.28 | −0.599 | −0.068 |
| TL | 177 | 200 | 10 | −49.821 | −41.124 | −32.426 | −8.555 | −0.666 | −0.169 | 37.062 | 51.356 | 15.254 | 11987.502 | 4708.595 | 10473.25 | −0.607 | −0.126 |
| BTL | 172 | 380 | 10 | −17.301 | −5.533 | 6.235 | −20.461 | 0.288 | −0.449 | 57.421 | 47.945 | 47.674 | 10775.933 | 9824.230 | 7256.59 | −0.088 | −0.327 |

**Banff**

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 185 | 480 | 15 | −39.357 | −26.544 | −5.751 | −8.008 | −0.658 | −0.234 | 45.087 | 53.493 | 32.973 | 10399.734 | 5489.12 | 8918.34 | −0.472 | −0.142 |
| TL | 170 | 391 | 15 | −22.391 | −12.647 | 6.144 | −10.821 | −0.434 | −0.372 | 55.298 | 53.723 | 53.529 | 8650.472 | 6500.55 | 6810.86 | −0.249 | −0.213 |
| BTL | 159 | 870 | 15 | −24.545 | −5.737 | 17.539 | −16.552 | −0.159 | −0.564 | 60.244 | 50.043 | 63.522 | 7038.274 | 6126.04 | 4406.55 | −0.130 | −0.374 |

**MWHS**

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 191 | 270 | 15 | −81.206 | −54.393 | −28.004 | −9.410 | −0.731 | −0.226 | 23.425 | 46.033 | 17.277 | 17920.364 | 7531.270 | 16122.96 | −0.580 | −0.100 |
| TL | 192 | 445 | 20 | −53.278 | −41.827 | −25.428 | −12.554 | −0.671 | −0.305 | 33.316 | 48.408 | 17.708 | 14918.136 | 6887.320 | 12507.75 | −0.538 | −0.162 |
| BTL | 187 | 1490 | 30 | −45.586 | −16.262 | 47.405 | −23.643 | −0.455 | −0.590 | 52.192 | 46.059 | 86.096 | 12061.894 | 9020.965 | 7640.65 | −0.252 | −0.367 |

#### Interpretation — season HN24 offsets

Numbers below are from **HN24 days, all aspects** (the first execute block). Precip-day and flat-only tables are almost the same for HN24; that is discussed at the end. Offsets are millimetres of 24 h new snow versus the **spatial grid mean** μ in that elevation band. Negative = the reduced config snows less than the full grid.

##### How to read one operation (Banff ALP as the example)

Take Banff alpine, 196 HN24 days, 480 grid members, 15 hex members (3 hexes × 5 aspects):

| Column | Banff ALP | Meaning |
|--------|-----------|---------|
| `mean_off_hex_med` / `mean_off_sp` | −25 mm / −8 mm | Average daily (config − μ). Hex median is 2.5 cm too dry per snow day; Config III is 0.8 cm too dry. |
| `season_rel_hex_med` / `season_rel_sp` | −47% / −14% | $(\Sigma\mathrm{config} - \Sigma\mu)/\Sigma\mu$ over those days. This is the “did we get the winter right” number. Prefer it over `mean_rel_*`. |
| `mean_rel_*` | −70% / −31% | Mean of $(\mathrm{config}-\mu)/\mu$ per day. It **over-weights tiny snow days**, so it looks worse than the season total. |
| `mean_rank_*` | 47 / 55 | Percentile of the config in that day’s grid. 50 = a typical cell. Rank and millimetre offset **disagree when the field is right-skewed**: a few deep cells pull μ above the median, so a config can sit near the median cell (rank ~50) and still be dry vs the mean. |
| `pct_days_hex_covers_mean` | 27% | Share of days where μ lies between hex min and hex max. Low = the hex set does not even bracket the grid, so it is not a conservative envelope. |

The same Banff table by band: hex dry-bias **shrinks** downslope (ALP −47% → TL −25% → BTL −13%) while Config III **grows** downslope (ALP −14% → TL −22% → BTL −38%). Hex centroids miss the high/wet ALP terrain; the band-median single point is a decent ALP cell but a poor match to a BTL field that includes valley bottoms.

##### Climate comparison

Whistler is **maritime**, Rogers / Glacier **transitional**, Banff and MWHS **continental**. Season Σμ (ALP, HN24 days) already shows the gradient: Whistler 17.4 m, Rogers 17.1 m, MWHS 17.9 m, Banff 10.4 m. MWHS is a high, snowy continental range; Banff is the dry continental end-member.

**Maritime — Whistler.** ALP/TL hex medians sit within 5 mm of μ (season −5% / −2%), the hex envelope contains μ on ~80% of days, and Config III is within ±3% of the season total. Rank ~56–60: slightly above the median cell, slightly below or near the mean — the usual right-skew. The failure mode is **BTL hex**: median +28 mm, season **+37%**, rank 78, envelope covers μ only 46%. With only four BTL hexes in a 145-cell band, those hexes sit on the snowy side; hex *min* is already +5 mm above μ, so the envelope cannot recover. Config III stays honest at BTL (+4%).

**Transitional — Rogers.** Sharp wet-west / dry-east (and elevation) gradients. ALP/TL hex medians are −52 / −39 mm (season **−60% / −61%**). Hex *max* is still 43 mm below μ in ALP; the envelope contains μ on **4% / 8%** of days. Two ALP hexes are systematically the dry part of the grid. Config III recovers ALP (−7%) and TL (−13%) far better than hex, then fails at BTL (−33%) for the same valley-bottom reason as Banff.

**Continental — Banff.** Lower totals, same qualitative pattern as Rogers but less extreme at ALP: hex season −47 / −25 / −13%; Config III −14 / −22 / −38%. Envelope coverage 27 / 44 / 49% — better than Rogers, still not an envelope at ALP (hex max −5 mm vs μ).

**Continental — MWHS.** Snowier than Banff, hex dry-bias like Rogers: ALP/TL season −58% / −54%, rank 29 / 37, coverage 14 / 13%. BTL is mixed: median still −25% but coverage **75%** because six hexes in a 1490-cell band make a wide min–max even when the median is dry. Config III: −10 / −16 / −37%, the same elevation pattern as Banff and Rogers.

##### What holds across climates

1. **Config III beats hex for ALP season totals everywhere except Whistler**, where both are already close. Hex is not a safer substitute for the grid at Rogers or MWHS ALP — the whole hex range sits below μ.
2. **Where the reduced config breaks depends on climate and elevation.** Maritime: hex BTL too *wet* (undersampled snowy hexes). Transitional/continental: hex ALP/TL too *dry* (centroids miss orographic maxima); Config III too *dry* at BTL (band median is not a valley).
3. **Absolute millimetres vs relative error.** Whistler ALP hex −5 mm is −5% of a big winter. Banff ALP hex −25 mm is −47% of a smaller winter. Continental operations look worse in `season_rel_*` even when the millimetre offset is comparable to Rogers.
4. **Rank is not a substitute for bias.** Rogers ALP hex rank 31 matches the dry bias. Banff ALP hex rank 47 looks almost unbiased while season_rel is −47% — use both.

##### HN24 days vs precip days, and all aspects vs flat

Precip-day tables change `n_days` by a few days and leave `season_rel_*` essentially unchanged: winter ΣHN24 is dominated by days that both precipitate and produce new snow. Flat-only vs F+4 also barely moves HN24 (Banff ALP hex season_rel −47.4% both ways). New snow is precip-driven; aspect mainly changes energy, not HN24. Use the HN24-day, all-aspect block as the paper numbers unless you are explicitly discussing rain vs snow or aspect.

**Cross-climate summary** (HN24 days). `season_rel_*` is $(\Sigma\mathrm{config} - \Sigma\mu)/\Sigma\mu$; `mean_off_*` is mm/day; rank 50 = typical grid cell. Full frame: `season_compare(days, aspects)`.

| label | climate | band | n_days | n_grid | n_hex | mean_off_hex_med | mean_off_sp | season_rel_hex_med | season_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm |
|-------|---------|------|--------|--------|-------|------------------|-------------|--------------------|---------------|-------------------|--------------|--------------------|----------------|
| Whistler | maritime | ALP | 176 | 225 | 25 | −4.882 | 2.945 | −0.049 | 0.030 | 55.634 | 59.951 | 81.250 | 17412.188 |
| Whistler | maritime | TL | 166 | 165 | 25 | −1.879 | −1.771 | −0.018 | −0.017 | 58.205 | 54.598 | 79.518 | 17031.917 |
| Whistler | maritime | BTL | 160 | 145 | 20 | 27.799 | 2.962 | 0.365 | 0.039 | 78.017 | 61.703 | 46.250 | 12184.689 |
| Rogers / GNP | transitional | ALP | 197 | 230 | 10 | −52.103 | −6.072 | −0.599 | −0.070 | 30.952 | 53.098 | 4.061 | 17125.795 |
| Rogers / GNP | transitional | TL | 185 | 200 | 10 | −39.488 | −8.328 | −0.608 | −0.128 | 39.162 | 52.838 | 8.108 | 12013.891 |
| Rogers / GNP | transitional | BTL | 174 | 380 | 10 | −5.426 | −20.435 | −0.087 | −0.329 | 57.016 | 47.649 | 38.506 | 10812.298 |
| Banff | continental | ALP | 196 | 480 | 15 | −25.219 | −7.691 | −0.474 | −0.145 | 47.487 | 55.422 | 27.041 | 10431.951 |
| Banff | continental | TL | 179 | 390 | 15 | −12.245 | −10.511 | −0.252 | −0.216 | 56.559 | 55.063 | 43.575 | 8692.381 |
| Banff | continental | BTL | 178 | 870 | 15 | −5.226 | −15.003 | −0.131 | −0.377 | 63.596 | 54.481 | 48.876 | 7077.057 |
| MWHS | continental | ALP | 207 | 270 | 15 | −50.319 | −8.814 | −0.580 | −0.102 | 28.757 | 49.618 | 14.010 | 17947.359 |
| MWHS | continental | TL | 206 | 445 | 20 | −39.105 | −11.821 | −0.539 | −0.163 | 37.335 | 51.402 | 13.107 | 14942.854 |
| MWHS | continental | BTL | 199 | 1490 | 30 | −15.374 | −22.310 | −0.253 | −0.368 | 54.679 | 48.917 | 75.377 | 12080.432 |

### 2.2 Season overview — flat only

Same season window and HN24 > 0 day filter, but **flat aspect only**.

**HN24 total**

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24" data-type="image" data-title="Whistler · HN24 · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_whistler.png" alt="Whistler flat-aspect season HN24 totals" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24" data-type="image" data-title="Rogers / GNP · HN24 · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_rogers.png" alt="Rogers GNP flat-aspect season HN24 totals" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_banff.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24" data-type="image" data-title="Banff · HN24 · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_banff.png" alt="Banff flat-aspect season HN24 totals" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_mwhs.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24" data-type="image" data-title="MWHS · HN24 · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_mwhs.png" alt="MWHS flat-aspect season HN24 totals" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 3.</strong> Season overview (flat only) — HN24 total on days with HN24 > 0, 1 Sep 2025 → 31 May 2026. Click a miniature to maximize.</p>

**HN24 offset mm**

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_offset_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24-offset" data-type="image" data-title="Whistler · HN24 offset (config – grid mean) · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_offset_whistler.png" alt="Whistler flat-aspect HN24 offset vs grid mean" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_offset_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24-offset" data-type="image" data-title="Rogers / GNP · HN24 offset (config – grid mean) · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_offset_rogers.png" alt="Rogers GNP flat-aspect HN24 offset vs grid mean" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_offset_banff.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24-offset" data-type="image" data-title="Banff · HN24 offset (config – grid mean) · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_offset_banff.png" alt="Banff flat-aspect HN24 offset vs grid mean" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_season_flat_hn24_offset_mwhs.png" class="glightbox image-zoom" data-gallery="status-precip-season-flat-hn24-offset" data-type="image" data-title="MWHS · HN24 offset (config – grid mean) · HN24 > 0 days · flat aspect only · 2025-09-01 → 2026-05-31">
      <img src="../assets/images/paper_config/precip_season_flat_hn24_offset_mwhs.png" alt="MWHS flat-aspect HN24 offset vs grid mean" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 4.</strong> Season overview (flat only) — HN24 offset (config − grid mean) on days with HN24 > 0, 1 Sep 2025 → 31 May 2026. Click a miniature to maximize.</p>

**Season summary tables** (filter: HN24 > 0 days · flat aspect)

<details class="table-dropdown">
<summary><strong>Whistler</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 176 | 45 | 5 | −28.984 | −4.882 | 26.043 | 2.945 | −0.320 | −0.023 | 55.634 | 59.951 | 81.250 | 17412.188 | 16552.890 | 17930.57 | −0.049 | 0.030 |
| TL | 166 | 33 | 5 | −22.150 | −1.879 | 23.629 | −1.771 | −0.144 | −0.140 | 58.205 | 54.598 | 79.518 | 17031.917 | 16720.015 | 16737.85 | −0.018 | −0.017 |
| BTL | 160 | 29 | 4 | 5.236 | 27.817 | 51.122 | 2.980 | 0.708 | −0.130 | 78.021 | 61.725 | 46.250 | 12181.671 | 16632.450 | 12658.55 | 0.365 | 0.039 |

</details>

<details class="table-dropdown">
<summary><strong>Rogers / GNP</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 197 | 46 | 2 | −61.271 | −52.103 | −42.936 | −6.072 | −0.710 | −0.159 | 30.952 | 53.098 | 4.061 | 17125.795 | 6861.455 | 15929.52 | −0.599 | −0.070 |
| TL | 185 | 40 | 2 | −47.809 | −39.488 | −31.167 | −8.328 | −0.703 | −0.259 | 39.162 | 52.838 | 8.108 | 12013.891 | 4708.595 | 10473.25 | −0.608 | −0.128 |
| BTL | 174 | 76 | 2 | −17.311 | −5.426 | 6.458 | −20.435 | 0.261 | −0.515 | 57.016 | 47.649 | 38.506 | 10812.298 | 9868.125 | 7256.59 | −0.087 | −0.329 |

</details>

<details class="table-dropdown">
<summary><strong>Banff</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 196 | 96 | 3 | −37.321 | −25.227 | −5.325 | −7.699 | −0.695 | −0.310 | 47.472 | 55.402 | 27.041 | 10433.554 | 5489.12 | 8924.52 | −0.474 | −0.145 |
| TL | 179 | 78 | 3 | −21.511 | −12.257 | 5.815 | −10.523 | −0.510 | −0.456 | 56.544 | 55.057 | 43.575 | 8694.480 | 6500.55 | 6810.86 | −0.252 | −0.217 |
| BTL | 178 | 174 | 3 | −22.143 | −5.226 | 15.446 | −15.003 | −0.302 | −0.652 | 63.596 | 54.476 | 48.876 | 7077.022 | 6146.75 | 4406.55 | −0.131 | −0.377 |

</details>

<details class="table-dropdown">
<summary><strong>MWHS</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 207 | 54 | 3 | −75.060 | −50.319 | −25.866 | −8.814 | −0.758 | −0.305 | 28.757 | 49.618 | 14.010 | 17947.359 | 7531.270 | 16122.96 | −0.580 | −0.102 |
| TL | 206 | 89 | 4 | −49.777 | −39.105 | −23.820 | −11.821 | −0.704 | −0.376 | 37.335 | 51.402 | 13.107 | 14942.854 | 6887.320 | 12507.75 | −0.539 | −0.163 |
| BTL | 199 | 298 | 6 | −42.930 | −15.374 | 44.453 | −22.310 | −0.526 | −0.644 | 54.679 | 48.917 | 75.377 | 12080.432 | 9020.965 | 7640.65 | −0.253 | −0.368 |

</details>

### 2.3 Low / avg / high precip days

HN24 offsets split by local precip terciles (aspects=all): season relative error \((\Sigma\text{config} - \Sigma\mu)/\Sigma\mu\) and mean daily offset (config − grid mean, mm).

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_tercile_season_rel.png" class="glightbox image-zoom" data-gallery="status-precip-tercile" data-type="image" data-title="HN24 season relative offset by precip tercile · aspects=all · (Σconfig − Σμ) / Σμ">
      <img src="../assets/images/paper_config/precip_tercile_season_rel.png" alt="HN24 season relative offset by precip tercile" />
    </a>
    <span class="pro-evo-grid__label">Season rel %</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_tercile_mean_off.png" class="glightbox image-zoom" data-gallery="status-precip-tercile" data-type="image" data-title="HN24 mean daily offset by precip tercile · aspects=all · config – grid mean (mm)">
      <img src="../assets/images/paper_config/precip_tercile_mean_off.png" alt="HN24 mean daily offset by precip tercile" />
    </a>
    <span class="pro-evo-grid__label">Mean daily offset mm</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 5.</strong> HN24 by precip tercile (low / avg / high) — season relative offset and mean daily offset vs grid mean, aspects=all. Click a miniature to maximize.</p>

#### Interpretation by operation and band

Terciles are local. A Banff “high” ALP day is ≥ ~6 mm grid-mean precip; a Whistler “high” ALP day is ≥ ~14 mm. Millimetre offsets (`mean_off_*`) show where the winter is won or lost; `season_rel_*` on low days is noisy because μ is small.

**Whistler (maritime)**

- **Alpine.** Hex is a few millimetres dry in every tercile. Relative error collapses on the days that matter: −38% on low days (tiny totals) → −9% average → **−2% on high days** (Σμ ≈ 13 m of the 17 m winter). Config III turns **wet** on high days (+6%, +13 mm/day). Hex envelope coverage rises from 73% to 95% as storms get bigger — maritime ALP hexes sample the same storms as the grid.
- **Treeline.** Same pattern, even closer: hex high-day season rel −0.6%. Config III is slightly dry on average days (−8%) and near zero on high days (+1%).
- **Below treeline.** The season-level +37% hex wet bias is a **high-precip** problem: +64 mm/day and **+41%** of those days’ ΣHN24, and the envelope contains μ on only 32% of high days. Low days are almost unbiased (+4%). Four BTL hexes sit on the snowy side of the band, and that mismatch is expressed when it snows hard. Config III stays within +9% on high BTL days.

**Rogers / GNP (transitional)**

- **Alpine.** Hex millimetre bias scales with the storm: −8 / −43 / **−117 mm/day**. Relative error stays brutal (−75 / −70 / −56%). On high days the hex *max* never reaches μ (coverage **0%**). Two ALP hexes are the dry side of a sharp orographic gradient, and storms make that worse in millimetres. Config III is the opposite: relative error is small on high days (**−5%**) — the band-median cell is a decent ALP storm sampler.
- **Treeline.** Hex ~−60% in every tercile (−92 mm/day on high). Config III improves toward high days (−30% → −10%).
- **Below treeline.** Hex is only mildly dry (−6% high). Config III is the failure mode: **−53% / −37% / −30%**, and −43 mm/day on high BTL days. Valley bottoms in the grid have no analogue in the band-median point.

**Banff (continental)**

Cuts are lower (ALP 1.2 / 6.1 mm). High-day Σ still dominates the winter (ALP 8.1 of 10.4 m).

- **Alpine.** Hex relative error looks worst on low days (−88%) because μ is tiny; high days are −45% and **−59 mm/day**, coverage 21%. Config III high days are only **−9%** — same “good ALP storm cell” as Rogers.
- **Treeline.** Hex −71% → −23% from low to high; Config III −51% → −16%. Both improve relatively as precip increases; hex remains the drier of the two on high days (−26 vs −19 mm).
- **Below treeline.** Hex almost recovers on storms (−9% high). Config III does not (−32%, −32 mm/day). Continental BTL is where a single band-median point cannot represent a field that includes valley rain/snow shadows.

**MWHS (continental, snowier)**

Cuts resemble Rogers (ALP 3.2 / 11.5 mm), totals resemble Whistler.

- **Alpine.** Hex −12 / −47 / **−104 mm/day** (−89 / −70 / −52%). Coverage falls to 9% on high days. Config III high days **−6%**. Same transitional/continental ALP story: hex centroids miss the wet high terrain when it actually precipitates.
- **Treeline.** Hex −78 / −65 / −49%; Config III high −11%.
- **Below treeline.** Hex envelope is wide (coverage 73 → 95%) so it *contains* μ even while the median stays dry (−22% high, −30 mm/day). Config III is worse on every tercile at BTL (−77 / −47 / −30%, −42 mm/day on high).

#### What the split changes in the paper story

1. **Hex millimetre errors live on high precip days** — the third of days that hold most of ΣHN24. Reporting only a season mean hides that Rogers/MWHS ALP hex is ~10 cm/day too dry in storms.
2. **Config III relative error lives on low days and at BTL.** On high ALP days it is within ~5–10% of the grid in every climate. It is the wrong tool for light days and for valley BTL.
3. **Whistler BTL hex wet bias is not a drizzle artefact** — it is +64 mm/day on the high tercile.
4. Do not compare “high” millimetres across climates without the cuts. Banff high ≈ Whistler average.

### 2.4 Detailed period

Candidate window **17–31 Dec 2025**: daily grid violin + hex beeswarm + median HRDPS.

**PSUM 24h**

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum" data-type="image" data-title="Whistler · PSUM 24h · daily 00:00 grid violin + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_whistler.png" alt="Whistler PSUM 24h detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum" data-type="image" data-title="Rogers / GNP · PSUM 24h · daily 00:00 grid violin + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_rogers.png" alt="Rogers GNP PSUM 24h detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_banff.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum" data-type="image" data-title="Banff · PSUM 24h · daily 00:00 grid violin + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_banff.png" alt="Banff PSUM 24h detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_mwhs.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum" data-type="image" data-title="MWHS · PSUM 24h · daily 00:00 grid violin + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_mwhs.png" alt="MWHS PSUM 24h detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 6.</strong> Detailed period — PSUM 24h daily grid violin + hex beeswarm + median HRDPS (17–31 Dec 2025). Click a miniature to maximize.</p>

**PSUM 24h** (Whistler, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p43 (rank 10–90: p34–p50; bias −1.143 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 100% of days. Hex contains 61% of grid cells and spans 0.66× the grid p10–p90 width (hex median bias −1.393 mm).
- **Treeline:** single-point sits at grid p44 (rank 10–90: p37–p58; bias −0.916 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 100% of days. Hex contains 51% of grid cells and spans 0.51× the grid p10–p90 width (hex median bias −1.074 mm).
- **Below treeline:** single-point sits at grid p43 (rank 10–90: p35–p82; bias −1.071 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 60% of days. Hex contains 43% of grid cells and spans 0.45× the grid p10–p90 width (hex median bias +0.237 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 77 | 5 | 15 | 15.590 | −1.143 | −1.393 | 42.857 | 34.286 | 49.610 | 100.0 | 100.0 | 100.0 | 60.519 | 0.662 |
| TL | 64 | 5 | 15 | 14.662 | −0.916 | −1.074 | 43.750 | 36.875 | 58.125 | 100.0 | 100.0 | 100.0 | 51.146 | 0.515 |
| BTL | 143 | 4 | 15 | 14.201 | −1.071 | 0.237 | 43.357 | 35.385 | 81.538 | 100.0 | 100.0 | 60.0 | 42.517 | 0.453 |

**PSUM 24h** (Rogers / GNP, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p48 (rank 10–90: p33–p56; bias −0.752 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 7% of days. Hex contains 10% of grid cells and spans 0.16× the grid p10–p90 width (hex median bias −8.279 mm).
- **Treeline:** single-point sits at grid p45 (rank 10–90: p36–p49; bias −1.045 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 13% of days. Hex contains 14% of grid cells and spans 0.11× the grid p10–p90 width (hex median bias −3.777 mm).
- **Below treeline:** single-point sits at grid p45 (rank 10–90: p33–p49; bias −0.832 mm vs grid median). Inside grid IQR on 100% of days; inside hex envelope on 67% of days. Hex contains 32% of grid cells and spans 0.30× the grid p10–p90 width (hex median bias −0.703 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 46 | 2 | 15 | 14.502 | −0.752 | −8.279 | 47.826 | 33.043 | 55.652 | 100.0 | 100.0 | 6.667 | 10.000 | 0.161 |
| TL | 40 | 2 | 15 | 10.425 | −1.045 | −3.777 | 45.000 | 36.000 | 49.000 | 100.0 | 100.0 | 13.333 | 14.333 | 0.112 |
| BTL | 126 | 2 | 15 | 8.742 | −0.832 | −0.703 | 45.238 | 33.016 | 49.206 | 100.0 | 100.0 | 66.667 | 32.381 | 0.296 |

**PSUM 24h** (Banff, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p47 (rank 10–90: p26–p52; bias −0.768 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 13% of days. Hex contains 27% of grid cells and spans 0.42× the grid p10–p90 width (hex median bias −3.113 mm).
- **Treeline:** single-point sits at grid p40 (rank 10–90: p15–p58; bias −0.918 mm vs grid median). Inside grid IQR on 80% of days; inside hex envelope on 60% of days. Hex contains 39% of grid cells and spans 0.36× the grid p10–p90 width (hex median bias −1.589 mm).
- **Below treeline:** single-point sits at grid p38 (rank 10–90: p22–p63; bias −0.981 mm vs grid median). Inside grid IQR on 80% of days; inside hex envelope on 73% of days. Hex contains 52% of grid cells and spans 0.47× the grid p10–p90 width (hex median bias −0.664 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 101 | 3 | 15 | 8.664 | −0.768 | −3.113 | 46.535 | 26.139 | 52.277 | 86.667 | 100.0 | 13.333 | 27.327 | 0.424 |
| TL | 89 | 3 | 15 | 7.472 | −0.918 | −1.589 | 40.449 | 14.607 | 58.202 | 80.000 | 100.0 | 60.000 | 38.951 | 0.362 |
| BTL | 247 | 3 | 15 | 5.950 | −0.981 | −0.664 | 37.652 | 22.267 | 63.401 | 80.000 | 100.0 | 73.333 | 52.200 | 0.472 |

**PSUM 24h** (MWHS, 17–31 Dec 2025)

- **Alpine:** single-point sits at grid p47 (rank 10–90: p26–p50; bias −0.741 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 27% of days. Hex contains 27% of grid cells and spans 0.57× the grid p10–p90 width (hex median bias −5.197 mm).
- **Treeline:** single-point sits at grid p39 (rank 10–90: p23–p48; bias −0.993 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 40% of days. Hex contains 27% of grid cells and spans 0.36× the grid p10–p90 width (hex median bias −3.586 mm).
- **Below treeline:** single-point sits at grid p39 (rank 10–90: p26–p49; bias −1.096 mm vs grid median). Inside grid IQR on 87% of days; inside hex envelope on 73% of days. Hex contains 65% of grid cells and spans 0.92× the grid p10–p90 width (hex median bias +0.187 mm).

| band | n_grid | n_hex | n_days | grid_med | sp−grid_med | hex−grid_med | sp_rank_p50 | sp_rank_p10 | sp_rank_p90 | %days SP in IQR | %days SP in p10–p90 | %days SP in hex | hex cover % | hex vs p10–p90 |
|------|--------|-------|--------|----------|-------------|--------------|-------------|-------------|-------------|-----------------|---------------------|-----------------|-------------|----------------|
| ALP | 55 | 3 | 15 | 12.182 | −0.741 | −5.197 | 47.273 | 26.182 | 50.182 | 86.667 | 100.0 | 26.667 | 26.788 | 0.574 |
| TL | 89 | 4 | 15 | 10.215 | −0.993 | −3.586 | 39.326 | 22.697 | 48.315 | 86.667 | 100.0 | 40.000 | 26.891 | 0.365 |
| BTL | 585 | 6 | 15 | 7.845 | −1.096 | 0.187 | 38.803 | 26.427 | 48.752 | 86.667 | 100.0 | 73.333 | 64.615 | 0.924 |

**PSUM 24h — rank / offset / hex coverage**

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_rank_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum-rank" data-type="image" data-title="Whistler · PSUM_24h · rank | offset vs grid mean | hex coverage · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_rank_whistler.png" alt="Whistler PSUM 24h rank offset hex coverage" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_rank_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum-rank" data-type="image" data-title="Rogers / GNP · PSUM_24h · rank | offset vs grid mean | hex coverage · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_rank_rogers.png" alt="Rogers GNP PSUM 24h rank offset hex coverage" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_rank_banff.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum-rank" data-type="image" data-title="Banff · PSUM_24h · rank | offset vs grid mean | hex coverage · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_rank_banff.png" alt="Banff PSUM 24h rank offset hex coverage" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_rank_mwhs.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum-rank" data-type="image" data-title="MWHS · PSUM_24h · rank | offset vs grid mean | hex coverage · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_psum_rank_mwhs.png" alt="MWHS PSUM 24h rank offset hex coverage" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 7.</strong> Detailed period — PSUM 24h daily rank, offset vs grid mean, and hex coverage (17–31 Dec 2025). Click a miniature to maximize.</p>

**PSUM 24h — pooled ECDF**

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_ecdf_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum-ecdf" data-type="image" data-title="Whistler · PSUM_24h · pooled ECDF over 2025-12-17 → 2025-12-31 (cell-days)">
      <img src="../assets/images/paper_config/precip_detail_psum_ecdf_whistler.png" alt="Whistler PSUM 24h pooled ECDF" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_ecdf_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum-ecdf" data-type="image" data-title="Rogers / GNP · PSUM_24h · pooled ECDF over 2025-12-17 → 2025-12-31 (cell-days)">
      <img src="../assets/images/paper_config/precip_detail_psum_ecdf_rogers.png" alt="Rogers GNP PSUM 24h pooled ECDF" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_psum_ecdf_banff.png" class="glightbox image-zoom" data-gallery="status-precip-detail-psum-ecdf" data-type="image" data-title="Banff · PSUM_24h · pooled ECDF over 2025-12-17 → 2025-12-31 (cell-days)">
      <img src="../assets/images/paper_config/precip_detail_psum_ecdf_banff.png" alt="Banff PSUM 24h pooled ECDF" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 8.</strong> Detailed period — PSUM 24h pooled ECDF (grid vs hex vs single-point cell-days), 17–31 Dec 2025. MWHS ECDF not included yet. Click a miniature to maximize.</p>

**HN24**

<div class="pro-evo-grid pro-evo-grid--2x2">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_hn24_whistler.png" class="glightbox image-zoom" data-gallery="status-precip-detail-hn24" data-type="image" data-title="Whistler · HN24 · daily grid violins + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_hn24_whistler.png" alt="Whistler HN24 detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">Whistler</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_hn24_rogers.png" class="glightbox image-zoom" data-gallery="status-precip-detail-hn24" data-type="image" data-title="Rogers / GNP · HN24 · daily grid violins + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_hn24_rogers.png" alt="Rogers GNP HN24 detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">Rogers / GNP</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_hn24_banff.png" class="glightbox image-zoom" data-gallery="status-precip-detail-hn24" data-type="image" data-title="Banff · HN24 · daily grid violins + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_hn24_banff.png" alt="Banff HN24 detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">Banff</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/precip_detail_hn24_mwhs.png" class="glightbox image-zoom" data-gallery="status-precip-detail-hn24" data-type="image" data-title="MWHS · HN24 · daily grid violins + hex beeswarm + median HRDPS · 2025-12-17 → 2025-12-31">
      <img src="../assets/images/paper_config/precip_detail_hn24_mwhs.png" alt="MWHS HN24 detail period violin and hex beeswarm" />
    </a>
    <span class="pro-evo-grid__label">MWHS</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 9.</strong> Detailed period — HN24 daily grid violin + hex beeswarm + median HRDPS (17–31 Dec 2025). Click a miniature to maximize.</p>

#### Interpretation — Dec storm window (17–31 Dec 2025)

**Whistler (maritime)**

This storm is wet: ALP Σμ ≈ 2.2 m of HN24 in two weeks.

- **Alpine.** Hex −4% / −6 mm/day; Config III −3%. Rank ~60, hex brackets μ on 87% of days, r = 0.99. Both reduced configs track the grid.
- **Treeline.** Hex −7%, Config III −6%. Still close.
- **Below treeline.** Hex HN24 −6%; Config III −12%. Hex precip is almost unbiased (−2% PSUM) while Config III precip is −10% — the band-median point is a poorer BTL sampler. Hex coverage drops to 60%.
- This storm does **not** reproduce the season-level BTL hex wet bias (+37%). Here hex is slightly dry. One maritime cyclone is not the winter.

**Rogers / GNP (transitional)**

ALP Σμ is also ~2.2 m — as snowy as Whistler aloft, but the hexes miss it.

- **Alpine.** Hex −52% HN24 (−77 mm/day, snow-day MAE 95 mm), rank 21, brackets μ on 7% of days. PSUM hex −58%, coverage 0%. Two ALP hexes are the dry side of the wet-west / dry-east gradient, and this storm makes that obvious in millimetres. Config III is −7% HN24 and PSUM, rank 50 — a single well-chosen ALP cell beats two badly placed hexes.
- **Treeline.** Hex −31%, Config III −8%. Same pattern, milder.
- **Below treeline.** Hex and Config III both −22% HN24. The band-median point has no valley analogue; the two BTL hexes are not enough either.

**Banff (continental)**

Drier storm: ALP Σμ 1.4 m (about 2/3 of Whistler/Rogers).

- **Alpine.** Hex −38% (−36 mm/day), rank 29, coverage 27%. Config III −11%. PSUM matches HN24, so again it is sampling, not microphysics.
- **Treeline.** Hex −14%, Config III −15% — about the same.
- **Below treeline.** Hex −13% (coverage 60%); Config III −26%. Hex is the better BTL reduced config in this storm; Config III gets worse downslope, as in the season.

**MWHS (continental, snowier)**

ALP Σμ 1.9 m — continental totals, Rogers-like hex errors.

- **Alpine.** Hex −38% (−49 mm/day), rank 23, coverage 20%. Config III −10%.
- **Treeline.** Hex −38%, Config III −12%.
- **Below treeline.** Hex −12% but coverage 93% (six hexes → a wide min–max that contains μ even when the median is dry). Config III −29%. Same split as Banff: hex fails ALP, Config III fails BTL.

##### Comparison across climates

1. **Maritime vs the interior.** Whistler ALP/TL stay within ~7% of the grid. Rogers, Banff, and MWHS ALP hexes lose 38–52% of storm HN24. The reduced-config problem in this window is orographic sampling, not a maritime rain/snow issue.
2. **Config III vs hex at ALP.** Config III is within 7–11% of ALP ΣHN24 in every climate. Hex is only competitive at Whistler. At Rogers the whole hex range sits below μ.
3. **Where each config breaks.** Hex millimetre error is an ALP (and Rogers TL) storm problem. Config III error grows downslope (Whistler BTL −12%, Banff −26%, MWHS −29%, Rogers −22%). That is the band-median vs valley-bottom mismatch.
4. **PSUM vs HN24.** Rogers/Banff/MWHS ALP hex dryness shows up in PSUM at about the same relative size → blame hex placement in the HRDPS field. Whistler BTL is the exception: hex precip is fine, Config III precip is not.
5. **Season vs this storm.** Same climate ranking (Whistler OK; interior ALP hex too dry; Config III too dry at BTL). Magnitudes differ: this is one wet sequence, and Whistler BTL even flips sign vs the winter hex wet bias. Use the season terciles for climate; use this window as the worked storm example.

## 3. AvAPro

<div class="note-box">
<p class="note-box__title">AvAPro analysis</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/docker_fun/docs/notebooks/AvAPro_analysis.ipynb">/Users/machtl/Documents/docker_fun/docs/notebooks/AvAPro_analysis.ipynb</a>
</div>
</div>

Problem prevalence (fraction of profiles) for storm, wind, persistent, deep persistent, and wet — grid vs hex vs median HRDPS, **20–23 Dec 2025 18Z**.

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/avapro_prevalence_all_aspects.png" class="glightbox image-zoom" data-gallery="status-avapro-prevalence" data-type="image" data-title="AvAPro prevalence · grid vs hex vs median HRDPS · all aspects · fraction of profiles · 2025-12-20 → 2025-12-23 18Z">
      <img src="../assets/images/paper_config/avapro_prevalence_all_aspects.png" alt="AvAPro prevalence all aspects grid vs hex vs median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">All aspects</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/avapro_prevalence_flat.png" class="glightbox image-zoom" data-gallery="status-avapro-prevalence" data-type="image" data-title="AvAPro prevalence · grid vs hex vs median HRDPS · flat (F) only · fraction of profiles · 2025-12-20 → 2025-12-23 18Z">
      <img src="../assets/images/paper_config/avapro_prevalence_flat.png" alt="AvAPro prevalence flat aspect grid vs hex vs median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">Flat only</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 10.</strong> AvAPro prevalence — grid vs hex vs median HRDPS by operation and elevation band (20–23 Dec 2025 18Z): all aspects and flat only. Click a miniature to maximize.</p>

#### Interpretation

The bars are the fraction of **profiles** (cell × aspect) that flagged each problem over **20–23 Dec 18Z**. Grid is the spatial truth for that window; hex and Config III (median HRDPS) are small samples of the same domain. Hex bias is **not one-sided** — it over-flags in some climates and under-flags in others.

**How to read Config III.** Each median bar is only ~20 profiles per band (3 stations × 5 aspects × 4 days). It is often 0 or 1, not a spatial prevalence. Treat it as “did the band-median profile fire?” not “how much of the forecast area had the problem.”

**Whistler (maritime).** Full grid has a clear elevation drop: ALP storm / wind / deep persistent ≈ 0.42 / 0.56 / 0.59, TL similar, **BTL much quieter** (0.13 / 0.08 / 0.17). Hex saturates every band (storm ~0.8–0.9, deep persistent **1.0**, any-problem **1.0**), including BTL. Config III matches that over-flag at ALP/TL (all 1.0) and still keeps BTL storm/deep persistent high, though it drops BTL wind to 0 — the one place it agrees with the quiet grid BTL. Hex/Config III look like “the Coast is always a problem”; the grid says that is only true for a subset of ALP/TL cells.

That fits the precip result: Whistler hex BTL was the wet outlier. The hexes sit in the snowy part of the maritime domain, so AvAPro never sees the quiet BTL majority.

**Rogers / GNP (transitional).** Opposite error. Grid ALP is almost always flagged (storm 0.79, wind 0.83, deep persistent 0.91); TL/BTL stay high on deep persistent (~0.8) with less storm/wind. Hex ALP has **storm = 0, wind = 0, deep persistent only 0.45**; hex TL is nearly empty. Config III ALP saturates like the grid (1/1/1); Config III TL is “deep persistent only.” Hex misses the orographic ALP maximum that the full grid (and even the single median ALP profile) still sees — same pattern as hex ALP HN24 ~−60%.

**MWHS (snowy continental).** Same ALP miss as Rogers: grid ALP wind 0.93 and deep persistent 1.0 vs hex ALP **0 / 0 / 0.47**. Config III ALP tracks the grid (0.75 / 1.0 / 1.0). Lower down, hex TL keeps deep persistent (~0.84 vs grid 0.94) but drops wind to 0 (grid 0.55) and invents extra persistent (0.32 vs 0.04). Hex BTL is closer on storm, under on wind and deep persistent, and is the only place **wet** shows up (~0.17). Config III again follows grid ALP and then collapses wind at TL/BTL.

**Banff (continental).** Grid is the quiet domain: ALP any-problem only 0.17; storm ~0.02 everywhere; wind peaks at TL (0.32); deep persistent 0.10–0.22. Hex and Config III **manufacture a windy, persistent Banff**: hex TL wind = 1.0 and persistent ~0.57; hex ALP persistent 0.37 vs grid 0.02; Config III ALP/TL wind = 1.0 and deep persistent 0.50–0.60. Storm stays near 0 on all three — everyone agrees there was little new snow — but the sparse configs turn a mostly-no-problem grid into a persistent/wind-slab forecast.

##### What the three settings actually do

1. **Full grid** keeps the elevation structure: storm and wind decrease ALP → BTL; deep persistent stays high into BTL at Rogers and MWHS, not at Whistler or Banff.
2. **Hex** often **erases that structure**. Whistler hex BTL looks alpine; Rogers/MWHS hex ALP looks empty. With only 2–7 hexes per op, one misplaced ALP hex is enough to flip the bar.
3. **Config III** is not a middle ground. At **ALP** it tracks the **grid** at Rogers/MWHS (saturated) and the **hex** at Whistler/Banff (over-flag). It cannot represent partial coverage: if the median profile fires, the bar is ~1 even when the grid is 0.2.

##### Cross-climate takeaway

Coarsening is not conservatively high or low. Hex/Config III **over-represent** problems in maritime Whistler and dry Banff, and **under-represent** them at ALP in the orographic interiors (Rogers, MWHS). Persistent and wet are rare on the grid in this window; hex Banff persistent and hex MWHS wet are sampling artifacts, not a second problem type the grid missed. For the paper: AvAPro prevalence is sensitive to *where* the reduced grid sits, not just to how many cells you keep.

## 4. QMAH stability comp

<div class="note-box">
<p class="note-box__title">Stability analysis QMAH</p>
<div class="note-box__body">
<a href="file:///Users/machtl/Documents/docker_fun/docs/notebooks/Stability_analysis_QMAH.ipynb">/Users/machtl/Documents/docker_fun/docs/notebooks/Stability_analysis_QMAH.ipynb</a>
</div>
</div>

QMAH GeoJSON, daily **18:00 UTC**, **all aspects**. Whistler window: **20–23 Dec 2025**. Grid violin + hex beeswarm (W2–W6) + median HRDPS (Config III). Slab height is the QMAH critical-layer `depth` (cm); SK38 / Punstable / CCL can pick different layers.

### 4.1 Whistler — SK38, Punstable, CCL

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/qmah_whistler_sk38.png" class="glightbox image-zoom" data-gallery="status-qmah-whistler" data-type="image" data-title="Whistler · SK38 · daily 18Z all aspects · grid violin + hex beeswarm + median HRDPS · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/qmah_whistler_sk38.png" alt="Whistler SK38 grid violin vs hex beeswarm and median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">SK38</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/qmah_whistler_punstable.png" class="glightbox image-zoom" data-gallery="status-qmah-whistler" data-type="image" data-title="Whistler · P unstable · daily 18Z all aspects · grid violin + hex beeswarm + median HRDPS · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/qmah_whistler_punstable.png" alt="Whistler Punstable grid violin vs hex beeswarm and median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">P unstable</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/qmah_whistler_ccl.png" class="glightbox image-zoom" data-gallery="status-qmah-whistler" data-type="image" data-title="Whistler · Critical cut length (m) · daily 18Z all aspects · grid violin + hex beeswarm + median HRDPS · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/qmah_whistler_ccl.png" alt="Whistler CCL grid violin vs hex beeswarm and median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">Critical cut length</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 11.</strong> Whistler QMAH — SK38, Punstable, and critical cut length: daily 18Z grid violins vs hex beeswarm and median HRDPS by elevation band (20–23 Dec 2025, all aspects). Click a miniature to maximize.</p>

### 4.2 Whistler — slab height (critical-layer depth)

<div class="pro-evo-grid">
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/qmah_whistler_sk38_slab.png" class="glightbox image-zoom" data-gallery="status-qmah-whistler-slab" data-type="image" data-title="Whistler · Slab height · SK38 layer (cm) · daily 18Z all aspects · grid violin + hex beeswarm + median HRDPS · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/qmah_whistler_sk38_slab.png" alt="Whistler SK38 slab height grid violin vs hex and median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">SK38 slab</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/qmah_whistler_pu_slab.png" class="glightbox image-zoom" data-gallery="status-qmah-whistler-slab" data-type="image" data-title="Whistler · Slab height · Punstable layer (cm) · daily 18Z all aspects · grid violin + hex beeswarm + median HRDPS · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/qmah_whistler_pu_slab.png" alt="Whistler Punstable slab height grid violin vs hex and median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">Punstable slab</span>
  </div>
  <div class="pro-evo-grid__item">
    <a href="../assets/images/paper_config/qmah_whistler_ccl_slab.png" class="glightbox image-zoom" data-gallery="status-qmah-whistler-slab" data-type="image" data-title="Whistler · Slab height · CCL layer (cm) · daily 18Z all aspects · grid violin + hex beeswarm + median HRDPS · 2025-12-20 → 2025-12-23">
      <img src="../assets/images/paper_config/qmah_whistler_ccl_slab.png" alt="Whistler CCL slab height grid violin vs hex and median HRDPS" />
    </a>
    <span class="pro-evo-grid__label">CCL slab</span>
  </div>
</div>

<p class="fig-caption"><strong>Figure 12.</strong> Whistler QMAH — slab height (critical-layer depth, cm) for the SK38, Punstable, and CCL layers: daily 18Z grid violins vs hex beeswarm and median HRDPS by elevation band (20–23 Dec 2025, all aspects). Click a miniature to maximize.</p>

