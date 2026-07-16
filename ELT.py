#ELT loads raw data into the destination FIRST, then transforms it there using the destination's
#  own compute power. Made practical by cloud warehouses (BigQuery, Snowflake, Redshift) that are 
# powerful enough to transform at scale.

# --Step 1: Raw Table(as is from source)
#Create Table raw.patients as 
#Select * From source.patients; --load everything

# --Step 2: Transform inside warehouse
# Create Table marts.patients As
# Select 
#  patient_id,
# InitCap(name) as name,
# Coalesce(bill,Avg(bill), Over()) As bill,
# case disease
# When 'Heart Disease' then 'High
# When 'Diabetes' then 'Medium'
# Else 'Low'
# End as risk_level
# From raw.patients