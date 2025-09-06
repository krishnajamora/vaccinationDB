
-- Correlation between vaccination rates and disease incidence
SELECT c.country_name, c.year, c.coverage_percent, i.incidence_rate 
FROM coverage_data c
JOIN incidence_data i ON c.country_code=i.country_code AND c.year=i.year
WHERE c.coverage_percent IS NOT NULL AND i.incidence_rate IS NOT NULL;

-- Drop-off rate between doses
SELECT country_name, antigen, MIN(coverage_percent) as min_coverage, MAX(coverage_percent) as max_coverage 
FROM coverage_data GROUP BY country_name, antigen;

-- Gender difference, education impact, urban/rural difference, seasonal pattern, density
-- Dummy queries; actual data granularity needed.

-- Regions with high incidence despite high vaccination rates
SELECT c.country_name, c.year, c.coverage_percent, i.incidence_rate 
FROM coverage_data c 
JOIN incidence_data i ON c.country_code=i.country_code AND c.year=i.year
WHERE c.coverage_percent>90 AND i.incidence_rate>avg(i.incidence_rate);

-- Booster dose uptake over time
SELECT country_name, year, antigen, coverage_percent FROM coverage_data WHERE antigen LIKE '%booster%';

-- Gaps in coverage for high-priority diseases (TB, HepB, etc.)
SELECT country_name, antigen, coverage_percent FROM coverage_data WHERE antigen IN ('TB', 'HepB') ORDER BY coverage_percent ASC;
