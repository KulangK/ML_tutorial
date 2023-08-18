import time

lt = time.localtime()

dateStr = '[' + str(lt.tm_year) + '년' + \
          str(lt.tm_mon) + '월' + \
          str(lt.tm_mday) + '일] '

schedule = input('오늘 일정: ')

file = open('C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급/test.txt', 'w')
file.write(dateStr + schedule)
file.close()
