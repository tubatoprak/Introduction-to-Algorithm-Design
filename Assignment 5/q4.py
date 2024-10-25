def calc_discount(set_of_stores):
  return sum(len(store) for store in set_of_stores)

def max_discount_dp(stores):
  n = len(stores)
  max_discounts = [[0] * (n + 1) for _ in range(n + 1)]  
  for i in range(1, n + 1):
      max_discounts[i][i] = calc_discount(stores[:i])

  for i in range(1, n + 1):
      for j in range(1, i + 1):
          subset = stores[j - 1:i] 
          discount_with_current = calc_discount(subset) + max_discounts[j - 1][i - 1]
          discount_without_current = max_discounts[j][i - 1]
          max_discounts[j][i] = max(discount_with_current, discount_without_current)

  return max_discounts[n][n]  
stores = ["Store1", "Store2", "Store3", "Store4"]  
maximum_discount = max_discount_dp(stores)
print("Maximum Achievable Discount:", maximum_discount)
