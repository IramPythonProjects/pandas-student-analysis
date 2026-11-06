import pandas as pd

# Load data
df = pd.read_csv('students.csv')

# Explore data
print(df.head())
print(df.info())
print(df.describe())

# 1. Single condition - Toppers
print("Toppers:")
print(df[df['Marks'] > 80])

# 2. Single condition - Failed students
print("Failed in Maths:")
print(df[df['Subject'] == 'Maths'])

# 3. Multiple conditions - AND
print("Gujranwala Toppers:")
print(df[(df['City'] == 'Gujranwala') & (df['Marks'] > 80)])

# 4. Multiple conditions - OR
print("Class 10 OR 70+ Marks:")
print(df[(df['Class'] == 10) | (df['Marks'] > 70)])
