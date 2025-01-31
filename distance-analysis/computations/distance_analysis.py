import pandas as pd
import geopy.distance as gd

df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv')

df.dropna(inplace=True)

df['distance_km'] = df.apply(lambda row: gd.geodesic((row['start_lat'], row['start_lng']), (row['end_lat'], row['end_lng'])).km, axis=1)
df.head()

average_distance = df['distance_km'].mean()

print(f"The average distance per ride is {average_distance:.2f} km.")