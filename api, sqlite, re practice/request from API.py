from imdb import IMDb, IMDbError
import re

try:
    # instance of IMDb
    im = IMDb()

    # getting  top 250 movies
    movies = im.get_top250_movies()


except IMDbError as e:
    print(e)

else:

    # top 250 movie id
    pattern = re.compile(r'\d\d\d\d\d\d\d')
    matches = pattern.finditer(str(movies))

    movie_id = []
    for match in matches:
        movie_id.append(match.group(0))

    # top 250 plot
    movie_info = []
    for movie in movie_id:
        info = im.get_movie(movie, info= "plot")
        plot = info.get("plot")
        movie_info.append(plot)


    with open("data.txt", "w") as f:

        for moviei in movie_info:
            f.write('%s\n' % str(moviei))