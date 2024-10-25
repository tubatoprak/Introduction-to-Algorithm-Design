def find_max_area_interval(f, n):
  if n <= 1:
      return (0, n), f[0]

  left_interval, left_area = find_max_area_interval(f, n - 1)
  right_interval, right_area = find_max_area_interval(f, n - 2)

  last_two_area = f[n - 1] 
  total_area = sum(f[i] for i in range(n))

  if total_area > max(left_area, right_area, last_two_area):
      return (0, n), total_area
  elif left_area >= right_area and left_area >= last_two_area:
      return left_interval, left_area
  else:
      return right_interval, right_area


f = [2, 1, 2, -2, 1, -1, 1]
n = len(f)

interval, area = find_max_area_interval(f, n)
print(interval, area)

# Output:
# (0, 3), 5