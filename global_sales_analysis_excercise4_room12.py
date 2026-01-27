#The Quarterly Revenue Audit 
#Background: You are the new Lead Analyst for a global retail chain. The previous 
#analyst was fired for bad data practices. You have been given a messy file (GLOBAL 
#SALES DATA) and asked to build a reusable Python Class to clean it and generate a 
#report.

import os
from pathlib import Path
import pandas as pd
import numpy as np

#1.creating the class SalesDataProcessor and loading our csv file into a pandas dataframe
class SalesDataProcessor:  
    def __init__(self, file_name='global_sales_data.csv'):
        #resolve the CSV path relative to this file unless an absolute path is provided
        csv_path = Path(file_name)
        
        #if path is absolute use it directly
        if csv_path.is_absolute():
            final_csv_path = csv_path
        else:
        #resolve relative to this file's directory
            final_csv_path = Path(__file__).parent / csv_path

        if final_csv_path.exists():
            self.file_name = str(csv_path)
            self.df = pd.read_csv(self.file_name)
        else:
            raise FileNotFoundError(f"File not found: {final_csv_path}")
        #print(self.df.head())   #we have printed the first 5 rows of the dataframe
        #print(self.df.info())  #we have printed the info of the dataframe
#The above code defines a class SalesDataProcessor that reads a CSV file into a pandas
#DataFrame and prints the first five rows of the DataFrame when an instance of the class is created.

    #2.data cleaning method
    def clean_data(self):  #we are to clean the data by removing anomalies,
        #handling refunds and fixing missing data
        #Using numpy to remove anomalies; rows with unit price > 10,000.
        self.df = self.df[self.df['Unit_Price'] <= 10000]

        #Handling refunds; create a new column Transaction_Type
        # If Quantity < 0 → Refund, else Purchase
        self.df['Transaction_Type'] = np.where(self.df['Quantity'] < 0, 'Refund', 'Purchase')

        # Fix missing Payment_Method values by filling with "Unknown"
        self.df['Payment_Method'] = self.df['Payment_Method'].fillna("Unknown")
        #print(self.df.info())

    #3.Complex Analysis: Category Volatility
    def calculate_category_volatility(self):  # Create a new column Total_Amount = Quantity * Unit_Price
        self.df['Total_Amount'] = self.df['Quantity'] * self.df['Unit_Price']
        category_volatility = self.df.groupby('Category')['Total_Amount'].std()
        # Calculate the standard deviation of Total_Amount for each Category
        most_volatile_category = category_volatility.idxmax()
        # Identify the category with the highest standard deviation
        return most_volatile_category  #returns the most volatile category name

    #4.Visualisation method
    def visualize_trends(self):  #we are to visualize sales trends over time
        import matplotlib.pyplot as plt
        # Convert Date column to datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        # Resample data monthly and sum Total_Amount
        Monthly_Data = self.df.set_index('Date').resample('ME')['Total_Amount'].sum()
        # Plotting a line graph
        plt.figure(figsize=(8, 6))
        plt.plot(Monthly_Data.index, Monthly_Data.values, color='purple', marker='o', linestyle='--')
        plt.title('Monthly Revenue Trends')
        plt.xlabel('Date')
        plt.ylabel('Total Revenue')
        plt.grid(True)
        plt.show()
        plt.savefig('sales_trend.png')  #saving the plot as a PNG file

#example usage:
processor = SalesDataProcessor(r"C:\Users\Dell\Downloads\GLOBAL SALES DATA.csv")
processor.clean_data()
print(processor.df.head())
print(processor.df.info())
volatile_category = processor.calculate_category_volatility()
print("Most volatile category:", volatile_category)
print("Visualizing sales trends...")
processor.visualize_trends()
