import numpy as np
from scipy import stats

old_mean, new_mean, new_std, sample_size = 200, 190, 15, 40
degrees_of_freedom = sample_size - 1
t_statistic = (new_mean - old_mean) / (new_std / np.sqrt(sample_size))
p_value = stats.t.cdf(t_statistic, degrees_of_freedom)
t_critical = stats.t.ppf(0.05, degrees_of_freedom)

print(f"t-statistic: {t_statistic:.2f}")
print(f"p-value: {p_value:.5f}")
print(f"Critical t-value: {t_critical:.2f}")
print("Reject the null hypothesis: The new recipe has significantly fewer calories." if t_statistic < t_critical
      else "Fail to reject the null hypothesis: No significant reduction in calories.")
