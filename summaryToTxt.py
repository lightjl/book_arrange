import getContent
import pandas as pd
import arrange
from collections import Counter
import math

class Summary:
    def __init__(self, fold, zPath, ePath):
        self.toTxt = getContent.saveToFile(fold)
        self.zBook = pd.read_excel(zPath)
        self.eBook = pd.read_excel(ePath)
        self.zr = arrange.ar(zPath, '')
        self.er = arrange.ar(ePath, '')
        self.tagSet = set()
        self.tagList = []
        pass

    def __fixFileName(self, fileName):
        fileName = fileName.replace('：', '__')
        fileName = fileName.replace(':', '__')
        fileName = fileName.replace('/', '_')
        fileName = fileName.replace('*', '')
        fileName = fileName.replace('\\', '')
        fileName = fileName.replace('<', '')
        fileName = fileName.replace('>', '')
        fileName = fileName.replace('|', '')
        return fileName

    def saveTxt(self):
        for (index, row) in self.zBook.iterrows():
            #print(type(list(row[2])))
            listTag = []
            if not(row[2] == '[]' or type(row[2])==float):
                listTag = row[2].split("['")[1].split("']")[0].split("', '")
            for tag in listTag:
                self.tagList.append(tag)

        for (index, row) in self.eBook.iterrows():
            if row[0] in self.zBook['name'].values:
                continue
            #print(type(list(row[2])))
            listTag = []
            if not(row[2] == '[]' or type(row[2])==float):
                listTag = row[2].split("['")[1].split("']")[0].split("', '")
            for tag in listTag:
                self.tagList.append(tag)

        print(Counter(self.tagList).most_common(64))
        mostTag64 = [ith[0] for ith in Counter(self.tagList).most_common(64)]
        print(mostTag64)
        for (index, row) in self.zBook.iterrows():
            fileName = row[0]
            fileName = fileName.replace('[', '')
            #print(type(list(row[2])))
            listTag = []
            #print(row[2])
            #print(type(row[2])==float)
            fileName += '['
            if not(row[2] == '[]' or type(row[2])==float):
                listTag = row[2].split("['")[1].split("']")[0].split("', '")
                for tag in listTag:
                    fileName += tag + ' '
            fileName += 'zBook '
            #print(type(row[3]) == float and row[3] != 0 and (not math.isnan(row[3])))
            if (type(row[3]) == float and row[3] != 0 and (not math.isnan(row[3]))):
                fileName += str(int(row[3]/2+1))+'star]'
            else:
                fileName += ']'
            fileName = self.__fixFileName(fileName)
            print(fileName+'-'+str(row[3]))
            #print(row[4])      #url
            #print(row[5])
            self.toTxt.save(fileName+'-'+str(row[3]), str(row[4])+'\r\n'+str(row[5]))


        for (index, row) in self.eBook.iterrows():
            if row[0] in self.zBook['name'].values:
                continue
            fileName = row[0]
            fileName = fileName.replace('[', '')
            fileName = fileName.replace(']', '-')
            #print(type(list(row[2])))
            listTag = []
            #print(row[2])
            #print(type(row[2])==float)
            fileName += '['
            if not(row[2] == '[]' or type(row[2])==float):
                listTag = row[2].split("['")[1].split("']")[0].split("', '")
                for tag in listTag:
                    fileName += tag + ' '
            fileName += 'eBook '
            if (type(row[3]) == float and row[3] != 0 and (not math.isnan(row[3]))):
                fileName += str(int(row[3]/2+1))+'star]'
            else:
                fileName += ']'

            fileName = self.__fixFileName(fileName)
            print(fileName+'-'+str(row[3]))
            #print(row[4])      #url
            #print(row[5])
            self.toTxt.save(fileName+'-'+str(row[3]), str(row[4])+'\r\n'+str(row[5]))



zBook = Summary('ezBook', r'D:/pythonResouce/zbook.xls', r'D:/pythonResouce/ebookAR.xls')
zBook.saveTxt()