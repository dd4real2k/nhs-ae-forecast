-- NHS A&E Performance Analysis - February 2026
-- Author: Daniel Diala
-- Description:
-- This SQL file contains portfolio analysis queries for exploring
-- NHS A&E demand, waiting-time pressure, admissions, and regional performance
-- using the nhs_ae_waiting_times table.


-- 1. Check total number of rows in the dataset
SELECT COUNT(*) AS row_count
FROM nhs_ae_waiting_times;


-- 2. National summary totals
-- Shows the overall scale of attendances, booked attendances,
-- long waits, and emergency admissions across all organisations
SELECT
    SUM(total_attendances) AS national_total_attendances,
    SUM(total_booked_attendances) AS national_total_booked_attendances,
    SUM(total_over_4hrs) AS national_total_over_4hrs,
    SUM(total_emergency_admissions) AS national_total_emergency_admissions
FROM nhs_ae_waiting_times;


-- 3. Top 10 organisations by total A&E attendances
-- Identifies the busiest organisations by patient demand
SELECT
    org_name,
    parent_org,
    total_attendances
FROM nhs_ae_waiting_times
ORDER BY total_attendances DESC
LIMIT 10;


-- 4. Top 10 organisations by number of over-4-hour waits
-- Highlights organisations with the highest absolute waiting-time pressure
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


-- 5. Worst over-4-hour performance rate
-- Restricting to organisations with at least 1,000 attendances
-- avoids very small sites distorting the ranking
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


-- 6. Top 10 organisations by 12+ hour DTA waits
-- Focuses on the longest reported delays from decision to admit to admission
SELECT
    org_name,
    parent_org,
    patients_who_have_waited_12plus_hrs_from_dta_to_admission AS waits_12plus
FROM nhs_ae_waiting_times
ORDER BY waits_12plus DESC
LIMIT 10;


-- 7. Regional summary of attendances, waits, and admissions
-- Compares parent organisations/regions by activity and over-4-hour performance
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


-- 8. Pressure band classification
-- Uses CASE WHEN to group organisations into pressure categories
-- based on their over-4-hour wait rate
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


-- 9. Rank organisations by total attendances
-- Demonstrates use of a SQL window function for ranking
SELECT
    org_name,
    parent_org,
    total_attendances,
    RANK() OVER (ORDER BY total_attendances DESC) AS attendance_rank
FROM nhs_ae_waiting_times
ORDER BY attendance_rank;


-- 10. Rank organisations by 12+ hour waits
-- Another window-function example focused on the longest delays
SELECT
    org_name,
    parent_org,
    patients_who_have_waited_12plus_hrs_from_dta_to_admission AS waits_12plus,
    RANK() OVER (
        ORDER BY patients_who_have_waited_12plus_hrs_from_dta_to_admission DESC
    ) AS wait_rank
FROM nhs_ae_waiting_times
ORDER BY wait_rank;
