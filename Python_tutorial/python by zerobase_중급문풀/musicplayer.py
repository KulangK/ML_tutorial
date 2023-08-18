import random
from time import sleep

class Player:
    def __init__(self):
        self.songList = []
        self.isLoop = False

    def addSong(self, s):
        self.songList.append(s)

    def play(self):                               # 해설 보고 작성
        if self.isLoop:
            while self.isLoop:
                for i in self.songList:
                    print(f'Title: {i.title}, Singer: {i.singer}, Play time: {i.play_time}')
                    sleep(i.play_time)
        else:
            for i in self.songList:
                print(f'Title: {i.title}, Singer: {i.singer}, Play time: {i.play_time}')
                sleep(i.play_time)

    def suffle(self):
        random.shuffle(self.songList)             # shuffle이 list 순서를 바꾸어줌

    def setIsLoop(self, flag):
        self.isLoop = flag


class Song:
    def __init__(self, t, s, pt):
        self.title = t
        self.singer = s
        self.play_time = pt

    def printSongInfo(self):
        print(f'Title: {self.title}, Singer: {self.singer}, Play time: {self.play_time}')
