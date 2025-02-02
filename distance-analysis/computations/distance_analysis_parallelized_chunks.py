import pandas as pd
import numpy as np
import time

start_time_total = time.time()

# Define the vectorized haversine function
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return 6371 * c  # Earth's radius in km

# Read CSV in chunks and process each chunk
start_time = time.time()
chunk_size = 170000  # Adjust the chunk size as needed
total_distance = 0
total_rows = 0
start_time = time.time()
for chunk in pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv', chunksize=chunk_size, low_memory=False):
    # Drop rows with missing values in each chunk
    chunk = chunk.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])

    # Apply the vectorized haversine function
    chunk['distance_km'] = haversine(chunk['start_lat'].values, chunk['start_lng'].values, chunk['end_lat'].values, chunk['end_lng'].values)

    # Sum distances and row counts for averaging
    total_distance += chunk['distance_km'].sum()
    total_rows += len(chunk)
print(f"CSV read and distance calculation time: {time.time() - start_time:.2f} seconds")

# Calculate and print the average distance
start_time = time.time()
average_distance = total_distance / total_rows
print(f"Average distance calculation time: {time.time() - start_time:.2f} seconds")
print(f"The average distance per ride is {average_distance:.2f} km.")

total_time = time.time() - start_time_total
print(f"Total computation time: {total_time:.2f} seconds")