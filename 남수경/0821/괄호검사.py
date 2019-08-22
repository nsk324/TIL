import sys.

def check(b):
    arr = []
    bi = []

    for i in range(len(b)):
        if b[i] == '(' or b[i] == '{':
            arr.append(b[i])
        if b[i] == ')' or b[i] == '}':
            if len(arr) == 0:
                return 0
            bi.append(b[i])
            if arr.pop() != bi[-1]:
                return 0

    if len(arr) > 0:
        return 0

    else:
        return 1


T = int(input())

for tc in range(T):
    sen = list(input())
    print('#{} {}'.format(tc + 1, check(sen)))
    # print(sen)