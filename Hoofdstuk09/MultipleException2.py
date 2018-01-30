try:
    Value = int(input("Typ een getal tussen 1 en 10: "))
except ValueError:
    print("Gebruik een getal tussen 1 en 10!")
except KeyboardInterrupt:
    print("\n Je gebruikte Ctrl+C!")
else:

    if (Value > 0) and (Value <= 10):
        print("Je typte: ", Value)
    else:
        print("De getypte waarde is ongeldig!")
