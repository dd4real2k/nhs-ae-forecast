-- NHS A&E Performance Analysis
-- File: 04_long_waits.sql
-- Description:
-- Focuses on organisations with the highest 12+ hour waits from decision to admit

SELECT
    org_name,
    parent_org,
    patients_who_have_waited_12plus_hrs_from_dta_to_admission AS waits_12plus
FROM nhs_ae_waiting_times
ORDER BY waits_12plus DESC
LIMIT 10;
