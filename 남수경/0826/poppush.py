# target = list(input().split())
# stack = []
# calc = ['+','*','/']
#
# for t in target:
#     if t not in calc:
#         print(t, end =' ')
#     else:
#         stack.append(t)
#
# for i in range(len(stack)-1,-1,-1):
#     print(stack[i], end=' ')
str = '2+3-4*5'
stack = []
for i in range(len(str)):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        stack.append(str[i])
    else:
        print(str[i], end='')

while len(stack) !=0:
    print(stack.pop(), end='')