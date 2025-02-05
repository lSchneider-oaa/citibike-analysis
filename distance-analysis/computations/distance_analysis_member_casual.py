import numpy as np
import pandas as pd

# Define vectorized haversine function
def haversine_real(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    # Earth's radius in kilometers
    c = 6371 * c

    # Convert from straight line to real world distance
    c = c * 1.35

    return c

# Load data
df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv', engine='pyarrow', 
                 usecols=['start_lat', 'start_lng', 'end_lat', 'end_lng', 'member_casual'])
df = df.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])

# Use vectorized haversine_real function
df['distance_km'] = haversine_real(df['start_lat'].to_numpy(), df['start_lng'].to_numpy(), df['end_lat'].to_numpy(), df['end_lng'].to_numpy())

# Calculate average distance by bike type
average_distances = df.groupby('member_casual')['distance_km'].mean()

# Display the results
for rider_type, avg_distance in average_distances.items():
    print(f"The average distance for {rider_type} is {avg_distance:.2f} km.")
