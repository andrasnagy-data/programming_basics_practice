import sqlite3


def adding_list(list):
    """function to add imdb list to DB"""
    # connecting to DB
    conn = sqlite3.connect("movie.db")
    # cursor object
    c = conn.cursor()
    # execute SQL commands
    c.executemany("""INSERT INTO movies VALUE(?,?,?)""", (list))
    # commiting change to DB
    conn.commit()
    # closing connection
    conn.close()


def pull_movie(id):
    """function to get a movie from table"""
    # connecting to DB
    conn = sqlite3.connect("movie.db")
    # cursor object
    c = conn.cursor()
    # execute SQL commands
    c.execute("""SELECT FROM movies WHERE rowid = (?)""", (id))
    movie = c.fetchone()
    # commiting change to DB
    conn.commit()
    # closing connection
    conn.close()
    return movie


def delete_one(id):
    """function to delete one movie from table"""
    # connecting to DB
    conn = sqlite3.connect("movie.db")
    # cursor object
    c = conn.cursor()
    # execute SQL commands
    c.execute("""DELETE FROM movies WHERE rowid = (?)""", id)
    # commiting change to DB
    conn.commit()
    # closing connection
    conn.close()