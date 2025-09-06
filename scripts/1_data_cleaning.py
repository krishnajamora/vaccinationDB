
import pandas as pd
import numpy as np
import os

data_folder = '../data/'

def clean_coverage(filename):
    df = pd.read_csv(os.path.join(data_folder, filename))
    df = df.dropna(subset=['Coverage'])  # Remove incomplete coverage
    df['Coverage'] = pd.to_numeric(df['Coverage'], errors='coerce')
    df['Year'] = pd.to_datetime(df['Year'], errors='coerce').dt.year
    df = df.drop_duplicates()
    df.to_csv(os.path.join(data_folder, 'coverage_clean.csv'), index=False)
    return df

def clean_incidence(filename):
    df = pd.read_csv(os.path.join(data_folder, filename))
    df = df.dropna(subset=['Incidence rate'])
    df['Incidence rate'] = pd.to_numeric(df['Incidence rate'], errors='coerce')
    df['Year'] = pd.to_datetime(df['Year'], errors='coerce').dt.year
    df = df.drop_duplicates()
    df.to_csv(os.path.join(data_folder, 'incidence_clean.csv'), index=False)
    return df

def clean_cases(filename):
    df = pd.read_csv(os.path.join(data_folder, filename))
    df = df.dropna(subset=['Cases'])
    df['Cases'] = pd.to_numeric(df['Cases'], errors='coerce')
    df['Year'] = pd.to_datetime(df['Year'], errors='coerce').dt.year
    df = df.drop_duplicates()
    df.to_csv(os.path.join(data_folder, 'cases_clean.csv'), index=False)
    return df

def clean_vaccine_intro(filename):
    df = pd.read_csv(os.path.join(data_folder, filename))
    df = df.drop_duplicates()
    df['Year'] = pd.to_datetime(df['Year'], errors='coerce').dt.year
    df.to_csv(os.path.join(data_folder, 'vaccine_intro_clean.csv'), index=False)
    return df

def clean_vaccine_schedule(filename):
    df = pd.read_csv(os.path.join(data_folder, filename))
    df = df.drop_duplicates()
    df['Year'] = pd.to_datetime(df['Year'], errors='coerce').dt.year
    df.to_csv(os.path.join(data_folder, 'vaccine_schedule_clean.csv'), index=False)
    return df

# Example execution
# clean_coverage('coverage.csv')
# clean_incidence('incidence.csv')
# clean_cases('cases.csv')
# clean_vaccine_intro('vaccine_intro.csv')
# clean_vaccine_schedule('vaccine_schedule.csv')
