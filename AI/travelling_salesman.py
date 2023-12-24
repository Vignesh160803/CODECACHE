import itertools
import math
def tsp(cities):
    # Generate all possible permutations of cities
    permutations = list(itertools.permutations(cities))

    # Initialize the minimum distance and path
    min_distance = float('inf')
    min_path = None

    # Iterate through each permutation
    for path in permutations:
        distance = 0

        # Calculate the total distance for the current path
        for i in range(len(path) - 1):
            distance += calculate_distance(path[i], path[i+1])

        # Check if the current path has a shorter distance
        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance

def calculate_distance(city1, city2):
    # Calculate the Euclidean distance between two cities
    x1, y1 = city1
    x2, y2 = city2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage
cities = [(0, 5), (4, 5), (3, 8), (1, 2)]
min_path, min_distance = tsp(cities)
print(f"Minimum path: {min_path}")
print(f"Minimum distance: {min_distance}")
