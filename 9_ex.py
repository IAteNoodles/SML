import numpy as np, matplotlib.pyplot as plt

square_feet = np.array([1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3500, 4000])
price = np.array([200000, 240000, 280000, 300000, 330000, 370000, 410000, 450000, 510000, 570000])

features = np.column_stack([np.ones(10), square_feet, np.maximum(square_feet - 2000, 0)])
coefficients = np.linalg.inv(features.T @ features) @ features.T @ price

print(f"Intercept: {coefficients[0]:.2f}")
print(f"Base Slope (up to 2000 sq ft): {coefficients[1]:.2f} per sq ft")
print(f"Change in Slope (after 2000 sq ft): {coefficients[2]:.2f} per sq ft")

plt.scatter(square_feet, price, color='blue', label='Data Points')
plt.plot(square_feet, features @ coefficients, color='red', label='Spline Regression Line')
plt.axvline(x=2000, color='gray', linestyle='--', label='Knot at 2000 sq ft')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.title('Spline Regression on Housing Prices')
plt.legend()
plt.show()
