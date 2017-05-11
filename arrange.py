from pandas import DataFrame
import pandas as pd
import book

class ar:
    def __init__(self, fromPath, toPath):
        self.originPath = fromPath
        self.dfBook = pd.read_excel(fromPath)
        #print(self.dfBook)
        self.toPath = toPath

    def arrangeAZ(self):
        bookInfo = []
        for (index, row) in self.dfBook.iterrows():
            bookName = row[0].split('（')[0].split('(')[0]
            bookInfo.append(book.book(bookName, row[1].replace('•', '')).getBookInfo())
        # print(bookInfo)
        coloums = ['name', 'author', 'tags', 'rating', 'bookUrl', 'summary']
        df = DataFrame(bookInfo, columns=coloums)
        df.to_excel(self.toPath)

    def arrangeEbook(self):
        bookInfo = []
        for (index, row) in self.dfBook.iterrows():
            bookName = row[0].split('\\')[-1].split('.')[0]
            bookName = bookName.split('（')[0].split('(')[0]
            #print(bookName)
            bookInfo.append(book.book(bookName).getBookInfo())

        print(bookInfo)
        coloums = ['name', 'author', 'tags', 'rating', 'bookUrl', 'summary']
        df = DataFrame(bookInfo, columns=coloums)
        df.to_excel(self.toPath)

    def arrangeBook233(self, fixPath):
        # todo 现只用书名查找，书名+作者查找
        # 原因：原始书名经过格式化处理，没办法对应原作者
        # 对策：建立一个dataframe 存储格式化后的书名与作者
        originBook = pd.read_excel(self.originPath)
        resultBook = pd.read_excel(self.toPath)
        originName = set(originBook['name'].values)
        originNameFixed = []
        for name in originName:
            nameFixed = name.split('（')[0].split('(')[0]
            #bookName = name.split('\\')[-1].split('.')[0]
            #nameFixed = bookName.split('（')[0].split('(')[0]
            originNameFixed.append(nameFixed)
        toFindBook = (set(originNameFixed) - set(resultBook['name'].values))

        bookInfo = []
        for bookname in toFindBook:
            bookInfo.append(book.book(bookname).getBookInfo())
        #print(bookInfo)
        coloums = ['name', 'author', 'tags', 'rating', 'bookUrl', 'summary']
        df = DataFrame(bookInfo, columns=coloums)
        df.to_excel(fixPath)


#zBook = ar(r'D:/pythonResouce/亚马逊电子书233.xlsx', r'D:/pythonResouce/book.xls')
#eBook = ar(r'D:/pythonResouce/eBook.xlsx', r'D:/pythonResouce/ebookAR.xls')
#eBook.arrangeEbook()

#test = ar(r'D:/pythonResouce/book.xls', r'D:/pythonResouce/ebookAR233.xls')
#test.arrangeBook233(r'D:/pythonResouce/EbookFixed.xls')
