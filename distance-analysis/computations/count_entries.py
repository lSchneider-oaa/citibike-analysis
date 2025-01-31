import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("citibike_data.db")

# Run a query (example: count rows in the table)
query = "SELECT COUNT(DISTINCT start_station_name) AS start_station_name, COUNT(DISTINCT start_station_id) AS start_station_id, COUNT(DISTINCT end_station_name) AS end_station_name, COUNT(DISTINCT end_station_id) AS end_station_id, COUNT(DISTINCT rideable_type) AS rideable_type, COUNT(DISTINCT member_casual) AS member_casual FROM trips;"
result = pd.read_sql_query(query, conn)

# Print the result
print(result)

# Close the connection
conn.close()