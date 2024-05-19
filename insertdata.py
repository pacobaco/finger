import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('inmates.db')
cursor = conn.cursor()

# Create a table for storing inmate data
cursor.execute('''
CREATE TABLE IF NOT EXISTS inmates (
    id INTEGER PRIMARY KEY,
    name TEXT,
    register_number TEXT,
    age INTEGER,
    race TEXT,
    sex TEXT,
    release_date TEXT,
    location TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
