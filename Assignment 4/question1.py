def find_flawed_fuse(fuses):
  n = len(fuses)

  if n == 1:
      return 0 if not fuses[0] else -1  # Base case: single fuse

  if not fuses[0]:  # Check the first fuse
      return 0

  half_size = n // 2

  broken_index = find_flawed_fuse(fuses[half_size:])  # Recursively search the second half

  if broken_index == -1:  # Broken fuse not found in the second half, search the first half
      return find_flawed_fuse(fuses[:half_size])
  else:
      return half_size + broken_index  # Adjust index based on the half-size


fuses = [True, True, True, True,False, True, True]
broken_fuse_index = find_flawed_fuse(fuses)

if broken_fuse_index == -1:
  print("All fuses are functional.")
else:
  print(f"Broken fuse found at index {broken_fuse_index}.")
