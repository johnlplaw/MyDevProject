from imblearn.under_sampling import RandomUnderSampler
import numpy as np

# Sample data generation (replace this with your dataset)
# Let's create a dummy dataset with 3 features and 2 classes
X = np.random.rand(1000, 3)  # 1000 samples, 3 features
y = np.random.randint(0, 2, 1000)  # 2 classes (0 and 1)

for i in X:
    print(i[0])
    print(type(i))
    print(i.shape)

# Initialize RandomUnderSampler
undersampler = RandomUnderSampler()

# Perform undersampling
X_resampled, y_resampled = undersampler.fit_resample(X, y)

# Display class distribution before and after undersampling
print("Class distribution before undersampling:")
print(np.bincount(y))
print("Class distribution after undersampling:")
print(np.bincount(y_resampled))