import dask.dataframe as dd
import numpy as np
import time

start_time_total = time.time()

# Define the vectorized haversine function
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = np.radians(lat1), np.radians(lon1), np.radians(lat2), np.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return 6371 * c


# Read CSV with specified dtypes to handle mixed-type columns
start_time = time.time()
df = dd.read_csv(
    'C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv',
    dtype={
        'start_station_id': 'object',
        'end_station_id': 'object'
    },
    low_memory=False
)
print(f"CSV read time: {time.time() - start_time:.2f} seconds")

# Drop rows with missing data
df = df.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])

# Apply vectorized haversine function across partitions
start_time = time.time()
df['distance_km'] = df.map_partitions(lambda chunk: haversine(
    chunk['start_lat'].to_numpy(), chunk['start_lng'].to_numpy(), chunk['end_lat'].to_numpy(), chunk['end_lng'].to_numpy()
))
print(f"Distance calculation time: {time.time() - start_time:.2f} seconds")

# Trigger computation and calculate the average distance
start_time = time.time()
average_distance = df['distance_km'].mean().compute()
print(f"Average distance calculation time: {time.time() - start_time:.2f} seconds")

print(f"The average distance per ride is {average_distance:.2f} km.")

total_time = time.time() - start_time_total
print(f"Total computation time: {total_time:.2f} seconds")