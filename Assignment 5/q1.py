import math


def distance(p1, p2):
  return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force_closest_pair(drones):
  min_dist = float('inf')
  for i in range(len(drones)):
    for j in range(i + 1, len(drones)):
      dist = distance(drones[i], drones[j])
      min_dist = min(min_dist, dist)
  return min_dist


def find_drones_in_strip(drones, d_min):
  mid = drones[len(drones) // 2][0]
  return [drone for drone in drones if mid - d_min <= drone[0] <= mid + d_min]


def closest_pair_strip(drones, d_min):
  drones.sort(key=lambda p: p[1])  # Sort by y-coordinates
  min_dist = d_min
  for i in range(len(drones)):
    for j in range(i + 1, min(i + 7,
                              len(drones))):  # Check only 6 points ahead
      dist = distance(drones[i], drones[j])
      if dist < min_dist:
        min_dist = dist
  return min_dist


def closest_pair(drones):
  if len(drones) <= 3:
    return brute_force_closest_pair(drones)

  drones.sort(key=lambda p: p[0])  # Sort by x-coordinates
  mid = len(drones) // 2
  left_drones = drones[:mid]
  right_drones = drones[mid:]

  d_left = closest_pair(left_drones)
  d_right = closest_pair(right_drones)

  d_min = min(d_left, d_right)

  middle_drones = find_drones_in_strip(drones, d_min)
  d_strip = closest_pair_strip(middle_drones, d_min)

  return min(d_min, d_strip)


drones = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
min_distance = closest_pair(drones)
print("Minimum distance between drones:", min_distance)
