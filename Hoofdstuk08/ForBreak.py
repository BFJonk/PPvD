Value = input("Typ minder dan 6 tekens: ")
LetterNum = 1

for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1
    if LetterNum > 6:
        print("De string is te lang!")
        break
