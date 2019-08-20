import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())

exoes = [["ZRO",0],["ONE", 1],["TWO", 2],["THR", 3],["FOR", 4],["FIV", 5],["SIX", 6],["SVN", 7],["EGT", 8],["NIN", 9]]
# exoes = {"ZRO": 0,
#        "ONE": 1,
#        "TWO": 2,
#        "THR": 3,
#        "FOR": 4,
#        "FIV": 5,
#        "SIX": 6,
#        "SVN": 7,
#        "EGT": 8,
#        "NIN": 9
#        }
# print(T)
for t in range(T):
    tc, number = input().split()
    numbers = list(input().split()) # 결과
    # print(numbers)
    number = [] # 0 몇개 1 몇개 등등
    result = []
    for exo in exoes:
        number.append(numbers.count(exo[0]))
    # print(number) #각 숫자
    # print(number[:]) 각 수가 몇개인지


    for i in range(10): #0 부터 9 까지
        for j in range(number[i]):
            result.append(exoes[i][0])
    print(tc)
    print(' '.join(result))
    # print(result)
    # for j in range(len(number)):
    #     for i in range(number[j]):
    #         result.append(exoes[j])
    # print(number)
    # print(result)

    # print(exoes(1))