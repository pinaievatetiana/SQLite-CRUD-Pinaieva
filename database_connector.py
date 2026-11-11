import sqlite3

def create_connection():
    return sqlite3.connect('data.db')

def create_db_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            release_year INTEGER,
            director TEXT,
            rating REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_item(movie_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO movies (title, genre, release_year, director, rating) VALUES (?, ?, ?, ?, ?)",
        (movie_data['title'], movie_data['genre'], movie_data['release_year'], movie_data['director'], movie_data['rating'])
    )
    conn.commit()
    conn.close()

def get_all_items():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    items = cursor.fetchall()
    conn.close()
    return items

def get_item_by_id(movie_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
    item = cursor.fetchone()
    conn.close()
    return item

def update_item(movie_id, movie_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE movies 
        SET title = ?, genre = ?, release_year = ?, director = ?, rating = ? 
        WHERE id = ?
        """,
        (movie_data['title'], movie_data['genre'], movie_data['release_year'], movie_data['director'], movie_data['rating'], movie_id)
    )
    conn.commit()
    conn.close()

def delete_item(movie_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()