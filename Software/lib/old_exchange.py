import pandas as pd


ABC = ['A','B','C','D','E','F','G','H','I','J','K','L']

class dataFrame():
    
    def r_csv(self, file):
        self.csv = pd.read_csv(file, header=None)
        numheaders = len(self.csv.columns)
        self.newHeader=[]
        x = 0
        while x < numheaders:
            self.newHeader.append(ABC[x])
            x+=1

        self.csv.columns = self.newHeader

        #return self.csv

    def onlyColumn(self, column):
        column = self.csv[column].tolist()
        return column
    
    def header(self):
        return self.csv
    
    def column(self):
        return self.newHeader
    
    def numberCol(self):
        return len(self.newHeader)
    
    def array2d(self):
        return self.csv.values.tolist()
        
        
        
"""
dicvalue={}

for x in newHeader:
    y = csv[x].tolist()
    dicvalue[x] = y



print(dicvalue['D'])


"""