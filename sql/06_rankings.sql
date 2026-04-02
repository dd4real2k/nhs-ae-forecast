-- NHS A&E Performance Analysis
-- File: 06_rankings.sql
-- Description:
-- Pressure banding and organisation ranking using SQL window functions

SELECT
    org_name,
    total_attendances,
    total_over_4hrs,
    ROUND(over_4hr_rate * 100, 2) AS over_4hr_rate_pct,
    CASE
        WHEN over_4hr_rate >= 0.50 THEN 'Critical Pressure'
        WHEN over_4hr_rate >= 0.30 THEN 'High Pressure'
        WHEN over_4hr_rate >= 0.15 THEN 'Moderate Pressure'
        ELSE 'Lower Pressure'
    END AS pressure_band
FROM nhs_ae_waiting_times
WHERE total_attendances >= 1000
ORDER BY over_4hr_rate DESC;

SELECT
    org_name,
    parent_org,
    total_attendances,
    RANK() OVER (ORDER BY total_attendances DESC) AS attendance_rank
FROM nhs_ae_waiting_times
ORDER BY attendance_rank;

SELECT
    org_name,
    parent_org,
    patients_who_have_waited_12plus_hrs_from_dta_to_admission AS waits_12plus,
    RANK() OVER (
        ORDER BY patients_who_have_waited_12plus_hrs_from_dta_to_admission DESC
    ) AS wait_rank
FROM nhs_ae_waiting_times
ORDER BY wait_rank;
