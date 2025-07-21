import psycopg2
from datetime import datetime

# Replace with your Render DB credentials
DB_URL = "postgresql://sample_postgres_db_django_user:tSwHNM7aGfFJp1xfmrPV4Wa9SlLcPvQX@dpg-d1uuks6mcj7s73eseglg-a.oregon-postgres.render.com/sample_postgres_db_django"

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    # Query the Entry table
    cur.execute("SELECT id, title, content, created_at FROM myproject_entry ORDER BY created_at DESC LIMIT 10;")
    entries = cur.fetchall()

    # Display results
    if entries:
        print("\nRecent Entries:")
        for entry in entries:
            print(f"ID: {entry[0]}")
            print(f"Title: {entry[1]}")
            print(f"Content: {entry[2]}")
            print(f"Created At: {entry[3].strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 40)
    else:
        print("No entries found.")

    # Close connections
    cur.close()
    conn.close()

except Exception as e:
    print("Error connecting to database:", e)
