# Sales & Revenue Performance Dashboard

## Business Problem
Retail/e-commerce businesses often have sales data sitting unused in spreadsheets, with no way for non-technical stakeholders to explore performance without requesting a custom report each time. This project analyzes sales performance and delivers a live, interactive dashboard so a business owner can explore revenue, profit, and regional trends themselves.

## Live Dashboard
🔗 [View Live Dashboard](https://huzi-sales-dashboard.streamlit.app/)

## Dataset
[Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) — 9,994 retail orders (2014-2017), including sales, profit, discount, category, and region data.

## Key Findings
- **18.7% of all orders are unprofitable** (1,871 of 9,994), with losses as steep as -$6,600 on a single order.
- **Tables and Bookcases lose money overall** (-$17,725 and -$3,473 respectively), dragging down Furniture's category profit despite strong sales — a pattern hidden at the category level and only visible in sub-category analysis.
- **Discounts above ~40% are strongly associated with unprofitable orders**; correlation between discount and profit is -0.22, more pronounced at high discount levels.
- **Clear seasonal pattern**: sales spike every November-December, with steady year-over-year growth from 2014 to 2017.
- **West region leads** in both sales ($725K) and profit ($108K); Central lags in profit efficiency despite solid sales volume.

## Recommendation
Reassess pricing/discount strategy for Tables specifically, and investigate whether Central region's lower profit efficiency stems from higher discounting, shipping costs, or product mix.

## Tech Stack
Python, Pandas, Plotly, Streamlit, Google Colab (analysis) → Streamlit Community Cloud (deployment)

## Repo Structure
- `notebook/` — full analysis (cleaning, EDA, visualizations)
- `app.py` — Streamlit dashboard code
- `superstore_clean.csv` — cleaned dataset used by the dashboard
