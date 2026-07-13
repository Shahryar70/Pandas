import pandas as pd
data = {
    "Name":['Shahryar','Muneeb','Ali','Hamza','Haseeb','Abdullah','Hassan','Shari'],
    "Age": [23,44,35,26,22,30,40,38],
    "Salary":[50000,40000,42300,90000,80000,60000,35000,70000],
    "PerformanceScore":[80,90,70,60,50,60,85,68]
} 
df = pd.DataFrame(data)
#select column
name = df['Name']
print(name)
subset = df[['Name', 'Salary']]
print('\nSubset of Name and Salary')
print(subset)
#fiter rows
high_salary = df[df['Salary'] > 50000]
print("\n Person who has more than 50 thousand salary are")
print(high_salary)

Filter_Salry_Age = df[(df['Age']> 30 ) & (df['Salary'] > 50000)]
print("\n Salary of those higher than 50k and age above 30")
print(Filter_Salry_Age)

Filter_OR = df[(df['Age']> 35) | (df['PerformanceScore']> 80 )]
print("\n those whose age is more than 35 or performance score is more than 80")
print(Filter_OR)