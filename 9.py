import numpy as np, matplotlib.pyplot as plt

sqft = np.array([1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3500, 4000])
price = np.array([200000, 240000, 280000, 300000, 330000, 370000, 410000, 450000, 510000, 570000])

X = np.column_stack([np.ones(10), sqft, np.maximum(sqft - 2000, 0)])
beta = np.linalg.inv(X.T @ X) @ X.T @ price

print(f"Intercept: {beta[0]:.2f}")
print(f"Base Slope (up to 2000 sq ft): {beta[1]:.2f} per sq ft")
print(f"Change in Slope (after 2000 sq ft): {beta[2]:.2f} per sq ft")

plt.scatter(sqft, price, color='blue', label='Data Points')
plt.plot(sqft, X @ beta, color='red', label='Spline Regression Line')
plt.axvline(x=2000, color='gray', linestyle='--', label='Knot at 2000 sq ft')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.title('Spline Regression on Housing Prices')
plt.legend()
plt.show()
