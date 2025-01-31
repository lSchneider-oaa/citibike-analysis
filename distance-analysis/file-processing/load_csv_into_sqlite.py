import sqlite3
import pandas as pd

# File path for the CSV
file_path = 'C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv'

# Load the CSV into a pandas DataFrame
data = pd.read_csv(file_path)

# Connect to SQLite (creates a database file if it doesn't exist)
conn = sqlite3.connect("citibike_data.db")

# Write the DataFrame to a SQL table
data.to_sql("trips", conn, if_exists="replace", index=False)

# Close the connection
conn.close()

print("CSV data successfully loaded into SQLite database!")