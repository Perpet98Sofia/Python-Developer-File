from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#data = { 
#   'Age': [22, 25, 47, 52, 46, 56, 21, 55, 60, 25],
#    'Salary': [20000, 43000, 150000, 120000, 90000, 130000, 18000, 160000, 200000, 45000],
#    'Bought': [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
#    }

#Convert the dictionary into a pandas DataFrame
#df = pd.DataFrame(data)
#X = df[['Age', 'Salary']]  # Features
#y = df['Bought']        # Target variable

# Split the dataset into training and testing sets
#x_train, x_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)

#train
#model = LogisticRegression()
#model.fit(x_train, y_train)
#print('This training is successful. The model has learned the pattern')

#predict
#y_pred = model.predict(x_test)



df = pd.read_csv(r"C:\Users\Dell\Downloads\Housing 1.csv")
#print(df.info())
#print(df.head())
binary_column = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'furnishingstatus']
for column in binary_column:
    df[column] = df[column].map({'yes': 1, 'no': 0})
print(df.head())