import numpy as np
import pandas as pd
import time

start_time_total = time.time()

# Define vectorized haversine function
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    # Earth's radius in kilometers
    return 6371 * c

# Load data
start_time = time.time()
df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv', engine='pyarrow', usecols=['start_lat', 'start_lng', 'end_lat', 'end_lng'])
df = df.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])
print(f"CSV read time: {time.time() - start_time:.2f} seconds")

# Use vectorized haversine function
start_time = time.time()
df['distance_km'] = haversine(df['start_lat'].to_numpy(), df['start_lng'].to_numpy(), df['end_lat'].to_numpy(), df['end_lng'].to_numpy())
print(f"Distance calculation time: {time.time() - start_time:.2f} seconds")

# Compute average distance
start_time = time.time()
average_distance = df['distance_km'].mean()
print(f"Average distance calculation time: {time.time() - start_time:.2f} seconds")
print(f"The average distance per ride is {average_distance:.2f} km.")

total_time = time.time() - start_time_total
print(f"Total computation time: {total_time:.2f} seconds")