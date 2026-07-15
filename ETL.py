#ETL extracts raw data from sources, transforms it (cleans, reshapes, enriches) in a 
# staging area, then loads the clean result into the destination. Transformation happens 
# BEFORE loading — so the warehouse always contains clean, ready-to-query data.
# Hospital ETL in Python (panadas)
import pandas as pd

df = pd.read_sql('Select * From Patients',conn)
# Tranform clean before loading 
df= df.drop_duplicates()
df["Disease"] = df["Disease"].str.title()
df["BillAmount"] = df["BillAmount"].fillna(df["BillAmount"].mean())
df["RiskLevel"]= df["BillAmount"]({
    "Heart Disease":'High',
    "Diabetic": 'Medium',
    "Flu": 'Low'
})
