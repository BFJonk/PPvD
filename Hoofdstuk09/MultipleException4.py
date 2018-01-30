TryAgain = True

while TryAgain:

    try:
        Value = int(input("Typ een heel getal. "))
    # except BaseException as e:
    #    for Entry in dir(e):
    #       if (not Entry.startswith("_")):
    #          try:
    #             print(Entry, " = ", e.__getattribute__(Entry))
    #          except AttributeError:
    #             print("Attribuut ", Entry, " niet toegankelijk.")
    except ValueError:
        print("\n")
        print("Je moet een heel getal gebruiken!")

        try:
            DoOver = input("Nog een keer (y/n)? ")
        except:
            print("\n")
            print("Goed, tot ziens!")
            TryAgain = False
        else:
            if (str.upper(DoOver) == "N"):
                TryAgain = False

    except KeyboardInterrupt:
        print("\n")
        print("Je gebruikte Ctrl+C!")
        print("Tot ziens!")
        TryAgain = False
    else:
        print(Value)
        TryAgain = False
