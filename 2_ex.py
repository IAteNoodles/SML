import pandas as pd, matplotlib.pyplot as plt

customers = pd.DataFrame({'Satisfaction': 'Low Medium High Medium High Low High Medium Low High'.split(),
                          'RepeatPurchase': 'No Yes Yes No Yes No Yes Yes No Yes'.split()})
counts = pd.crosstab(customers.Satisfaction, customers.RepeatPurchase)
print(counts)

for is_stacked in (False, True):
    counts.plot(kind='bar', stacked=is_stacked, figsize=(8, 5), color=['red', 'green'] if is_stacked else None)
    plt.title('Repeat Purchase by Satisfaction Level' + (' (Stacked)' if is_stacked else ''))
    plt.xlabel('Satisfaction level')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=0)
    plt.show()
