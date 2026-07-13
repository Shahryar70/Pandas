#head() tail()
#head() if n not passed will display 5 row
#tail(n) if n not passed will display last 5 row

import pandas as pd
df = pd.read_json("sample_Data.json")
print("Display first 10 rows")
print(df.head())
print("Display last 10 rows")
print(df.tail())