One = int(input("Typ een getal tussen 1 en 10: "))
Two = int(input("Typ een getal tussen 1 en 10: "))

if (One >= 1) and (One <= 10):
    if (Two >= 1) and (Two <= 10):
        print("Je geheime getal is: ", One * Two)
    else:
        print("Verkeerde tweede waarde!")
else:
    print("Verkeerde eerste waarde!")
