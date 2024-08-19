import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 32, 37]
})
for index, row in df.iterrows():
    print(row['Name'] + "-" + str(row['Age']))