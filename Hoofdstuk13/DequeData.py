import collections

MyDeque = collections.deque("abcdef", 10)

print("Beginstaat:")
for Item in MyDeque:
    print(Item, end=" ")

print("\r\n\r\nRechts toevoegen en uitbreiden")
MyDeque.append("h")
MyDeque.extend("ij")
for Item in MyDeque:
    print(Item, end=" ")
print("\r\nMyDeque bevat {0} items."
      .format(len(MyDeque)))

print("\r\nRechts met pop verwijderen")
print("Verwijdert {0}".format(MyDeque.pop()))
for Item in MyDeque:
    print(Item, end=" ")

print("\r\n\r\nLinks toevoegen en uitbreiden")
MyDeque.appendleft("a")
MyDeque.extendleft("bc")
for Item in MyDeque:
    print(Item, end=" ")
print("\r\nMyDeque bevat {0} items."
      .format(len(MyDeque)))

print("\r\nLinks met pop verwijderen")
print("Verwijdert {0}".format(MyDeque.popleft()))
for Item in MyDeque:
    print(Item, end=" ")

print("\r\n\r\nMet remove verwijderen")
MyDeque.remove("a")
for Item in MyDeque:
    print(Item, end=" ")
