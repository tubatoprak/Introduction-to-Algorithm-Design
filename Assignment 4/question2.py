def find_unique_brightest_pixel(image):
  rows, cols = len(image), len(image[0])

  # Start from the top-left corner
  current_row, current_col = 0, 0

  # Move towards the unique brightest pixel
  while True:
      current_brightness = image[current_row][current_col]

      # Check if current pixel is brighter than all neighbors
      if (current_row == 0 or image[current_row - 1][current_col] < current_brightness) and \
         (current_row == rows - 1 or image[current_row + 1][current_col] < current_brightness) and \
         (current_col == 0 or image[current_row][current_col - 1] < current_brightness) and \
         (current_col == cols - 1 or image[current_row][current_col + 1] < current_brightness):
          return (current_row, current_col)  # Found the unique brightest pixel

      # Move to the brighter neighbor
      if current_row > 0 and image[current_row - 1][current_col] > current_brightness:
          current_row -= 1
      elif current_row < rows - 1 and image[current_row + 1][current_col] > current_brightness:
          current_row += 1
      elif current_col > 0 and image[current_row][current_col - 1] > current_brightness:
          current_col -= 1
      elif current_col < cols - 1 and image[current_row][current_col + 1] > current_brightness:
          current_col += 1

# Example usage:
image = [
  [1, 2, 3],
  [11, 5, 6],
  [7, 8, 9]
]

result = find_unique_brightest_pixel(image)
print(f"Unique brightest pixel found at {result}")
