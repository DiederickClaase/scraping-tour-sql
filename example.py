import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE date='2024.04.15'")
rows = cursor.fetchall()
print(rows)

# Query certain data
cursor.execute("SELECT band, date FROM events WHERE date='2024.04.15'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
#new_rows = [('Cats', 'Cats City', '2024.04.25')]

#cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_rows)
#connection.commit()

# Query all data
cursor.execute("SELECT * FROM events ")
rows = cursor.fetchall()
print(rows)
