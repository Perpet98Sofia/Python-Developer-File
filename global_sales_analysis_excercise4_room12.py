#The Quarterly Revenue Audit 
#Background: You are the new Lead Analyst for a global retail chain. The previous 
#analyst was fired for bad data practices. You have been given a messy file (GLOBAL 
#SALES DATA) and asked to build a reusable Python Class to clean it and generate a 
#report.

import pandas as pd
import numpy as np

#creating the class SalesDataProcessor and loading our csv file into a pandas dataframe
class SalesDataProcessor:  #we have named our class SalesDataProcessor
    def __init__(self, file_name = 'global_sales_data.csv'): #we have initialized the class with a file name
        self.file_name = file_name
        self.df = pd.read_csv("C:\\Users\\Dell\\Downloads\\GLOBAL SALES DATA.csv") #we have read the csv file path into a pandas dataframe
        #print(self.df.head())   #we have printed the first 5 rows of the dataframe
        #print(self.df.info())  #we have printed the info of the dataframe
#The above code defines a class SalesDataProcessor that reads a CSV file into a pandas DataFrame and prints the first five rows of the DataFrame when an instance of the class is created.

# Data Cleaning Method   
        def clean_data(self):  #we are to clean the data by removing anomalies, handling refunds and fixing missing data
        #Using numpy to remove anomalies; rows with unit price > 10,000.
            self.df  = self.df[self.df['Unit_Price'] <= 10000]
        
        #Handling refunds; create a new column Transaction_Type 
        # If Quantity < 0 → Refund, else Purchase
            self.df['Transaction_Type'] = np.where(self.df['Quantity'] < 0, 'Refund', 'Purchase')

        # Fix missing Payment_Method values by filling with "Unknown" 
            self.df['Payment_Method'] = self.df['Payment_Method'].fillna("Unknown")
        print(self.df.info())


#example usage
processor = SalesDataProcessor()  #we have created an instance of the SalesDataProcessor class
