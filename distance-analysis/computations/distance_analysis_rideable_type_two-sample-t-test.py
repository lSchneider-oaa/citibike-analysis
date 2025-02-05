import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

# Load data
df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv', engine='pyarrow',
                 usecols=['start_lat', 'start_lng', 'end_lat', 'end_lng', 'rideable_type'])
df = df.dropna(subset=['start_lat', 'start_lng', 'end_lat', 'end_lng'])

# Define vectorized haversine function
def haversine_real(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    c = 6371 * c * 1.35  # Earth's radius and real-world distance adjustment
    return c

# Calculate distances
df['distance_km'] = haversine_real(df['start_lat'].to_numpy(), df['start_lng'].to_numpy(), 
                                    df['end_lat'].to_numpy(), df['end_lng'].to_numpy())

# Separate data for e-bikes and normal bikes
e_bike_distances = df[df['rideable_type'] == 'electric_bike']['distance_km']
normal_bike_distances = df[df['rideable_type'] == 'classic_bike']['distance_km']

# Perform a two-sample t-test
t_stat, p_value = ttest_ind(e_bike_distances, normal_bike_distances, equal_var=False)

# Display average distances
mean_e_bike = e_bike_distances.mean()
mean_normal_bike = normal_bike_distances.mean()

print(f"Average distance for e-bikes: {mean_e_bike:.2f} km")
print(f"Average distance for normal bikes: {mean_normal_bike:.2f} km")
print(f"Difference in means: {abs(mean_e_bike - mean_normal_bike):.2f} km")


# Display results
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.10e}")

if p_value < 0.05:
    print("The difference in average distances is statistically significant.")
else:
    print("The difference in average distances is not statistically significant.")
