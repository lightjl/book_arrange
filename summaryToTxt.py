import getContent
import pandas as pd
import arrange
from collections import Counter

class Summary:
    def __init__(self, fold, summaryPath):
        self.toTxt = getContent.saveToFile(fold)
        self.dfBook = pd.read_excel(summaryPath)
        self.ar = arrange.ar(summaryPath, '')
        self.tagSet = set()
        self.tagList = []
        pass

    def saveTxt(self):
        for (index, row) in self.dfBook.iterrows():
            #print(type(list(row[2])))
            listTag = []
            #print(row[2])
            #print(type(row[2])==float)
            if not(row[2] == '[]' or type(row[2])==float):
                listTag = row[2].split("['")[1].split("']")[0].split("', '")
            for tag in listTag:
                self.tagList.append(tag)
        print(Counter(self.tagList).most_common(32))
        mostTag64 = [ith[0] for ith in Counter(self.tagList).most_common(64)]
        print(mostTag64)
        for (index, row) in self.dfBook.iterrows():
            fileName = row[0]
            fileName = fileName.replace('[', '')
            #print(type(list(row[2])))
            listTag = []
            #print(row[2])
            #print(type(row[2])==float)
            if not(row[2] == '[]' or type(row[2])==float):
                listTag = row[2].split("['")[1].split("']")[0].split("', '")
                fileName += '['
                for tag in listTag:
                    if(tag in mostTag64):
                        fileName += tag + ' '
            fileName += tag + ']'
            fileName = fileName.replace('：', '__')
            fileName = fileName.replace(':', '__')
            fileName = fileName.replace('/', '_')
            fileName = fileName.replace('*', '')
            print(fileName+'-'+str(row[3]))
            #print(row[4])      #url
            #print(row[5])
            self.toTxt.save(fileName+'-'+str(row[3]), str(row[4])+'\r\n'+str(row[5]))

        pass


zBook = Summary('eBook', r'D:/pythonResouce/ebookAR.xls')
zBook.saveTxt()