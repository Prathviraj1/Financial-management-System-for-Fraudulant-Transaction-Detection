import csv
import pandas as pd

# file = open("AIML Dataset.csv")
# print(type(file))
# csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# print(header)
#
#
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)
# file.close()

data= pd.read_csv("AIML Dataset.csv")
print(data)
print(data.columns)
print(data.info())

# if data.columns[-2] or data.columns[-1] == 1:
#     print("Transaction is Fraud")
print(data['isFraud'].value_counts())
legit = data[data.isFraud == 0]
fraud = data[data.isFraud == 1]
print(legit.shape)
print(fraud.shape)
print(legit.describe())
print(fraud.describe())


legit_sample = legit.sample(n=8213)
new_dataset = pd.concat([legit_sample, fraud], axis=0)
print(new_dataset.head())
print(new_dataset.tail())
print(new_dataset['isFraud' and "isFlaggedFraud"].value_counts())
print(data.groupby('isFraud').mean())
X = new_dataset.drop(columns='isFraud' and 'isFlaggedFraud', axis=1)
Y = new_dataset['isFraud' and 'isFlaggedFraud']
print(X)
print(Y)