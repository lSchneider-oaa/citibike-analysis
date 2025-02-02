import pandas as pd
import geopy.distance as gd
import swifter
import time

start_time_total = time.time()

# Load data
start_time = time.time()
df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv', low_memory=False)
print(f"CSV read time: {time.time() - start_time:.2f} seconds")

# Drop rows with missing latitude/longitude
df = df.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])

# Use swifter to apply the geodesic calculation in parallel
start_time = time.time()
df['distance_km'] = df.swifter.apply(
    lambda row: gd.geodesic((row['start_lat'], row['start_lng']), (row['end_lat'], row['end_lng'])).km,
    axis=1
)
print(f"Distance calculation time: {time.time() - start_time:.2f} seconds")

# Compute average distance
start_time = time.time()
average_distance = df['distance_km'].mean()
print(f"Average distance calculation time: {time.time() - start_time:.2f} seconds")

print(f"The average distance per ride is {average_distance:.2f} km.")

total_time = time.time() - start_time_total
print(f"Total computation time: {total_time:.2f} seconds")