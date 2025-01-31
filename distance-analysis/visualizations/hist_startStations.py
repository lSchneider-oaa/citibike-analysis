# This analysis will plot the number of trips by start station. But it is basically useless as  the number of start stations is too high to be displayed in a bar chart.

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite
conn = sqlite3.connect("citibike_data.db")

# Query data (example: trips by user type)
query = "SELECT start_station_name, COUNT(*) as trip_count FROM trips GROUP BY start_station_name;"
df = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Plot the data
df.plot(kind="bar", x="start_station_name", y="trip_count", legend=False)
plt.title("Trips by Start Station")
plt.xlabel("Start Station")
plt.ylabel("Number of Trips")
plt.show()