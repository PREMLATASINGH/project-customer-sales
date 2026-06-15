import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('customer_sales_5000.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df['total_amount'].mean())
print(df['total_amount'].median())