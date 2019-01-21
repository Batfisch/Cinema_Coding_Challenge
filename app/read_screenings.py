import pandas
from sqlalchemy import exists
from app import db
from app.models import Screenings, Movies,Rooms
# Getting the movie titles from the textfile
# writing them to a list which can be given to the database
movies = []
i = 0
film_t = ';'
scr = open('screenings','r')
for film_title in scr:
        if film_t in film_title:
            movie = film_title
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

df = pandas.read_csv('screenings', delimiter='/', lineterminator=',')

i = 0
while i < len(movies):
    print(movies[i])
    df = df.replace(movies[i], '', regex=True)
    i = i+1

df = df.replace(' ', '', regex = True)
#print(Movies.query.order_by().all())
# import the csv file and deleting the movie titles from it
df = df.replace('\n', '', regex=True)
df = df.replace('\r', '', regex=True)
df = df.replace(';', '', regex=True)
# getting Rooms out of the csv file and writing them to the Rooms Table
# also checking that there is only 1 room with a specific name
df_Rooms = df.get('Room')
for Room in df_Rooms:
    room = Room
    #print(room)
    redun = Rooms.query.filter_by(name=room).count()
    if redun == 0:
        Room_name = Rooms(name=room)
        db.session.add(Room_name)
        db.session.commit()

#print(Rooms.query.order_by().all())

# getting all other information from csv File and write them to the screenings table

# writing Screening times into Screenings
#screening_time = df.iterrows()['Time']

for row_index, row in df.iterrows():
    screening_time = row['Time']
    day = row['Day']
    price = row['Price']

    screening = Screenings(time=screening_time, day=day, price=price)
    db.session.add(screening)
print(Screenings.query.order_by().all())
#print (df_Time)
#print(df)