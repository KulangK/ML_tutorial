# 1부터 사용자가 입력한 정수까지의 합, 홀수의 합, 짝수의 합 그리고 팩토리얼을 출력하는 프로그램을 만들자

userInput = int(input('정수 입력: '))

sum = 0
oddSum = 0
evenSum = 0
facto = 1

for i in range(1, userInput+1):
      sum += i
      facto *= i
      if i % 2 == 0:
            evenSum += i
      else:
            oddSum += i

print('합 결과 : {}\n홀수 합 결과 : {}\n짝수 합 결과 : {}\n팩토리얼 결과 : {}'\
      .format(sum, oddSum, evenSum, format(facto, ',')))