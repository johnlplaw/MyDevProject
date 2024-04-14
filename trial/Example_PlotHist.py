import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn-notebook')
fig, ax = plt.subplots()
trans = ax.get_xaxis_transform()

data = pd.read_csv('data_age.csv')
ids = data['Responder_id']
ages = data['Age']

print(ages)

counts, bins = np.histogram(ages)

print(counts)
print(bins)

# bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
plt.hist(ages, bins=bins, edgecolor='black', log=True)

median = np.median(ages)
print(median)
plt.axvline(median, color='red', label='Median', linewidth=2)

mean = np.mean(ages)
print(mean)
plt.axvline(mean, color='green', label='Mean', linewidth=2)
# plt.text(mean,0,'Mean: ' + str(mean), transform=trans)

plt.legend()
#
plt.title('Length of the texts')
plt.xlabel('Lengths')
plt.ylabel('Count')

plt.tight_layout()
plt.show()