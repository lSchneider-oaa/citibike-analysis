import pandas as pd

def nans(df): return df[df.isnull().any(axis=1)]

df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata/202412-citibike-tripdata_1.csv')
print(nans(df).to_string())