import numpy as np
from scipy import stats

mean_a, std_a, days_a = 1000, 100, 30
mean_b, std_b, days_b = 950, 120, 30
var_of_mean_a, var_of_mean_b = std_a**2 / days_a, std_b**2 / days_b
t_statistic = (mean_a - mean_b) / np.sqrt(var_of_mean_a + var_of_mean_b)
degrees_of_freedom = (var_of_mean_a + var_of_mean_b)**2 / (var_of_mean_a**2 / (days_a - 1) + var_of_mean_b**2 / (days_b - 1))
p_value = 2 * stats.t.sf(abs(t_statistic), degrees_of_freedom)
t_critical = stats.t.ppf(0.975, degrees_of_freedom)

print(f"t-statistic: {t_statistic:.2f}")
print(f"Degrees of Freedom: {degrees_of_freedom:.2f}")
print(f"p-value: {p_value:.5f}")
print(f"Critical t-value: ±{t_critical:.2f}")
print("Reject the null hypothesis: Significant difference in average daily sales." if abs(t_statistic) > t_critical
      else "Fail to reject the null hypothesis: No significant difference in average daily sales.")
