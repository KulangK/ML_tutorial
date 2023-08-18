def sendSMS(msg):
    if len(msg) > 10:
        raise Exception('10글자 초과, MMS 전환 후 발송', 1)
    else:
        print('SMS 발송')

def sendMMS(msg):
    if len(msg) <= 10:
        raise Exception('10글자 미달, SMS 전환 후 발송', 2)
    else:
        print('MMS 발송')

msg = input('보낼 문자를 입력하세요: ')

try:
    sendSMS(msg)

except Exception as e:
    print(f'e: {e.args[0]}')            # 10글자 초과 되었을시 line 3의 1번째 인덱스 출력
    print(f'e: {e.args[1]}')            # 해당 예외에 2개 배열이 들어간 것을 확인하는 코드

    if e.args[1] == 1:                  # (1) SMS 조건에 맞지 않아 exception이 생기면,
        sendMMS(msg)                    #     MMS function 작동
    elif e.args[1] == 2:                # (2) try가 SMS라서 여기서는 의미가 없지만, try에 MMS로 바꾸면
        sendSMS(msg)                    #     (1)과 비슷한 원리로 작동
