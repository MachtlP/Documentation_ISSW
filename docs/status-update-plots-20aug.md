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

<details class="table-dropdown">
<summary><strong>Whistler</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 178 | 225 | 25 | −28.577 | −4.747 | 25.526 | 2.993 | −0.279 | 0.036 | 56.464 | 60.733 | 85.955 | 17397.857 | 16552.890 | 17930.57 | −0.049 | 0.031 |
| TL | 173 | 165 | 25 | −21.164 | −1.713 | 22.763 | −1.610 | −0.095 | −0.090 | 60.266 | 56.805 | 85.549 | 17016.298 | 16720.015 | 16737.85 | −0.017 | −0.016 |
| BTL | 168 | 145 | 20 | 5.107 | 26.613 | 48.791 | 2.959 | 0.846 | −0.059 | 79.620 | 64.100 | 54.762 | 12161.496 | 16632.450 | 12658.55 | 0.368 | 0.041 |

</details>

<details class="table-dropdown">
<summary><strong>Rogers / GNP</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 184 | 230 | 10 | −65.428 | −55.613 | −45.798 | −6.358 | −0.679 | −0.076 | 26.846 | 50.556 | 7.609 | 17094.181 | 6861.455 | 15924.28 | −0.599 | −0.068 |
| TL | 177 | 200 | 10 | −49.821 | −41.124 | −32.426 | −8.555 | −0.666 | −0.169 | 37.062 | 51.356 | 15.254 | 11987.502 | 4708.595 | 10473.25 | −0.607 | −0.126 |
| BTL | 172 | 380 | 10 | −17.301 | −5.533 | 6.235 | −20.461 | 0.288 | −0.449 | 57.421 | 47.945 | 47.674 | 10775.933 | 9824.230 | 7256.59 | −0.088 | −0.327 |

</details>

<details class="table-dropdown">
<summary><strong>Banff</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 185 | 480 | 15 | −39.357 | −26.544 | −5.751 | −8.008 | −0.658 | −0.234 | 45.087 | 53.493 | 32.973 | 10399.734 | 5489.12 | 8918.34 | −0.472 | −0.142 |
| TL | 170 | 391 | 15 | −22.391 | −12.647 | 6.144 | −10.821 | −0.434 | −0.372 | 55.298 | 53.723 | 53.529 | 8650.472 | 6500.55 | 6810.86 | −0.249 | −0.213 |
| BTL | 159 | 870 | 15 | −24.545 | −5.737 | 17.539 | −16.552 | −0.159 | −0.564 | 60.244 | 50.043 | 63.522 | 7038.274 | 6126.04 | 4406.55 | −0.130 | −0.374 |

</details>

<details class="table-dropdown">
<summary><strong>MWHS</strong> — click to expand</summary>

| band | n_days | n_grid | n_hex | mean_off_hex_min | mean_off_hex_med | mean_off_hex_max | mean_off_sp | mean_rel_hex_med | mean_rel_sp | mean_rank_hex_med | mean_rank_sp | %days hex covers μ | Σ grid mean mm | Σ hex med mm | Σ SP mm | season_rel_hex_med | season_rel_sp |
|------|--------|--------|-------|------------------|------------------|------------------|-------------|---------------|-------------|-------------|--------------|--------------------|----------------|--------------|---------|--------------------|---------------|
| ALP | 191 | 270 | 15 | −81.206 | −54.393 | −28.004 | −9.410 | −0.731 | −0.226 | 23.425 | 46.033 | 17.277 | 17920.364 | 7531.270 | 16122.96 | −0.580 | −0.100 |
| TL | 192 | 445 | 20 | −53.278 | −41.827 | −25.428 | −12.554 | −0.671 | −0.305 | 33.316 | 48.408 | 17.708 | 14918.136 | 6887.320 | 12507.75 | −0.538 | −0.162 |
| BTL | 187 | 1490 | 30 | −45.586 | −16.262 | 47.405 | −23.643 | −0.455 | −0.590 | 52.192 | 46.059 | 86.096 | 12061.894 | 9020.965 | 7640.65 | −0.252 | −0.367 |

</details>

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

### 2.3 Detail period

Candidate window **17–31 Dec 2025**: daily 00:00 grid violin + hex beeswarm + median HRDPS (PSUM 24h).

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

<p class="fig-caption"><strong>Figure 5.</strong> Detail period — PSUM 24h daily grid violin + hex beeswarm + median HRDPS (17–31 Dec 2025). Click a miniature to maximize.</p>

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
