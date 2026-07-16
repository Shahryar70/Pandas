#A Data Warehouse is a central repository of structured, cleaned, integrated data — designed 
# specifically for analytics queries (GROUP BY, JOINs, aggregations), not for day-to-day 
# transaction processing. Data is organised into facts and dimensions.
#OLTP Sources → ETL/ELT → Data Warehouse → BI / Reports
# Create Table fact_appointments (
#  appointment_id Int,
#  patient_key int,   -- FK → dim_patients
#  doctor_key int,    -- FK → dim_doctors
#  date_key int,       -- FK → dim_date
#  bill_ammount Decimal(10,2),
#  stay_days int
# )
# CREATE TABLE dim_patients (
#     patient_key  INT PRIMARY KEY,
#     name         VARCHAR(100),
#     age_group    VARCHAR(20),  -- 'Adult', 'Senior'
#     disease      VARCHAR(100),
#     risk_level   VARCHAR(20)   -- 'High', 'Medium', 'Low'
# );
# select risk_level, Avg(bill_Amount)
# from fact_appointment as f
# left join dim_patients p On f.patient_key = p.patient_key
# Group by risk_level