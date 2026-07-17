# 🚚 Apex Fleet Health & Routing Operations: End-to-End Data Pipeline

![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Project Overview
**Apex Regional Deliveries** is a fictional logistics company facing operational bottlenecks. Dispatchers were struggling to identify underperforming drivers, and the VP of FFinance suspected major data quality issues regarding reported fuel consumption and vehicle maintenance.

This Project is an **End to End Data Analysis and BI Pipeline** designed to solve these business problems/ I built a custom ETL workflow that generates raw logistics data, cleanses and models it in a relational database, and serves it to an interactive , executive-ready Power BI dashboard.

*(Insert your GIF or Screenshot of your dashboard here!)*

---

## Architecure & Tech Stack

This project follows a modern ETL/ELT workflow:

1. **Data Generation (Python):** - Utilized `Faker` and `pandas` to genrate over 10,000 rows of realistic logistics data across three tables: `Drivers`, `Vehicles`, and `Delivery Routes`.
   - *Data Quality Engineering:* Intentionally injected real-world anomalies (e.g., nagative fuel entries, missing maintenance logs, and mathematically impossible MPG rates) to simulate a messy production enviroment.
2. **Data Managemnet (PostgreSQL & DBeaver):** - Loaded the raw CSVs into a structured PostgreSQL database using custom schemas (`apex-fleet-data-pipeline`).
3. **Data Transformation (SQL):** - Wrote advanced SQL scripts utilizing Common Table Expressions (CTEs), `EXTRACT(EPOCH)`, `COALESCE`, and `CASE` statements to clean the data.
   - Created optimized, analytical `VIEWS` that flagged anomalies natively in the database before passing them in the BI layer.
4. **Data Visualization (Power BI):** - Designed a Star Schema data model.
   - Created custom DAX measures for informative KPIs.
   - Built an interactive, UI/UX-optimized featuring custom Tile Slicers and Exception Reporting matixes.

---

## Key Insights & Dashboard Feartures
- **Self Serve Anomaly Detection:** Built an interactive scatter plot with a custom Tile Slicer, allovwing the VP of Finance to isntantly filter out valid trips and auto-zoom into mathematically impossible fuel recors (e.g., negative gallons or 5,000+ gallon outliers).
- **Driver Exception Reporting:** Developed a conditional formatting matrix that automatically highlights drivers averaging over 265 minutes per route in read, while rewarding highly efficient drivers in blue.
- **Fleet Health Tracking:** Identified critical fleet risks by isolating vehicles currently operating with "Missing Logs" or "Overdue" maintenance status.

---

## Repository Structure
## 📁 Repository Structure
```text
Apex-Fleet-Data-Pipeline/
│
├── Power_BI/
│   ├── Fleet_Health_Dashboard.Report/       # PBIP Report definition
│   ├── Fleet_Health_Dashboard.SemanticModel/# PBIP Data model
│   ├── Fleet_Health_Dashboard.pbip          # Power BI Project file
│   └── Fleet_Health_Dashboard.pbix          # Standard Power BI file
│
├── data/
│   ├── delivery_routes_raw.csv              # Generated routes dataset
│   ├── drivers_raw.csv                      # Generated drivers dataset
│   └── vehicles_raw.csv                     # Generated vehicles dataset
│
├── py_scripts/
│   ├── 01_data_generator.ipynb              # Jupyter Notebook for exploration
│   └── 01_data_generator.py                 # Executable Python script
│
├── sql_scripts/
│   ├── 02_create_raw_tables.sql             # DDL for Postgres tables
│   └── 03_clean_and_transform.sql           # CTEs and Views for cleaning
│
└── README.md
