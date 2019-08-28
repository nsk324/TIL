import sys
sys.stdin = open('Forth_input.txt')

T = int(input())
operation = '*+-/'

for tc in range(T):
    stack = []
    infix_str=list(input().split()) # 식 받아오기
    for str in infix_str:
        if '0'<= str and str <='9':
            stack.append(str)

        elif str in operation:
            if len(stack) < 2:
                print('#{} error'.format(tc+1))
                break
            else:
                if str == '*':
                    stack[-1] = int(stack[-2]) * int(stack.pop())

                elif str == '+':
                    stack[-1] = int(stack[-2]) + int(stack.pop())

                elif str == '-':
                    stack[-1] = int(stack[-2]) - int(stack.pop())

                elif str == '/':
                    stack[-1] = int(stack[-2]) // int(stack.pop())

        if str =='.':
            if len(stack)>=2:
                print('#{} error'.format(tc + 1))
                break
            else:
                print('#{} {}'.format(tc+1,stack.pop()))