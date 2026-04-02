-- NHS A&E Performance Analysis
-- File: 02_top_attendance_orgs.sql
-- Description:
-- Identifies the busiest organisations by A&E demand

SELECT
    org_name,
    parent_org,
    total_attendances
FROM nhs_ae_waiting_times
ORDER BY total_attendances DESC
LIMIT 10;
