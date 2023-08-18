import diary

members = {}
uri = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급문풀/'

def printMembers():
    for m in members.keys():
        print(f'ID: {m} \t PW: {members[m]}')


while True:
    selectNum = int(input('1. 회원가입, 2. 한 줄 일기쓰기, 3. 일기 보기, 4. 종료  '))

    if selectNum == 1:
        mId = input('input ID: ')
        mPw = input('input PW: ')
        members[mId] = mPw
        printMembers()

    elif selectNum == 2:
        mId = input('input ID: ')
        mPw = input('input PW: ')

        if mId in members and members[mId] == mPw:
            print('login success')
            fileName = 'myDiary_' + mId + '.txt'
            data = input('한 줄 일기를 작성해주세요: ')
            diary.writeDiary(uri, fileName, data)

        else:
            print('login fail')
            printMembers()

    elif selectNum == 3:
        mId = input('input ID: ')
        mPw = input('input PW: ')

        if mId in members and members[mId] == mPw:
            print('login success')
            fileName = 'myDiary_' + mId + '.txt'
            datas = diary.readDiary(uri, fileName)
            for d in datas:
                print(d, end='')

        else:
            print('login fail')
            printMembers()

    elif selectNum == 4:
        print('종료')
        break
