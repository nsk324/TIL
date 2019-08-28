def isFull():
    if rear == SIZE-1:
        return True
    return False

def isEmpty():
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print('값을 더 넣을 수 없어요.')
    else:
        rear +=1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("큐가 비어있어서 빼낼 게 없어요")
    else:
        front += 1
        return Q[front]


def Qpeek():
    if isEmpty():
        print("값이 없어요")
    else:
        return Q[front+1]




SIZE = 100
Q = [0]*SIZE
front, rear = -1, -1


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
