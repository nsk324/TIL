def isEmpty():
    if len(s) == 0: return True
    else: return False

def push(t):
    global s
    s.append(t)

s = list()

def check_matching(data):
    for i in range(len[data]):
        if data[i] == '(':
            push(data[i])
        elif data[i] ==')':
            if isEmpty(): return False
            pop()
    if not isEmpty() : return False
    else: return True



data = input()
print(check_matching(data))

