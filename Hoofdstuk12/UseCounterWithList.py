from collections import Counter

MyList = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 5]
ListCount = Counter(MyList)

print(ListCount)

for ThisItem in ListCount.items():
    print("Item: ", ThisItem[0],
          " aantal: ", ThisItem[1])

print("De waarde 1 verschijnt {0} keer."
      .format(ListCount.get(1)))
