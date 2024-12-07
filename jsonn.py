import json
import sqlite3

# Open the JSON file
with open('roster_data.json') as f:
    data = json.load(f)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

# Create tables
cur.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Course (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (course_id) REFERENCES Course(id)
)''')

# Insert data into tables
for entry in data:
    user_name = entry[0]
    course_title = entry[1]
    role = entry[2]

    # Insert user into User table
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user_name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (user_name,))
    user_id = cur.fetchone()[0]

    # Insert course into Course table
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course_title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course_title,))
    course_id = cur.fetchone()[0]

    # Insert member into Member table
    cur.execute('''
    INSERT OR REPLACE INTO Member (user_id, course_id, role)
    VALUES (?, ?, ?)''', (user_id, course_id, role))

# Commit changes and close the connection
conn.commit()

# Execute the required queries
print("Query 1 Result:")
cur.execute('''
SELECT User.name, Course.title, Member.role
FROM User
JOIN Member ON User.id = Member.user_id
JOIN Course ON Course.id = Member.course_id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
''')
for row in cur.fetchall():
    print(row)

print("\nQuery 2 Result:")
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X
FROM User
JOIN Member ON User.id = Member.user_id
JOIN Course ON Course.id = Member.course_id
ORDER BY X LIMIT 1
''')
result = cur.fetchone()
print(result[0])

# Close the connection
conn.close()
