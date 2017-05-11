import requests
import json
import time

class book:
    def __init__(self, name, author=None):
        self.name = name
        self.author = author
        #self.checkUrl = 'http://www.cbip.cn/Query.aspx?search_str0=' + urllib.request.quote(name)
        self.checkUrl = 'https://api.douban.com/v2/book/search?q=' + name
        if author is not None:
            self.checkUrl += "+"+author
        #self.checkUrl = 'http://www.cbip.cn/Query.aspx?search_str0=green'
        print(self.checkUrl)

    def getBookInfo(self):
        try:
            html = requests.get(self.checkUrl)
            booksJson = json.loads(html.content.decode())
        except:
            return
        #print(booksJson)
        while ('code' in booksJson):
            time.sleep(60*60)
            try:
                html = requests.get(self.checkUrl)
                booksJson = json.loads(html.content.decode())
            except:
                return [self.name, self.author] + ['' for i in range(4)]

        if len(booksJson['books']) == 0:
            return [self.name, self.author] + ['' for i in range(4)]
        self.tags = [tag['title'] for tag in (booksJson['books'][0]['tags'])]
        #print(tags)
        self.bookUrl = booksJson['books'][0]['alt']
        #print(self.bookUrl)
        self.summary = booksJson['books'][0]['summary']
        #print(self.summary)
        self.rating = booksJson['books'][0]['rating']['average']
        return [self.name, self.author, self.tags, self.rating, self.bookUrl, self.summary]

'''
yb = book('证券分析', '本杰明')
print(yb.getBookInfo())
'''