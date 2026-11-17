import pandas as pd, matplotlib.pyplot as plt

df = pd.DataFrame({'Satisfaction': 'Low Medium High Medium High Low High Medium Low High'.split(),
                   'RepeatPurchase': 'No Yes Yes No Yes No Yes Yes No Yes'.split()})
ct = pd.crosstab(df.Satisfaction, df.RepeatPurchase)
print(ct)

for stacked in (False, True):
    ct.plot(kind='bar', stacked=stacked, figsize=(8, 5), color=['red', 'green'] if stacked else None)
    plt.title('Repeat Purchase by Satisfaction Level' + (' (Stacked)' if stacked else ''))
    plt.xlabel('Satisfaction level')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=0)
    plt.show()
