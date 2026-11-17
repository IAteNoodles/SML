import numpy as np

house_prices = [250000, 300000, 320000, 350000, 400000, 420000, 450000, 500000, 550000, 600000]
q1, q3 = np.percentile(house_prices, [25, 75])

print("25th percentile (Q1):", q1)
print("75th percentile (Q3):", q3)
print("Interquartile Range (IQR):", q3 - q1)
