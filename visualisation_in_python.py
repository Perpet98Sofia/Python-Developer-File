import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

Data = r"C:\Users\Dell\Downloads\GLOBAL SALES DATA.csv"
df = pd.read_csv(Data)
#print(df.info())
#print(df.head())
df['Total_Amount'] = df['Quantity']*df['Unit_Price']
#print(df.head())
#print(df.info())
df['Date'] = pd.to_datetime(df['Date'])
#print(df.info())
Monthly_Data = df.set_index('Date').resample('ME')['Total_Amount'].sum()
print(Monthly_Data.head())
#plotting a line graph
plt.figure(figsize=(8,4))
#define x-axis(Date) and y-axis(Total Revenue)
plt.plot(Monthly_Data.index, Monthly_Data.values, color='purple', marker='o', linestyle='-')
plt.title('Monthly Revenue Trends')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()