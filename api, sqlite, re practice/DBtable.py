import sqlite3
from sqlite3 import Error


# creating lists from txt files
with open("movie_names.txt", "r") as a:
    names = a.readlines()
with open("movie_dates.txt", "r") as b:
    dates = b.readlines()
with open("data.txt", "r") as c:
    plots = c.readlines()

# creating a list of tuples
movie_table = list(zip(names, dates, plots))

# connection to database
try:
    conn = sqlite3.connect('movie.db')
except Error as e:
    print(e)
else:
    # cursor object
    c = conn.cursor()

    # past SQL commands
    Q1 = """CREATE TABLE movies (
    title text,
    year text,
    plot text
    )"""

    c.execute()

    # commit changes
    conn.commit()
    # close connection
    conn.close()

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


# adding the list of tuples to DB table
adding_list(movie_table)
