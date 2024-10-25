def activate_antennas(antennas):
  antennas.sort(key=lambda x: x[1])
  activated = []
  last_end = float('-inf')

  for start, end in antennas:
      if start >= last_end:
          activated.append((start, end))
          last_end = end

  return activated
antennas = [(1, 5), (3, 7), (2, 6), (8, 10), (9, 12)]
activated_antennas = activate_antennas(antennas)
print("Activated antennas:", activated_antennas) 
