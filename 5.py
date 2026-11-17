import numpy as np
from scipy import stats

n, mean, sd = 20, 8, 2
t = mean / (sd / np.sqrt(n))
tc = stats.t.ppf(0.975, n - 1)

print(f"T-statistic: {t:.3f}")
print(f"P-value: {2 * (1 - stats.t.cdf(abs(t), n - 1)):.20f}")
print(f"Critical t-value: ±{tc:.2f}")
print("Reject the null hypothesis: The drug significantly affects heart rate." if abs(t) > tc
      else "Fail to reject the null hypothesis: No significant effect on heart rate.")
