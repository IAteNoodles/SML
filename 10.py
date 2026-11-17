import numpy as np

for age, cond, label in [(60, 1, '60 yrs, Chronic Condition'), (60, 0, '60 yrs, No Chronic Condition'),
                         (45, 1, '45 yrs, Chronic Condition'), (30, 0, '30 yrs, No Chronic Condition')]:
    print(f"Expected Visits ({label}): {np.exp(2.5 - 0.03*age + 0.5*cond):.2f} per week")
