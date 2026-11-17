import numpy as np, seaborn as sns, matplotlib.pyplot as plt

np.random.seed(42)
population_salaries = np.random.exponential(scale=50000, size=10000)
sample_means = np.array([np.random.choice(population_salaries, size=50, replace=False).mean()
                         for _ in range(1000)])

print("Population size:", 10000)
print("Sample Size:", 50)
print("Number of samples:", 1000)
print()
print("Population Mean:", round(population_salaries.mean(), 2))
print("Mean of Sample Means:", round(sample_means.mean(), 2))
print()
print("First 10 Sample Means:")
print(np.floor(sample_means[:10] * 1e4) / 1e4)

plt.figure(figsize=(10, 6))
sns.histplot(sample_means, bins=30, kde=True, stat="density")
plt.title("Sampling Distribution of Sample Mean\n(n = 50, Number of Samples = 1000)")
plt.xlabel('Sample Mean Salary')
plt.ylabel("Density")
plt.grid(alpha=0.3)
plt.show()
