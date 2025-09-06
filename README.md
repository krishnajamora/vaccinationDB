
Vaccination Data Analysis and Visualization Project
-------------------------------------------------
How to Use:
Step 1) Place your CSV files into ./data/ directory. Name them as:
 coverage.csv, incidence.csv, cases.csv, vaccine_intro.csv, vaccine_schedule.csv

Step 2) Run scripts/1_data_cleaning.py to clean all data
Step 3) Run scripts/3_upload_to_sql.py to upload cleaned data to ./data/vaccination.db
Step 4) Open Power BI Desktop. Connect to ./data/vaccination.db or import CSVs
Step 5) Use the sample SQL queries (scripts/4_eda_queries.sql) for insights, or build interactive dashboards per instructions in powerbi/instructions.txt

Stack:
- Python (Pandas, Numpy)
- SQLite (for testing; adapt connection for MySQL/Postgres if needed)
- Power BI

Notes:
- Edit script paths for new database locations or custom CSV names.
- Provided SQL can be adapted for any RDBMS.
