import sys
sys.stdin = open('괄호검사_input.txt')



def check(b):
    arr = []
    open = ['(','{']
    close = [')','}']

    for i in range(len(b)):
        if b[i] in open:
            arr.append(b[i])
        else:
            if b[i] in close:
                if len(arr) == 0:
                    return 0
                if open.index(arr.pop()) != close.index(b[i]):

                    return 0

    if len(arr) > 0:
        return 0
    else:
        return 1

    # for i in range(len(b)):
    #     if b[i] == '(' or b[i] == '{':
    #         arr.append(b[i])
    #     if b[i] == ')'or b[i] =='}':
    #         if len(arr) == 0:
    #             return 0
    #         print(arr)
    #         print(arr[-1],b[i])
    #         if open.index(arr.pop()) != close.index(b[i]):
    #             return 0
    #
    # if len(arr) > 0:
    #     return 0
    #
    # else:
    #     return 1



T = int(input())

for tc in range(T):
    sen = input()
    print('#{} {}'.format(tc+1,check(sen)))
    # print(sen)