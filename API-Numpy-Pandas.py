#API in python

#import requests
#response = requests.get('https://api.agify.io/?name=Perpetua')
#data = response.json()
#print(data)

#Numpy in python
#import numpy as np
#numbers = np.array([1, 2, 3, 4])
#result = numbers * 2
#print(result)

#numbers = [1,2,3,4]
#result = []
#for n in numbers:
#    result.append(n * 2)
#print(result)

#EXERCISE: Using numpy, Define the list [2000, 3500, 1500, 4000, 7000, 16400, 1376, 2950, 5672,]
#Add 500 to sales above 3000
#Add 2000 across board

#numbers = np.array([2000, 3500, 1500, 4000, 7000, 16400, 1376, 2950, 5672])
#result = []
#for n in numbers:
#    if n > 3000:
#        result.append(n + 500) # Add 500 to sales above 3000
#   else:
#        result.append(n)
#result = np.array(result) + 2000 # Add 2000 across board
#print(result)

#but this one hasn't added the 500 to sales above 3000
#result[result > 3000] += 500
#result =numbers + 2000
#print("Result:", result)

#numbers = np.mean([1,2,3,4,5])
#print(numbers)
#numbers = np.argmax([1,2,3,4,5])
#print(numbers)
#numbers = np.max([1,2,3,4,5])
#print(numbers)
#numbers = np.median([1,2,3,4,5])
#print(numbers)
#numbers = np.sum([1,2,3,4,5])
#print(numbers)


#Pandas in python
import pandas as pd
import numpy as np

data =  {
    'Product': [ 'Apple', 'Banana', 'Cherry'],
    'Sales': [ 100, 150, 290],
    'Store': [ 'North', 'South', 'East']
}

df = pd.DataFrame(data)
print(df)
#Data Extraction
#iloc: Selection by integer position
position = df.iloc[0:2, 0:2]
print(position)

#iloc: Selection by label
df.set_index('Product', inplace=True)
price_of_banana = df.loc['Banana', 'Sales']
print(price_of_banana)
price_of_banana = df.iloc[1, 1]




