# AutoChart Builder

## Overview
AutoChart Builder is a simple Python tool that allows users to upload a CSV, select columns, and automatically generate charts and basic summary statistics. It’s designed to be **quick, interactive, and beginner-friendly** while still demonstrating Python, pandas, and matplotlib skills.

---

## Features
- Interactive CSV upload
- Choose X and Y columns for charting
- Supports line, bar, and scatter charts
- Saves charts and summary CSVs in a `reports/` folder
- Beginner-friendly, portable to Termux (Android)

---

## Folder Structure
auto-chart-builder/
- chart_builder.py
- generate_data.py # sample data
- requirements.txt
- README.md
- data/
  - user_data.csv
- reports/
- <generated charts and summaries>


---

## How to Use

### 1. Install dependencies
```bash
- pip install -r requirements.txt

### 2. Generate sample data (optional)
- python generate_data.py

### 3. Build charts from your CSV
- python chart_builder.py
  - Enter the path to your CSV (e.g., data/user_data.csv)
  - Choose columns for X and Y axes
  - Select chart type (line, bar, scatter)
  - Charts and summary statistics will be saved in the reports/ folder.

## Future Upgrades
- Add multiple Y columns for combined charts

- Generate interactive charts (Plotly)

- Allow batch CSV uploads

- Share charts via temporary URLs or GitHub Pages

- Build a mini web dashboard (Flask / Streamlit)

