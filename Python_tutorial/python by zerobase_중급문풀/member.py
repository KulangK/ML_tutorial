class Member:                                   # member라는 class는 생성되는 객체에 id와 pw를 담게 됨.
    def __init__(self, i, p):
        self.id = i
        self.pw = p


class MemberRepository:
    def __init__(self):
        self.members = {}                       # members라는 empty dictionary 생성

    def addMember(self, m):
        self.members[m.id] = m.pw               # addMember 실행시 key = id, 해당 key 할당 정보는 password
                                                # dictionary appending 방법 중 하나

    def loginMember(self, i, p):
        isMember = i in self.members            # members dictionary에 i라는 key 존재시, isMember에 할당

        if isMember and self.members[i] == p:   # isMember에 i가 존재하고, 해당 키와 비밀번호 일치 여부 확인
            print(f'{i}: log-in success!!')     # 정확하게 p: 가 의미하는 바가 무엇인지?
        else:
            print(f'{i}: log-in fail!!')

    def removeMember(self, i, p):
        del self.members[i]                     # dictionary deletion 방법

    def printMembers(self):
        for mk in self.members.keys():          # dictionary for문 사용 방법
            print(f'ID: {mk}')                  # mk는 해당 dictionary의 key들을 불러오게 됨.
            print(f'PW: {self.members[mk]}')    # line 9 dictionary에 저장된 할당 비밀번호 불러옴.
