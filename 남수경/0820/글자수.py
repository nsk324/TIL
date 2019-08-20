import sys

sys.stdin = open("글자수_input.txt")

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()
    str1_1 = set(str1)
    dic = {}

    for i in str1_1:
        dic[i] = 0

    for i in str1_1:
        for j in str2:
            if i == j:
                dic[i] += 1
    print(dic)
    max = 0
    for value in dic.values():
        if value > max:
            max = value


    print('#{} {}'.format(tc+1,max))


    # cnt = 0
    # for i in range(N2 - N1 + 1):
    #     temp = 0
    #     for j in str1_1:
    #         str2_j = str2[i:i + N1].count(j)
    #         str1_j = str1.count(j)
    #         if str2_j != str1_j:
    #             break
    #         else:
    #             temp += str2_j
    #     if temp == N1:
    #         cnt += 1
    #
    # print(cnt)


