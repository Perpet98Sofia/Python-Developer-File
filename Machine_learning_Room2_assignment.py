from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

#loading the dataset
Data = r"C:\Users\Dell\Downloads\GLOBAL SALES DATA.csv"
df = pd.read_csv(Data)
df['Transaction_Type'] = np.where(df['Quantity'] < 0, 'Refund', 'Purchase')
df['Quantity'] = df['Quantity'].abs()
#print(df.info())
#print(df.head())

#Separate features and target variable
X = df[['Quantity', 'Unit_Price']]  # Features
y = df['Transaction_Type']       # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size=0.2, random_state=42)
#train
model = LogisticRegression()
model.fit(X_train, y_train)
print('This training is successful. The model has learned the pattern')

#predict
y_predict = model.predict(X_test)
print(f'The predicted values are: {y_predict}')
#accuracy
score = accuracy_score(y_test, y_predict)
print(f'The accuracy of the model is: {score}')

#example usage:
#new_transaction = np.array([[5, 500]])  # Example: Quantity=5, Unit_Price=500
#prediction = model.predict(new_transaction)
#if prediction[0] == 'Purchase':
 #   print("The model predicts this is a legitimate sale")
#else:
 #   print("The model predicts this is a refund transaction")
#print(f'The prediction for the new transaction is: {prediction[0]}')

#example2
new_transaction2 = np.array([[0, 0]]) # Quantity=-3, Unit_Price=300
prediction2 = model.predict(new_transaction2)
if prediction2[0] == 'Purchase':
    print("The model predicts this is a legitimate sale")
else:
    print("The model predicts this is a refund transaction")