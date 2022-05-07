-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'jukebox' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS jukebox;
CREATE DATABASE jukebox;
-- connect via psql
\c jukebox

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

---
--- CREATE tables
---

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE orders (
    id SERIAL,
    date DATE NOT NULL,
    customer_id INT NOT NULL,
    song_id INT NOT NULL, 
    album_id INT
);

CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    artist TEXT NOT NULL,
    song_name TEXT NOT NULL,
    price NUMERIC NOT NULL,
    album_id INT
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    album_name TEXT NOT NULL,
    song_amount INT NOT NULL,
    price NUMERIC NOT NULL, --decimal
    song_id INT NOT NULL
);


--Add FKs

ALTER TABLE customers
ADD CONSTRAINT fk_customers_orders 
FOREIGN KEY (order_id) 
REFERENCES orders (id);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_songs
FOREIGN KEY (song_id) 
REFERENCES songs (id);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_albums
FOREIGN KEY (album_id) 
REFERENCES albums (id);

ALTER TABLE songs
ADD CONSTRAINT fk_songs_albums
FOREIGN KEY (album_id) 
REFERENCES albums (id);

ALTER TABLE albums
ADD CONSTRAINT fk_albums_songs
FOREIGN KEY (song_id) 
REFERENCES songs (id);


--INSERT DATA

INSERT INTO artists (artist_name)
VALUES 
('Fiona Apple'),
('Metallica');

INSERT INTO albums(album_name, song_amount, album_price, artist_id)
VALUES 
    ('Tidal', 10, 2.50, 1),
    ('Master of Puppets', 8, 2.00, 2);

INSERT INTO songs(song_name, song_price, artist_id, album_id)
VALUES 
    ('Sleep to Dream', 0.50, 1, 1),
    ('Sullen Girl', 0.50, 1, 1),
    ('Shadowboxer', 0.50, 1, 1),
    ('Criminal', 0.50, 1, 1),
    ('Slow Like Honey', 0.50, 1, 1),
    ('The First Taste', 0.50, 1, 1),
    ('Never Is a Promise', 0.50, 1, 1),
    ('The Child is Gone', 0.50, 1, 1),
    ('Pale September', 0.50, 1, 1),
    ('Carrion', 0.50, 1, 1),
    ('Battery', 0.50, 2, 2),
    ('Master of Puppets', 0.50, 2, 2),
    ('The Thing That Should Not Be', 0.50, 2, 2),
    ('Welcome Home (Sanitarium)', 0.50, 2, 2),
    ('Disposable Heroes', 0.50, 2, 2),
    ('Leper Messiah', 0.50, 2, 2),
    ('Orion', 0.50, 2, 2),
    ('Damage, Inc.', 0.50, 2, 2);



INSERT INTO customers(first_name, last_name, email, password)
VALUES 
    ('Martin',  'Young',  'martingyoung@hotmail.com', 'jb22'),
    ('Francis', 'Young', 'francislyoung@hotmail.com', 'jb22'),   
    ('Charles', 'Young', 'charleshyoung@hotmail.com', 'jb22'),   
    ('Michael', 'Young', 'michaeljyoung@hotmail.com', 'jb22');

INSERT INTO orders(date, customer_id) 
VALUES 
    ('2022-01-23', 1),
    ('2022-02-04', 2),
    ('2022-11-15', 3),
    ('2022-12-07', 4)
    (current_timestamp, 1);

INSERT INTO order_details(order_id, song_id, album_id) 
VALUES 
(5, 4, null),
(5, null, 6);
--take care of order having to have at least a song or album in code. 



--all FKs
--how can i create an order with only one song 
--and no album(and vice versa) if album/song cannot be NULL??
INSERT INTO order_details()
VALUES    
    (1, 1, 14, );
 

--the cx isn't buying an artist, just either a song or an album of songs but...
--I DID need Artist table to be a completely separate entity/table to
-- avoid redundant/rote changes of artist name column in song/album tables. 

--DB reset to start from scratch
    --delete ALL migrations/versions files
    --use queryTool of a different db: DROP DATABASE jukebox WITH (FORCE);
    --recreate the db: docker exec -i pg_container psql -c 'CREATE DATABASE jukebox;'
    --rework your code in models.py file. 
    --start your migrations again