import fresh_tomatoes
import media

# Create movie objects
creed = media.Movie(
    "Creed",
    "Rocky trains his old rival's son",
    "https://upload.wikimedia.org/wikipedia/en/2/24/Creed_poster.jpg",
    "https://www.youtube.com/watch?v=fCBzWLVQgk8")

the_martian = media.Movie(
    "The Martian",
    "A botnist stranded on Mars",
    "http://www.impawards.com/2015/posters/martian.jpg",
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

arrival = media.Movie(
    "Arrival",
    "Aliens visit the earth",
    "http://www.impawards.com/2016/posters/arrival.jpg",
    "https://www.youtube.com/watch?v=AMgyWT075KY")

gladiator = media.Movie(
    "Gladiator",
    "A Roman general becomes gladiator",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=owK1qxDselE")

cast_away = media.Movie(
    "Cast Away",
    "A man stranded on an island",
    "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",
    "https://www.youtube.com/watch?v=PJvosb4UCLs")

steve_jobs = media.Movie(
    "Steve Jobs",
    "A movie about Steve Jobs",
    "https://upload.wikimedia.org/wikipedia/en/a/aa/SteveJobsposter.jpg",
    "https://www.youtube.com/watch?v=ufMgQNCXy_M")

# List of movies
movies = [creed, the_martian, arrival, gladiator, cast_away, steve_jobs]

# Open movie pages
fresh_tomatoes.open_movies_page(movies)
