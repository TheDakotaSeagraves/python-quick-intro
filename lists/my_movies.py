# Initialize an Empty favorite_movies list
favorite_movies = []

# Function to add a movie
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie `{movie}` added.")

# Function to remove a task
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie `{movie}` removed.")

    else:
        print(f"movie `{movie}` not found.")

# Function to display all movies
def display_movies():
    print("Favorite Movie")
    for movie in favorite_movies:
        print(f"- {movie}")

# Function to count movies
def count_movies():
    total = len(favorite_movies)
    print(f"You have `{total}`movies.")

# Function to find movies
def find_movie(movie):
    if movie in favorite_movies:
        print(f"Movie `{movie}` found.")
    
    else:
        print(f"Movie`{movie}` not found.")

# function to clear movies
def clear_movies():
    favorite_movies.clear()
    print(f"Movies cleared.")            

# Adding movies
add_movie("Avatar")
add_movie("Avatar: 2 Way of Water")
add_movie("Avatar: Fire and Ash")
add_movie("Trolls 2")

# Displaying movies
display_movies()

#Removing a movies
remove_movie("Trolls 2")

#count movies
count_movies()

# find movies
find_movie("Avatar: 2 Way of Water")

# Display movies again
display_movies()

#clear movies
clear_movies()
