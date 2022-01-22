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
