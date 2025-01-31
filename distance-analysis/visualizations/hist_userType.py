import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite
conn = sqlite3.connect("citibike_data.db")

# Query data (example: trips by user type)
query = "SELECT member_casual, COUNT(*) as trip_count FROM trips GROUP BY member_casual;"
df = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Plot the data
df.plot(kind="bar", x="member_casual", y="trip_count", legend=False)
plt.title("Trips by User Type")
plt.xlabel("User Type")
plt.ylabel("Number of Trips")
plt.show()