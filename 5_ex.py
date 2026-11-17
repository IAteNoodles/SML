import numpy as np
from scipy import stats

sample_size, sample_mean, sample_std = 20, 8, 2
degrees_of_freedom = sample_size - 1
t_statistic = sample_mean / (sample_std / np.sqrt(sample_size))
p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), degrees_of_freedom))
t_critical = stats.t.ppf(0.975, degrees_of_freedom)

print(f"T-statistic: {t_statistic:.3f}")
print(f"P-value: {p_value:.20f}")
print(f"Critical t-value: ±{t_critical:.2f}")
print("Reject the null hypothesis: The drug significantly affects heart rate." if abs(t_statistic) > t_critical
      else "Fail to reject the null hypothesis: No significant effect on heart rate.")
