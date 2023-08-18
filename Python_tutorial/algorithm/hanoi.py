def moveDisc(discCnt, fromBar, toBar, viaBar):
    if discCnt == 1:
        print(f'{discCnt}disc를 {fromBar}에서 {toBar}(으)로 이동')

    else:
        # (discNo-1)개를 경유 기둥으로 이동
        moveDisc(discCnt-1, fromBar, viaBar, toBar)

        # discNo를 목적 기둥으로 이동
        print(f'{discCnt}disc를 {fromBar}에서 {toBar}(으)로 이동')

        # (discNo-1)개를 목적 기둥으로 이동
        moveDisc(discCnt-1, viaBar, toBar, fromBar)

moveDisc(3, 1, 3, 2)
