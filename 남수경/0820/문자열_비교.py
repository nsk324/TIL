import sys
sys.stdin = open("문자열_비교_input.txt")

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()
    str1_1 = set(str1)
    # print(str1_1)
    N1 = len(str1)#찾고자하는거
    N2 = len(str2)
    # print(str1,str2, N1, N2)

    cnt = 0
    for i in range(N2-N1+1):
        temp = 0
        for j in str1_1:
            str2_j = str2[i:i + N1].count(j)
            str1_j =str1.count(j)
            if str2_j != str1_j:
                break
            else:
                temp += str2_j
        if temp == N1:
            cnt = 1




    print(cnt)

