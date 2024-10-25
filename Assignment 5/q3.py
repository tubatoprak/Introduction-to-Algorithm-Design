def align_sequences(seq1, seq2):
  m = len(seq1)
  n = len(seq2)
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  # Setting up
  for i in range(1, m + 1):
      dp[i][0] = i
  for j in range(1, n + 1):
      dp[0][j] = j

  # Fill the table
  for i in range(1, m + 1):
      for j in range(1, n + 1):
          if seq1[i - 1] == seq2[j - 1]:
              cost = 0
          else:
              cost = 3  # Substitution cost
          dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

  # Backtrack
  alignment = []
  i, j = m, n
  while i > 0 and j > 0:
      if seq1[i - 1] == seq2[j - 1]:
          alignment.append("Match")
          i -= 1
          j -= 1
      else:
          if dp[i][j] == dp[i - 1][j] + 1:
              alignment.append("Deletion")
              i -= 1
          elif dp[i][j] == dp[i][j - 1] + 1:
              alignment.append("Insertion")
              j -= 1
          else:
              alignment.append("Substitution")
              i -= 1
              j -= 1

  alignment.reverse()
  return dp[m][n], alignment
seq1 = "ACTG"
seq2 = "ATCA"
min_cost, operations = align_sequences(seq1, seq2)
print("Minimum cost:", min_cost)
print("Alignment operations:", operations)
