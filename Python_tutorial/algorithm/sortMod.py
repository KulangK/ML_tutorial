import copy                             # 복사를 위한 모듈

def bubbleSort(ns, deepCopy=True):      # deepCopy는 모듈 같은 것이 아니라 flag 같은 것
                                        # deepCopy 대신 다른 단어를 사용해도 됨.
    if deepCopy:                        # deepCopy가 True일 경우
        cns = copy.copy(ns)             # ns를 이용하여 cns라는 새로운 복사본을 만들어냄
    else:
        cns = ns

    length = len(cns) - 1
    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j + 1]:
                cns[j], cns[j + 1] = cns[j + 1], cns[j]
    return cns

# deepCopy란이 False일 경우, 원본을 얕은 복사하여 원본까지 변경됨.
# deepCopy란이 True인 경우, 깊은 복사하여 새로운 내용만 변경됨.