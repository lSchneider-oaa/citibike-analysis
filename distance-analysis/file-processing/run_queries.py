import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("citibike_data.db")

# Run a query (example: count rows in the table)
query = "SELECT COUNT(*) AS total_rows FROM trips;"
result = pd.read_sql_query(query, conn)

# Print the result
print(result)

# Close the connection
conn.close()