# what is data set size
# what are the colum name

#we use shape and columns for that

import pandas as pd
data = {
    "Name":['Shahryar','Muneeb','Ali','Hamza','Haseeb','Abdullah','Hassan','Shari'],
    "Age": [23,44,35,26,22,30,40,38],
    "Salary":[50000,40000,42300,90000,80000,60000,35000,70000],
    "PerformanceScore":[80,90,70,60,50,60,85,68]
} 
df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'columns: {df.columns }')