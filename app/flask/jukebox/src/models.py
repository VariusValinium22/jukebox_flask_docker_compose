import datetime
from enum import unique
from flask_sqlalchemy import SQLAlchemy
import decimal

db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships

class Artists(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.VARCHAR(128), unique=True, nullable=False)

    albums = db.relationship('Album', backref='artist', cascade='all,delete')
    songs = db.relationship('Song', backref='artist', cascade='all,delete')

    def __init__(self, artist_name: str):
        self.artist_name = artist_name
    
    def serialize(self):
        return {
            'id': self.id,
            'artist': self.artist_name
        }

class Albums(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_name = db.Column(db.VARCHAR(128), unique=True, nullable=False)
    song_amount = db.Column(db.Integer, nullable=False)
    album_price = db.Column(db.Numeric, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=True)

    songs = db.relationship('Song', backref='album', cascade='all,delete')
    order_details = db.relationship('Order_detail', backref='album', cascade='all,delete')
    
    def __init__(self, album_name: str, song_amount: int, album_price: decimal, artist_id: int):
        self.album_name = album_name
        self.song_amount = song_amount
        self.album_price = album_price
        self.artist_id = artist_id

    def serialize(self):
        return {
            'id': self.id,
            'album_name': self.album_name,
            'song_amount': self.song_amount,
            'album_price': self.album_price,
            'artist_id': self.artist_id
        }

class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_name = db.Column(db.VARCHAR(128), nullable=False)
    song_price = db.Column(db.Numeric(10,2), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=True)
 
    order_details = db.relationship('Order_detail', backref='song', cascade='all,delete')

    def __init__(self, song_name: str, song_price: decimal, artist_id: int, album_id: int):
        self.song_name = song_name
        self.song_price = song_price
        self.artist_id = artist_id
        self.album_id = album_id
    
    def serialize(self):
        return {
            'id': self.id,
            'song_name': self.song_name,
            'song_price': self.song_price,
            'artist_id': self.artist_id,
            'album_id' : self.album_id
        }

class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    orders = db.relationship('Order', backref='customer', cascade='all,delete')

    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    
    order_details = db.relationship('Order_detail', backref='order', cascade='all,delete')    

    def __init__(self, date: datetime, customer_id: int):
        # self.date = date    #this will auto-populate so it is not needed here?
        self.customer_id = customer_id
    
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'customer_id': self.customer_id
        }

class Order_details(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=True)

    def __init__(self, order_id: int, song_id: int, album_id: int):
        self.order_id = order_id
        self.song_id = song_id
        self.album_id = album_id
    
    def serialize(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'song_id': self.song_id,
            'album_id': self.album_id
        }

# placed FK customer_id in  Orders          table for 1-M relationship
# placed FK order_id   in   Order_details   table for 1-1 relationship
# placed FK song_id    in   Order_details   table for 1-M relationship
# placed FK album_id   in   Order_details   table for 1-M relationship
# placed FKs Song_id and Album_id   in each model for M-M relationship

# placed relationship() to Orders        in Customers
# placed relationship() to Order_details in Orders, Songs, Albums
# placed relationship() to Songs         in Albums






