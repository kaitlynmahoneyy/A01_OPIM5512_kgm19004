from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Features + target as a single DataFrame
df = housing.frame

# Quick check
print(df.head())
print(df.shape)

# Making a box plot with House Age
plt.figure(figsize=(12, 8))

df.boxplot(column=['HouseAge'])
plt.title('House Age for California Housing')
plt.ylabel('House Age (Years)')

# Saving box plot
plt.savefig('figs/boxplot.png')
plt.show()
