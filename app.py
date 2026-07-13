import pandas as pd
# read data with excel , csv and json
# df = pd.read_csv("SampleSuperstore-Orders.csv",encoding="latin1")
# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")
print(df)

#gcsfs: to read data from cloud 