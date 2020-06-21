import pandas as pd


ABC = ['A','B','C','D','E','F','G','H','I','J','K','L']
j = []

csv = pd.read_csv('test.csv', header=None)

print(csv.head())
numheaders = len(csv.columns)

newHeader=[]
x = 0
while x < numheaders:
    newHeader.append(ABC[x])
    x+=1

csv.columns = newHeader

print(csv.head())

print(csv.loc[:, 'A'])