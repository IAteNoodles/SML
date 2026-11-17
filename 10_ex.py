import numpy as np

patients = [(60, 1, '60 yrs, Chronic Condition'), (60, 0, '60 yrs, No Chronic Condition'),
            (45, 1, '45 yrs, Chronic Condition'), (30, 0, '30 yrs, No Chronic Condition')]

for age, has_condition, description in patients:
    expected_visits = np.exp(2.5 - 0.03*age + 0.5*has_condition)
    print(f"Expected Visits ({description}): {expected_visits:.2f} per week")
