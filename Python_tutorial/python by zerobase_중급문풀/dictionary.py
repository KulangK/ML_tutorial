from abc import ABCMeta
from abc import abstractmethod

class AbsDictionary(metaclass=ABCMeta):

    def __init__(self):
        self.wordDic = {}

    @abstractmethod
    def registword(self, w1, w2):
        pass

    @abstractmethod
    def removeword(self, w1):
        pass

    @abstractmethod
    def updateword(self, w1, w2):
        pass

    @abstractmethod
    def searchword(self, w1):
        pass

class KorToEng(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registword(self, w1, w2):
        print(f'[KorToEng] registWord(): {w1} to {w2}')
        self.wordDic[w1] = w2

    def removeword(self, w1):
        print(f'[KorToEng] removeWord(): {w1}')
        del self.wordDic[w1]

    def updateword(self, w1, w2):
        print(f'[KorToEng] updateWord(): {w1} to {w2}')
        self.wordDic[w1] = w2

    def searchword(self, w1):
        print(f'[KorToEng] searchWord(): {w1}')
        return self.wordDic[w1]

    def printWords(self):
        for k in self.wordDic.keys():
            print(f'{k}: {self.wordDic[k]}')

