import os
import pandas as pd

file_path = "C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata"

file_list = os.listdir(file_path)

df_concat = pd.concat([pd.read_csv("C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata/" + f) for f in file_list ], ignore_index=True)

df_concat.to_csv("C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv", index=False)