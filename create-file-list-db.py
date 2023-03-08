# write python script to create database for files and folders
# and search for files and folders

import os
import sqlite3

conn = sqlite3.connect('file.db')
cur = conn.cursor()

directory_location = "<YOUR FOLDER LOCATION TO SEARCH FILES>"

cur.execute('DROP TABLE IF EXISTS Files')
cur.execute('CREATE TABLE Files (id INTEGER PRIMARY KEY, name TEXT UNIQUE, path TEXT UNIQUE)')
conn.commit()
def search_files():
    for root, dirs, files in os.walk(directory_location):
        for file in files:
            try:
                cur.execute('INSERT INTO Files (name, path) VALUES (?, ?)', (file, os.path.join(root, file)))
            except:
                continue
    conn.commit()
search_files()

