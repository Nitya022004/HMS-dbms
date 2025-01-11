import MySQLdb

# Connect to MySQL
db = MySQLdb.connect(
    host="localhost",
    user="root",      # Replace with your MySQL username (e.g., "root")
    passwd="",    # Replace with your MySQL password
    db="hmdbms"    # Replace with your database name
)

cursor = db.cursor()

# Example: Fetch data from the `patients` table
try:
    cursor.execute("SELECT * FROM patients")  # Replace 'patients' with your table name
    rows = cursor.fetchall()

    # Print fetched data
    for row in rows:
        print(row)

    cursor.execute("SELECT * FROM doctors")
    demo=cursor.fetchall()

    for dem in demo:
        print(dem)

except Exception as e:
    print(f"Error: {e}")

# Close the connection
cursor.close()
db.close()
