-- NHS A&E Performance Analysis
-- File: 05_regional_summary.sql
-- Description:
-- Regional/parent organisation comparison of attendances, waits, and admissions

SELECT
    parent_org,
    SUM(total_attendances) AS total_attendances,
    SUM(total_over_4hrs) AS total_over_4hrs,
    SUM(total_emergency_admissions) AS total_emergency_admissions,
    ROUND(
        CAST(SUM(total_over_4hrs) AS FLOAT) / NULLIF(SUM(total_attendances), 0) * 100,
        2
    ) AS over_4hr_rate_pct
FROM nhs_ae_waiting_times
GROUP BY parent_org
ORDER BY total_attendances DESC;
