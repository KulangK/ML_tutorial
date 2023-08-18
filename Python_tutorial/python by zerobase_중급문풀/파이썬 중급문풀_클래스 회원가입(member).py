import member as mb
# member 파일 안의 클래스 및 기능 활용

mems = mb.MemberRepository()        # MemberRepository class를 간략히 부르기 위함

for i in range(3):                  # 예시로 3개의 회원가입 진행
    mId = input('아이디 입력:')
    mPw = input('비밀번호 입력:')

    mem = mb.Member(mId, mPw)       # Member class로 객체 생성
    mems.addMember(mem)             # 해당 객체의 id와 pw가 MemberRepository dictionary에 저장

mems.printMembers()

mems.loginMember('abc@gmail.com', '1234')
mems.loginMember('def@gmail.com', '5678')
mems.loginMember('ghi@gmail.com', '9012')

mems.removeMember('abc@gmail.com', '1234')

mems.printMembers()