scoreDic = {'kor': 85, 'eng': 90, 'mat':92, 'sci':79, 'his':82}

uri = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급/'
# for key in scoreDic.keys(): dictionary를 활용한 for문에서는 key를 .keys()로 적어줘야 함.

with open(uri + 'scoreDic.txt', 'a') as f:
    f.writelines(x + '\t: ' + str(scoreDic[x]) + '\n' for x in scoreDic.keys())