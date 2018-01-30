MyStack = []
StackSize = 3


def DisplayStack():
    print("Stapel bevat nu:")
    for Item in MyStack:
        print(Item)


def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Stapel is vol!")


def Pop():
    if len(MyStack) > 0:
        MyStack.pop()
    else:
        print("Stapel is leeg.")


Push(1)
Push(2)
Push(3)
DisplayStack()
input("Druk op een toets...")

Push(4)
DisplayStack()
input("Druk op een toets...")

Pop()
DisplayStack()
input("Druk op een toets...")

Pop()
Pop()
Pop()
DisplayStack()
