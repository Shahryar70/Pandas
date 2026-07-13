import pandas as pd

data = {
    "Name":['Shahryar','Ali','Ryan'],
    "Age": [10,20,30],
    "City":['Rawalpindi','Lahore','Islamabad']
}
# df = pd.read_csv("SampleSuperstore-Orders.csv",encoding="latin1")
df = pd.DataFrame(data)
print("Display the info of data set")
print(df.info())