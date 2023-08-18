import book as bk

myB = bk.BookRepository()

myB.registBook(bk.Book('python', 20000, '1234123412'))
myB.registBook(bk.Book('java', 25000, '3456345634'))
myB.registBook(bk.Book('c/c++', 30000, '2345234523'))
myB.registBook(bk.Book('abc', 40000, '2345234523'))

myB.printBooksInfo()
myB.printBookInfo('1234123412')
myB.printBookInfo('3456345634')
myB.printBookInfo('2345234523')
myB.removeBook('2345234523')
myB.printBooksInfo()

print(myB.bDic)