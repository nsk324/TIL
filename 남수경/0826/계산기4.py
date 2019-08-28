import sys
sys.stdin = open("input.txt")
T = 10
N = int(input())
hi = list(input())
stack = [] #[0 for _ in range(N)]
result = []
numbers =['1','2','3','4','5','6','7','8','9']

for i in range(len(hi)):
    if hi[i] == '(' :
        stack.append(hi[i])
    elif hi[i] in numbers:
        result.append(hi[i])
    elif hi[i] == '+':
        if stack[-1] == '*':


print(hi, stack,result)