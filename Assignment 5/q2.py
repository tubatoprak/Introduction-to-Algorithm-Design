import math

def calculate_distance(sensor1, sensor2):
    # Calculate the Euclidean distance between two sensors
    return math.sqrt((sensor1[0] - sensor2[0]) ** 2 + (sensor1[1] - sensor2[1]) ** 2)

def secure_perimeter(sensors):
    n = len(sensors)

    # Base case
    if n <= 3:
        return n

    # Sort sensors based on x-coordinate
    sensors.sort()

    # Divide
    mid = n // 2
    left_half = sensors[:mid]
    right_half = sensors[mid:]

    # Recursively find the minimum number of sensors for left and right halves
    left_min = secure_perimeter(left_half)
    right_min = secure_perimeter(right_half)

    # Merge
    # Find the minimum distance between sensors from different halves
    min_distance = min(
        calculate_distance(left_half[-1], right_half[0]),  # Minimum distance between the last sensor in the left half and the first sensor in the right half
        calculate_distance(left_half[0], right_half[-1]),  # Minimum distance between the first sensor in the left half and the last sensor in the right half
    )

    # Check the minimum distance against the minimums from left and right halves
    return min(left_min, right_min, min_distance)

# Example usage:
sensors = [(1, 2), (4, 6), (7, 9), (10, 12), (15, 18), (20, 22)]
result = secure_perimeter(sensors)
print("Minimum number of sensors needed:", result)
