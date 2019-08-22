import sys
sys.stdin = open('반복문자_input.txt')

def hi(sen):
    for i in range(len(sen)-1):
        if sen[i] == sen[i + 1]:
            return True
    return False

T = int(input())
for tc in range(T):
    sen = list(input())
    # print(sen)

    while hi(sen):
        for i in range(len(sen)-1):
            if sen[i] == sen[i+1]:
                sen[i] , sen[i+1] ='', ''
        sen = list(''.join(sen))
    print('#{} {}'.format(tc+1, len(sen)))