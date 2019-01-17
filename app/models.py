from app import db

# defining tables for database


# screenings
class Screenings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Foreign Keys
    movies_id = db.Column(db.Integer, db.ForeignKey("Movies.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("Room.id"))
    # Data in Table
    time = db.Column(db.String(5))
    day = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)

    def __repr__(self):
        return '<Screenings {}>'.format(self.body)


# movies
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Data in Table
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Movies {}>'.format(self.body)


# rooms
class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Data in Table
    name = db.Column(db.String(10))

    def __repr__(self):
        return '<Rooms {}>'.format(self.body)


# seats
class Seats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Foreign Key
    room_id = db.Column(db.Integer, db.ForeignKey("Room.id"))
    # Data in Table
    row = db.Column(db.Integer)
    seat_number = db.Column(db.Integer)

    def __repr__(self):
        return '<Seats {}>'.format(self.body)


# seat_reservations
class SeatReservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Foreign Keys
    seats_id = db.Column(db.Integer, db.ForeignKey("Seats.id"))
    rooms_id = db.Column(db.Integer, db.ForeignKey("Room.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("Costumer.id"))
    screenings_id = db.Column(db.Integer, db.ForeignKey("Screenings.id"))
    # Data in Table
    paid = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Seat_reservation {}>'.format(self.body)


# costumer
class Costumer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Foreign Key
    screenings_id = db.Column(db.Integer, db.ForeignKey("Screenings.id"))
    # Data in Table
    name = db.Column(db.String(50))
    card_number = db.Column(db.Integer)
    card_code = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    number_of_seats = db.Column(db.Integer)

    def __repr__(self):
        return '<Costumer {}>'.format(self.body)
