class Book:
    def __init__(self, bName, bPrice, bIsbn):
        self.bName = bName
        self.bPrice = bPrice
        self.bIsbn = bIsbn

class BookRepository:
    def __init__(self):
        self.bDic = {}

    def registBook(self, b):              # Book이 들어감
        self.bDic[b.bIsbn] = b

    def removeBook(self, isbn):
        del self.bDic[isbn]

    def printBooksInfo(self):
        for isbn in self.bDic.keys():
            b = self.bDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')

    def printBookInfo(self, isbn):
        if isbn in self.bDic:
            b = self.bDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')
        else:
            print('The book does not exist')