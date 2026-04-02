-- NHS A&E Performance Analysis
-- File: 01_national_summary.sql
-- Description:
-- National-level summary of NHS A&E activity and pressure

SELECT COUNT(*) AS row_count
FROM nhs_ae_waiting_times;

SELECT
    SUM(total_attendances) AS national_total_attendances,
    SUM(total_booked_attendances) AS national_total_booked_attendances,
    SUM(total_over_4hrs) AS national_total_over_4hrs,
    SUM(total_emergency_admissions) AS national_total_emergency_admissions
FROM nhs_ae_waiting_times;
