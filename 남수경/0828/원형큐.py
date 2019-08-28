def isFull():
    return (rear+1) % SIZE == front

def isEmpty():
    return rear ==front

def enQueue(item):
    global rear
    if isFull():
        print("꽉 차서 더는 넣을 수 없습니다.")
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("아무것도 없어서 뽑을 게 없습니다.")
    else:
        front = (front+1)%len(Q)
        return Q[front]

def Qpeek():
    if isEmpty() :
        print("아무것도 없어서 뽑을 게 없습니다.")
    else:
        return Q[(front+1) % len(Q)]



SIZE = 10
Q = [0]*SIZE

front, rear = 0, 0
q_len =0

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())

# 큐 내부에 있는 큐 정보의 길이가 필요한것같다.