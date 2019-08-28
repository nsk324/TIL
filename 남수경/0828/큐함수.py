import queue
q = queue.Queue() # 큐 생성
q.put(1)
q.put(2)
q.put(3)
print(q)
print(q.get()) # dequeue
print(q)
print(q.get())
print(q)
print(q.get())