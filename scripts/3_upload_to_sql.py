
import pandas as pd
import sqlite3
import os

data_folder = '../data/'
conn = sqlite3.connect('../data/vaccination.db')

coverage = pd.read_csv(os.path.join(data_folder, 'coverage_clean.csv'))
coverage.to_sql('coverage_data', conn, if_exists='replace', index=False)

incidence = pd.read_csv(os.path.join(data_folder, 'incidence_clean.csv'))
incidence.to_sql('incidence_data', conn, if_exists='replace', index=False)

cases = pd.read_csv(os.path.join(data_folder, 'cases_clean.csv'))
cases.to_sql('reported_cases', conn, if_exists='replace', index=False)

intro = pd.read_csv(os.path.join(data_folder, 'vaccine_intro_clean.csv'))
intro.to_sql('vaccine_intro', conn, if_exists='replace', index=False)

schedule = pd.read_csv(os.path.join(data_folder, 'vaccine_schedule_clean.csv'))
schedule.to_sql('vaccine_schedule', conn, if_exists='replace', index=False)

conn.close()
