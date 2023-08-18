class PasswordLengthShortException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 너무 짧습니다. 다시 입력하세요.')

class PasswordLengthLongException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 너무 깁니다. 다시 입력하세요.')

class PasswordWrongException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 잘못 입력하셨습니다. 다시 입력하세요.')

adminpwd = 'admin1234'

while 1:
    try:
        pwd = input('패스워드를 입력하세요. : ')
        if len(pwd) < 5:
            raise PasswordLengthShortException(pwd)
        elif len(pwd) > 10:
            raise PasswordLengthLongException(pwd)
        elif pwd != adminpwd:
            raise PasswordWrongException(pwd)
        elif pwd == adminpwd:
            print('로그인 성공')
            break

    except PasswordLengthLongException as e:
        print(e)

    except PasswordLengthShortException as e:
        print(e)

    except PasswordWrongException as e:
        print(e)


