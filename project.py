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
print(df['total_amount'].min())
print(df['total_amount'].max())
print(df['total_amount'].std())
print(df['total_amount'].value_counts())
print(df.sort_values(by='total_amount', ascending=False).head(10))
print(df.groupby('payment_method')['total_amount'].sum())
print(df.groupby('payment_method')['total_amount'].mean())
print(df.groupby('payment_method')['total_amount'].count())