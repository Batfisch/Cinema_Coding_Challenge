import pandas
from sqlalchemy import exists
from app import db
from app.models import Screenings, Movies
# Getting the movie titles from the textfile
# writing them to a list which can be given to the database
movies = []
i = 0
film_t = ';'
scr = open('screenings','r')
for line in scr:
        if film_t in line:
            movie = line
            movie = movie.replace(';', '')
            movie = movie.replace('\n', '')
            #print(movie)
            movies.append(movie)
            if i <= int(len(movies)):
                red = Movies.query.filter_by(name=movie).count()
                if red == 0:
                    title = Movies(name=movies[i])
                    db.session.add(title)
                    db.session.commit()
            i = i+1


print(Movies.query.order_by().all())
# import the csv file and deleting the movie titles from it
df = pandas.read_csv('screenings', delimiter='/', lineterminator=',')
df = df.replace('\n', '', regex=True)
df = df.replace('\r', '', regex=True)
df = df.replace(Movies,'', regex=True)
df = df.replace(';', '', regex=True)


#print(df)