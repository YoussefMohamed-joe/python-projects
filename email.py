import sqlite3
import re

# Create a database connection
conn = sqlite3.connect('email_counts.sqlite')
cur = conn.cursor()

# Create the Counts table (if it doesn't already exist)
cur.execute('''CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')

# Open the mbox.txt file
with open('mbox.txt') as f:
    for line in f:
        # Look for lines that start with 'From ' (email lines)
        if line.startswith('From '):
            # Split the line and extract the email address
            words = line.split()
            email = words[1]
            
            # Use a regular expression to extract the domain (part after the @ symbol)
            domain = email.split('@')[1]
            
            # Check if the domain already exists in the table
            cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
            row = cur.fetchone()

            if row is None:
                # If domain doesn't exist, insert a new record
                cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
            else:
                # If domain exists, update the count
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# Commit the changes
conn.commit()

# Fetch the top organizations by count (the top 10)
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')

# Print the top organizations
for row in cur:
    print(f"{row[0]}: {row[1]}")

# Close the connection
conn.close()