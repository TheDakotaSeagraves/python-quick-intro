movie_collection = [
    ("Halloween", "John Carpenter", "1978"),
    ("Friday The 13th Part 3", "Steve Miner", "1982"),
    ("A Nightmare on Elm Street", "Wes Craven", "1984"),
    ("The Evil Dead", "Sam Raimi", "1981"),
    ("The Exorcist", "William Friedkin", "1973")
]

 # Function to display all movies in collection
def display_movies():
    print("Movie_Collection")
    for title, director, year in movie_collection:
        print(f"Title: {title}, Director: {director}, Year: {year}")

# Function to add a new movie to the collection
def add_movie(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)
    print(f"Movie `{title}` directed by {director} added to collection")

# Function to search for movies by a director
def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_director, year = movie
        if movie_director.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director

# Displaying the movies
display_movies()

print("-----------------------------------------")
# Adding a new movie
add_movie("The Lost Boys", "Joel Schumacher", "1987")

print("-----------------------------------------")
# Displaying movies again
display_movies()

print("-----------------------------------------")
# Searching for movies by Wes Craven
movies_by_craven = search_by_director("Wes Craven")
print("Movies by Wes Craven:")
for title, director, year in movies_by_craven:
    print(f"Title: {title}, Year: {year}") 