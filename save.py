import pandas as pd
data = {
    "Name": ['Shahryar','Hamza','Ryan'],
    "Age": [10,20,30],
    "City": ['Rawalpidni','Lahore','Islamabad']

}
df = pd.DataFrame(data)
print(df)

# save file in csv, excel and json
# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json",index= False)