import musicplayer as mp

s1 = mp.Song('Unholy', 'Sam Smith', 3)
s2 = mp.Song('Hello', 'Adele', 4)
s3 = mp.Song('We Higher', 'Unknown', 3)
s4 = mp.Song('데자뷰', '이영지', 2)
s5 = mp.Song('Go High', '이영지', 4)

player = mp.Player()

player.addSong(s1)
player.addSong(s2)
player.addSong(s3)
player.addSong(s4)
player.addSong(s5)

player.setIsLoop(True)
player.suffle()
player.play()
