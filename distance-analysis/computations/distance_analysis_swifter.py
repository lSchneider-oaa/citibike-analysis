import pandas as pd
import geopy.distance as gd
import swifter

# Load data
df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv', low_memory=False)

# Drop rows with missing latitude/longitude
df = df.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])

# Use swifter to apply the geodesic calculation in parallel
df['distance_km'] = df.swifter.apply(
    lambda row: gd.geodesic((row['start_lat'], row['start_lng']), (row['end_lat'], row['end_lng'])).km,
    axis=1
)

# Compute average distance
average_distance = df['distance_km'].mean()
print(f"The average distance per ride is {average_distance:.2f} km.")
