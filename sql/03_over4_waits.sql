-- NHS A&E Performance Analysis
-- File: 03_over4_waits.sql
-- Description:
-- Highlights organisations with the highest over-4-hour wait pressure

SELECT
    org_name,
    parent_org,
    total_attendances,
    total_over_4hrs,
    ROUND(over_4hr_rate * 100, 2) AS over_4hr_rate_pct
FROM nhs_ae_waiting_times
WHERE total_attendances > 0
ORDER BY total_over_4hrs DESC
LIMIT 10;

SELECT
    org_name,
    parent_org,
    total_attendances,
    total_over_4hrs,
    ROUND(over_4hr_rate * 100, 2) AS over_4hr_rate_pct
FROM nhs_ae_waiting_times
WHERE total_attendances >= 1000
ORDER BY over_4hr_rate DESC
LIMIT 10;
