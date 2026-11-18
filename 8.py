import numpy as np

salary = np.array([40000, 45000, 50000, 55000, 60000, 65000, 70000, 48000, 52000, 58000])
education = np.array(['High School']*2 + ['Bachelor']*2 + ['Master']*3 + ['Bachelor']*2 + ['Master'])
experience = np.array([1, 2, 3, 4, 5, 6, 7, 3, 4, 5])

features = np.column_stack([np.ones(10), education == 'Bachelor', education == 'Master', experience]).astype(float)
coefficients = np.linalg.inv(features.T @ features) @ features.T @ salary

labels = ["Intercept (High School):", "Coefficient for Bachelor's:",
          "Coefficient for Master's:", "Coefficient for Years of Experience:"]
for label, value in zip(labels, coefficients):
    print(label, round(value, 2))
