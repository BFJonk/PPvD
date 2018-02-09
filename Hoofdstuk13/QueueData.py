import queue

MyQueue = queue.Queue(3)

print(MyQueue.empty())
input("Druk op een toets...")

MyQueue.put(1)
MyQueue.put(2)
print(MyQueue.full())
input("Druk op een toets...")

MyQueue.put(3)
print(MyQueue.full())
input("Druk op een toets...")

print(MyQueue.get())
print(MyQueue.empty())
print(MyQueue.full())
input("Druk op een toets...")

print(MyQueue.get())
print(MyQueue.get())
