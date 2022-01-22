import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data= pd.read_csv("AIML Dataset.csv")
print(data)
print(data.columns)
print(data.info())


print(data['isFraud'].value_counts())
legit = data[data.isFraud == 0]
fraud = data[data.isFraud == 1]
flaggedfraud = data[data.isFlaggedFraud == 1]
print(legit.shape)
print(fraud.shape)
print(flaggedfraud.shape)
print(legit.describe())
print(fraud.describe())


legit_sample = legit.sample(n=8213)
new_dataset = pd.concat([legit_sample, fraud], axis=0)
print(new_dataset.head())
print(new_dataset.tail())
print(new_dataset['isFraud' and "isFlaggedFraud"].value_counts())
print(data.groupby('isFraud').mean())

X = new_dataset.drop(new_dataset.iloc[:,9:11],axis=1)
del X['type']
del X['nameDest']
del X['nameOrig']
Y = new_dataset['isFraud']

print("the new data set after dropping the columns is ")
print()
print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.1,test_size=0.9, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

model = LogisticRegression()

model.fit(X_train, Y_train)


X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data : ', training_data_accuracy)

