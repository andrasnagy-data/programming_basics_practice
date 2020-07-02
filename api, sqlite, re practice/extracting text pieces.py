import re

# getting file
with open("films", "r") as f:
    films = f.read()

# movie date
film_date = re.compile(r'\(\d\d\d\d\)')
dates = film_date.findall(str(films))

# movie name
film_name = re.compile(r'_([^_]+)\(')
names = film_name.findall(str(films))

# saving names to file
with open("movie_names.txt", "w") as e:
    for name in names:
        e.writelines('%s\n' % name)

# saving dates to file
with open("movie_dates.txt", "w") as d:
    for date in dates:
        d.writelines('%s\n' % str(date))