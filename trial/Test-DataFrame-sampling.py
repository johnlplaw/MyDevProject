# Import pandas library
import pandas as pd
import random
from imblearn.over_sampling import RandomOverSampler

# initialize list of lists
data = [['peter',11,1],['john', 10, 1], ['tom', 10, 1], ['nick', 15, 1], ['juli', 14, 2], ['julie', 14, 2], ['albert', 14, 2]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'label'])

# print dataframe.
print(df)
n=4
sampling_df = pd.DataFrame(columns=df.columns)
for label in [1,2]:
    print("  Working on: " + str(label))
    filtered_df = df[df['label'] == label]

    if len(filtered_df) > n:
        subSample_size = n
    else:
        subSample_size = len(filtered_df)
    selected_df = filtered_df.sample(n=subSample_size, random_state=42)
    sampling_df = pd.concat([sampling_df, selected_df], ignore_index=True)

print(sampling_df)

# Assuming you have a dataframe df with features and labels
# X_train contains the features, y_train contains the labels
X_train = sampling_df.drop('label', axis=1)
y_train = sampling_df['label'].tolist()

print(type(X_train))
print(type(y_train))

# Initialize the RandomOverSampler
oversampler = RandomOverSampler(random_state=42)

# Perform oversampling
X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train, y_train)

# Convert the resampled data back to a dataframe
resampled_df = pd.DataFrame(X_train_resampled, columns=X_train.columns)
resampled_df['label_column'] = y_train_resampled

print(resampled_df)
