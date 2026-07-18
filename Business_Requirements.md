# Business Requirements Document (BRD)
**Company:** Apex Regional Deliveries  
**Project:** Fleet Health & Routing Analytics Pipeline  
**Stakeholders:** VP of Finance, Dispatch Operations Manager

## 1. Executive Summary
Apex Regional Deliveries has been experiencing operational inefficacies and budget discrepancies due to poor visibility into daily fleet logistics, driver performance, and fuel consumption reporting. Executive stakeholders suspected that severe data quality issues and unmonitored driver behaviors were creating hidden bottlenecks, but dispatchers lacked the analytical tools to prove it.

To resolve this, a robust, end-to-end data pipeline and interactive Business Intelligence (BI) solution were developed. This project successfully extracted, cleansed, and modeled over 10,000 logistical records, transforming highly erroneous raw data into reliable, single source of truth.

The resulting Fleet Health & Routing Operations Dashboard empowers the VP of Finance and Dispatch Managers to immediately isolate mathematically impossible fuel entries, identify underperforming routing times, and proactively enforce vehicle maintenance compliance. By transitioning from reactive guesswork to a proactive, data-driven strategy. APEX is now positioned to significantly reduce fuel waste, optimize driver training, and mitigate DOT regulatory risks.


## 2. Problem Statement
APEX Regional Deliveries lacks centralized visibility into its daily fleet operations. Dispatchers are relying on fragmented, manual reporting to track route times, while the VP of Finance has noted severe discrepancies between projected fuel budgets and actual fuel consumption. Furthermore, the is no automated system to track vehicle maintenance, leading to vehicles operating with missing or overdue logs.

Without a reliable "Single Source of Truth", management is forced to rely on reactive guesswork. This lack of data governance is resulting in three major business risks:
  * **Financial Waste:** Unchecked fuel anomalies (e.g., negative entries or mathematically impossible MPG rates) are draining the operating budget.
  * **Operational Inefficiency:** Dispatchers cannot easily identify or retain drivers who consistently underperform on route times.
  * **Regulatory Risk:** Vehicles operating with overdue maintenance logs expose the company to potential DOT fines and safety liabilities.

APEX requires an end-to-end automated data pipeline that cleanses raw, erroneous logistics data and serves it into an interactive, executive-facing Business Intelligence dashboard. This solution must provide automated exception reporting for fuel anomalies, driver efficiency, and fleet compliance.


## 3. Project Objectives
* Generate a simulated environment of logistics data to mimic a production database.
* Build a robust ETL pipeline to cleanse mathematically impossible records (e.g., negative fuel entries).
* Deliver a self-serve BI tool for exception reporting.

## 4. Scope & Metrics
**Key Performance Indicators (KPIs) Defined:**
* **Avg Delivery Time:** Time elapsed between dispatch and completion.
* **Fuel Anomalies:** Count of records where fuel usage exceeds tank capacity or falls below 0.
* **Compliance Status:** Real-time tracking of DOT maintenance logs.
