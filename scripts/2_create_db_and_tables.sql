
-- Vaccination SQL Table Creation
CREATE TABLE IF NOT EXISTS coverage_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT,
    country_name TEXT,
    year INTEGER,
    antigen TEXT,
    antigen_description TEXT,
    coverage_category TEXT,
    coverage_category_description TEXT,
    target_number INTEGER,
    doses INTEGER,
    coverage_percent REAL
);

CREATE TABLE IF NOT EXISTS incidence_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT,
    country_name TEXT,
    year INTEGER,
    disease TEXT,
    disease_description TEXT,
    denominator TEXT,
    incidence_rate REAL
);

CREATE TABLE IF NOT EXISTS reported_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT,
    country_name TEXT,
    year INTEGER,
    disease TEXT,
    disease_description TEXT,
    cases INTEGER
);

CREATE TABLE IF NOT EXISTS vaccine_intro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT,
    country_name TEXT,
    who_region TEXT,
    year INTEGER,
    vaccine_desc TEXT,
    intro TEXT
);

CREATE TABLE IF NOT EXISTS vaccine_schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT,
    country_name TEXT,
    who_region TEXT,
    year INTEGER,
    vaccine_code TEXT,
    vaccine_description TEXT,
    schedule_rounds INTEGER,
    target_pop TEXT,
    target_pop_desc TEXT,
    geoarea TEXT,
    age_administered TEXT,
    source_comment TEXT
);
