import membership

m_name = input('이름 입력: ')
m_main = input('메일 주소 입력: ')
m_pw = input('비밀번호 입력: ')
m_addr = input('주소 입력: ')
m_phone = input('연락처 입력: ')

try:
    membership.checkInputData(m_name, m_main, m_pw, m_addr, m_phone)
    newMember = membership.RegistMember(m_name, m_main, m_pw, m_addr, m_phone)
    newMember.printMemberInfo()

except membership.EmptyDataException as e:              # 2개 이상 비었을시, checkInputData if문에 의해
                                                        # 가장 첫번째인 이름이 비었다고만 뜨고, 나머지 오류는 안뜸
    print(e)