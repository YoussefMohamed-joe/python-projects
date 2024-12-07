import sqlite3
import csv

# Create a connection to the SQLite database
conn = sqlite3.connect('itunes_tracks.sqlite')
cur = conn.cursor()

# Create the tables if they don't already exist
cur.execute('''
CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE,
    FOREIGN KEY (artist_id) REFERENCES Artist(id)
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER,
    FOREIGN KEY (album_id) REFERENCES Album(id),
    FOREIGN KEY (genre_id) REFERENCES Genre(id)
)''')

# Open the CSV file and process the rows
with open('itunes_tracks.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip the header row if there's one
    next(reader)
    
    for row in reader:
        track_title = row[0]
        artist_name = row[1]
        album_title = row[2]
        track_length = int(row[3])
        rating = int(row[4])
        play_count = int(row[5])
        genre_name = row[6]
        
        # Insert Artist if not already in the database
        cur.execute('''
        INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )
        ''', (artist_name,))
        
        # Insert Genre if not already in the database
        cur.execute('''
        INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )
        ''', (genre_name,))
        
        # Retrieve the artist id
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
        artist_id = cur.fetchone()[0]
        
        # Retrieve the genre id
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
        genre_id = cur.fetchone()[0]
        
        # Insert Album if not already in the database
        cur.execute('''
        INSERT OR IGNORE INTO Album (artist_id, title)
        VALUES ( ?, ? )
        ''', (artist_id, album_title))
        
        # Retrieve the album id
        cur.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
        album_id = cur.fetchone()[0]
        
        # Insert the Track into the database
        cur.execute('''
        INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )
        ''', (track_title, album_id, genre_id, track_length, rating, play_count))
    
    # Commit the changes to the database
    conn.commit()

# Close the connection to the database
conn.close()
