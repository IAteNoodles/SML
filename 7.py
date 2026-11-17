import numpy as np
from scipy import stats

x1, s1, n1 = 1000, 100, 30
x2, s2, n2 = 950, 120, 30
a, b = s1**2 / n1, s2**2 / n2
t = (x1 - x2) / np.sqrt(a + b)
df = (a + b)**2 / (a**2 / (n1 - 1) + b**2 / (n2 - 1))
tc = stats.t.ppf(0.975, df)

print(f"t-statistic: {t:.2f}")
print(f"Degrees of Freedom: {df:.2f}")
print(f"p-value: {2 * stats.t.sf(abs(t), df):.5f}")
print(f"Critical t-value: ±{tc:.2f}")
print("Reject the null hypothesis: Significant difference in average daily sales." if abs(t) > tc
      else "Fail to reject the null hypothesis: No significant difference in average daily sales.")
