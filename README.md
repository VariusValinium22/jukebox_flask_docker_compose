# jukebox_flask_docker_compose
Project title: jukebox
Project description: This is a NuCamp project for building an API. 
        The idea is to have a jukebox of music that a user can choose from. 
        They can purchase a single song or an album of songs by filtering by artist/song/album. 
        This project implemented the skills:
            creating ERDiagram for the juke box idea.(jukebox.drawio)
                designed entites and attributes for each
            creating a db in PostgresSQL using psql and/or PgAdmin
                created tables using Flask (src/models.py)
            creating API logic to make calls from Insomnia HTTP browser
                created a Request Collection in Insomnia for HTTP calls to the API logic
            
Not completed: 
-populate with data using SQLAlchemy ORM(seed.py) modeled after code for twitter already added to this file
-code the API logic for jukebox modeled after twitter code (flask/twitter/src/api/tweets.py)

How did the project's design evolve over time? 
    1. Designed an ERD to define the models/entities of the jukebox 
    2. Implemented the ERD design into PostgresSQL db through PgAdmin and inserted data records
    3. Built .py code for accepting HTTP calls from Insomnia to the API logic that will fetch the requested data from the postgres db
Did you choose to use an ORM or raw SQL? Why? 
    
What future improvements are in store, if any?
    The addition of a User account to keep tabs on costs/payments for the jukebox service. 





What ENDPOINTS would you test in your API? 
What would you think the user would need to retrieve from the db? 
User:
    GET artists
    GET artists/songs
    GET artists/albums
Admin: 
    POST artist
    POST song
    POST album

    PUT artist
    PUT song
    PUT album

    DELETE artist
    ...this would cascade/remove all the artist's songs and albums 
    DELETE song 
    DELETE album
