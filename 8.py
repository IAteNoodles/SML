import numpy as np
from scipy import stats

mu, x, s, n = 200, 190, 15, 40
t = (x - mu) / (s / np.sqrt(n))
tc = stats.t.ppf(0.05, n - 1)

print(f"t-statistic: {t:.2f}")
print(f"p-value: {stats.t.cdf(t, n - 1):.5f}")
print(f"Critical t-value: {tc:.2f}")
print("Reject the null hypothesis: The new recipe has significantly fewer calories." if t < tc
      else "Fail to reject the null hypothesis: No significant reduction in calories.")
