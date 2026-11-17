import numpy as np
from scipy import stats

users_a, sales_a = 1000, 120
users_b, sales_b = 1200, 150
pooled_rate = (sales_a + sales_b) / (users_a + users_b)
std_error = np.sqrt(pooled_rate * (1 - pooled_rate) * (1/users_a + 1/users_b))
z_statistic = (sales_a/users_a - sales_b/users_b) / std_error
p_value = 2 * stats.norm.sf(abs(z_statistic))
z_critical = stats.norm.ppf(0.975)

print(f"z-statistic: {z_statistic:.2f}")
print(f"p-value: {p_value:.5f}")
print(f"Critical z-value: ±{z_critical:.2f}")
print("Reject the null hypothesis: Significant difference in conversion rates." if abs(z_statistic) > z_critical
      else "Fail to reject the null hypothesis: No significant difference in conversion rates.")
