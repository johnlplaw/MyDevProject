from imblearn.under_sampling import RandomUnderSampler
import numpy as np
import pandas as pd

# Sample imbalanced dataset (replace this with your dataset)
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([0, 0, 0, 1, 1])

# Initialize the RandomUnderSampler
rus = RandomUnderSampler(random_state=42)

# Perform downsampling
X_resampled, y_resampled = rus.fit_resample(X, y)

# Display the original and resampled class distribution
print("Original class distribution:")
print(pd.Series(y).value_counts())
print("\nResampled class distribution:")
print(pd.Series(y_resampled).value_counts())