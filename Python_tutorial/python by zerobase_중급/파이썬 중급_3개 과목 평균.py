# 국어, 영어, 수학 점수를 입력받고, 입력 받은 점수를 이용해서 총점과 평균을 출력하는 함수를 만들어보자.

def testScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = round(sum / 3, 1)
    print(f'총점 : {sum}점\n평균 : {avg}점')

kor = int(input('국어 점수 입력: '))
eng = int(input('영어 점수 입력: '))
mat = int(input('수학 점수 입력: '))

testScore(kor, eng, mat)