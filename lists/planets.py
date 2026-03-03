planet_list = ["Mercury", "Mars"]

# function to append jupiter and saturn
def add_planet(planet):
    planet_list.append(planet)
    print(f"Planet `{planet}` added.")
    
#function to display planets 
def display_planet():
    print("Planet List")
    for planet in planet_list:
        print(f"- {planet}")

# function to extend the new added list
def add_planets(planets):
    planet_list.extend(planets)
    for planets in planet_list:
        print(f"Planets `{planets}` added.")


# Add planets
add_planet("Jupiter")
add_planet("Saturn")
print("-----------------------")
#inserting planets correctly on the list
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print("-----------------------")
#calling extend
last_two_planets = ["Uranus", "Neptune"]
add_planets(last_two_planets) 
print("-----------------------")
#Add planet again
add_planet("Pluto")
print("-----------------------")
# Display planet list
display_planet()
print("-----------------------")
# remove pluto from list
del planet_list[8]

# Display planet list after removing Pluto
display_planet()
print("-----------------------")
# rocky planets
rocky_planets = planet_list[0:4]
print("Rocky Planets")
print(rocky_planets)
print("-----------------------")

spacecraft_list = [
    ("Mariner 10", "Mercury", "Venus"),
    ("MESSENGER", "Mercury", "Venus"),
    ("Venera 1-16", "Venus"),
    ("Mariner 2", "Venus"),
    ("Mariner 5", "Venus"),
    ("Pioneer Venus 1 and 2", "Venus"),
    ("Vega 1 and 2", "Venus"),
    ("Magellan", "Venus"),
    ("Venus Express", "Venus"),
    ("Parker Solar Probe", "Venus"),
    ("Mariner 4", "Mars"),
    ("Mariner 6 and 7", "Mars"),
    ("Mariner 9", "Mars"),
    ("Viking 1 and 2", "Mars"),
    ("Mars Pathfinder", "Mars"),
    ("Mars Odyssey", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Phoenix", "Mars"),
    ("Dawn", "Mars"),
    ("Curiosity", "Mars"),
    ("InSight", "Mars"),
    ("Perseverance", "Mars"),
    ("Pioneer 10 and 11", "Jupiter"),
    ("Voyager 1 and 2", "Jupiter", "Saturn", "Uranus", "Neptune"),("Ulysses", "Jupiter"),
    ("Galileo", "Venus", "Jupiter"),
    ("Cassini", "Venus", "Jupiter", "Saturn"),
    ("New Horizons", "Jupiter", "Pluto"),
    ("Juno", "Jupiter"),
    ("Pioneer 11", "Jupiter", "Saturn"),
]

for spacecraft_name, *planets_visited in spacecraft_list:
    print(f"{spacecraft_name} has visited")
    print("-----------------------")
    for planet in planets_visited:
        print(f"{planet}")