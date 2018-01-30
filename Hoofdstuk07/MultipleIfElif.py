print("1. Eieren")
print("2. Pannenkoeken")
print("3. Wafels")
print("4. Havermout")
MainChoice = int(input("Kies een ontbijtgerecht: "))

if (MainChoice == 2):
    Meal = "Pannenkoeken"
elif (MainChoice == 3):
    Meal = "Wafels"

if (MainChoice == 1):
    print("1. Volkoren")
    print("2. Zuurdesem")
    print("3. Toast")
    print("4. Wit")
    Bread = int(input("Kies een broodsoort: "))

    if (Bread == 1):
        print("Je koos eieren met volkorenbrood.")
    elif (Bread == 2):
        print("Je koos eieren met zuurdesembrood.")
    elif (Bread == 3):
        print("Je koos eieren met toast.")
    elif (Bread == 4):
        print("Je koos eieren met witbrood.")
    else:
        print("We hebben eieren, maar niet dat type brood.")

elif (MainChoice == 2) or (MainChoice == 3):
    print("1. Stroop")
    print("2. Aardbeien")
    print("3. Poedersuiker")
    Topping = int(input("Kies een type beleg: "))

    if (Topping == 1):
        print("Je koos " + Meal + " met siroop.")
    elif (Topping == 2):
        print("Je koos " + Meal + " met aardbeien.")
    elif (Topping == 3):
        print("Je koos " + Meal + " met poedersuiker.")
    else:
        print("We hebben " + Meal + ", maar niet dat beleg.")

elif (MainChoice == 4):
    print("Je koos havermout.")

else:
    print("Dat ontbijtgerecht hebben we niet!")
