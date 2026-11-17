import numpy as np
from scipy import stats

n1, x1, n2, x2 = 1000, 120, 1200, 150
pool = (x1 + x2) / (n1 + n2)
z = (x1/n1 - x2/n2) / np.sqrt(pool * (1 - pool) * (1/n1 + 1/n2))
zc = stats.norm.ppf(0.975)

print(f"z-statistic: {z:.2f}")
print(f"p-value: {2 * stats.norm.sf(abs(z)):.5f}")
print(f"Critical z-value: ±{zc:.2f}")
print("Reject the null hypothesis: Significant difference in conversion rates." if abs(z) > zc
      else "Fail to reject the null hypothesis: No significant difference in conversion rates.")
