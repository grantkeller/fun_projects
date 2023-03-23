import re

def find_city(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    # Regular expression to match city names
    regex = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'
    # Find all matches in the text
    matches = re.findall(regex, data)
    # Iterate through matches and check if they are cities
    for match in matches:
        if is_city(match):
            return match
    # No cities found
    return None

def is_city(name):
    # List of cities for comparison
    vacation_cities = ["New York", "Los Angeles", "Chicago", "Las Vegas", "Miami", "San Francisco", "Seattle", "New Orleans",
                   "San Diego", "Honolulu", "Boston", "Washington D.C.", "Orlando", "Austin", "Nashville", "Atlanta", 
                   "Portland", "Denver", "Philadelphia", "San Antonio", "Dallas", "Houston", "Phoenix", "St. Louis", 
                   "Charleston", "Savannah", "Asheville", "Napa", "Santa Fe", "San Juan", "Newport", "Santa Barbara", 
                   "Jacksonville", "Indianapolis", "Salt Lake City", "Kansas City", "Memphis", "Detroit", "Pittsburgh", 
                   "Tucson", "Anchorage", "Portland", "Boulder", "Albuquerque", "Louisville", "Cleveland", "Cincinnati", 
                   "Madison", "Minneapolis", "Paris", "Barcelona", "Rome", "Amsterdam", "London", "Bali", "Phuket", "Tokyo", "Sydney", "Queenstown", 
                   "Cancun", "Puerto Vallarta", "Montego Bay", "Punta Cana", "Cape Town", "Marrakesh", "Dubai", "Bali", 
                   "Phuket", "Rio de Janeiro", "Florence", "Venice", "Santorini", "Mykonos", "Athens", "Madrid", "Seville", 
                   "Berlin", "Munich", "Vienna", "Prague", "Zurich", "Geneva", "Brussels", "Lisbon", "Porto", "Dublin", 
                   "Edinburgh", "Glasgow", "Stockholm", "Oslo", "Copenhagen", "Helsinki", "Reykjavik", "Dubrovnik", 
                   "Split", "Krakow", "Budapest", "Istanbul", "Jerusalem"]
    return name in vacation_cities

# Example usage
file_name = 'transcript.txt'
city = find_city(file_name)
if city:
    print(f"The city mentioned in {file_name} is {city}.")
else:
    print(f"No city mentioned in {file_name}.")
