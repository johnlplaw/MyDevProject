import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler

# Sample imbalanced dataset (replace this with your dataset)
# X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
# X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# y = np.array([0, 0, 0, 1, 1]).reshape(-1, 1)

ori_X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = [0, 0, 0, 1, 1]


# Initialize the RandomOverSampler
ros = RandomOverSampler(random_state=42)

# Perform upsampling
X_resampled, y_resampled = ros.fit_resample(X, y)

# Display the original and resampled class distribution
print("Original class distribution:")
print(pd.Series(y).value_counts())
print("\nResampled class distribution:")
print(pd.Series(y_resampled).value_counts())

print(X_resampled)
print(y_resampled)

#Convert
sampled_X = []
for item in X_resampled.tolist():
    sampled_X.append(item[0])
print(ori_X)
print(sampled_X)