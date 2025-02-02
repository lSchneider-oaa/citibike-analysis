from numba import jit
import numpy as np
import pandas as pd
import time

start_time_total = time.time()

@jit(nopython=True, parallel=True)
def haversine_numba(lat1, lon1, lat2, lon2):
    # Same Haversine logic as before
    lat1, lon1, lat2, lon2 = np.radians(lat1), np.radians(lon1), np.radians(lat2), np.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return 6371 * c

start_time = time.time()
df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv', low_memory=False)
df = df.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])
print(f"CSV read time: {time.time() - start_time:.2f} seconds")

# Apply with Numba-optimized function
start_time = time.time()
df['distance_km'] = haversine_numba(df['start_lat'].values, df['start_lng'].values, df['end_lat'].values, df['end_lng'].values)
print(f"Distance calculation time: {time.time() - start_time:.2f} seconds")

print(df.memory_usage(deep=True).sum() / (1024 ** 2), "MB")

start_time = time.time()
average_distance = df['distance_km'].mean()
print(f"Average distance calculation time: {time.time() - start_time:.2f} seconds")
print(f"The average distance per ride is {average_distance:.2f} km.")

total_time = time.time() - start_time_total
print(f"Total computation time: {total_time:.2f} seconds")