Colors = ["Rood", "Oranje", "Geel", "Groen", "Blauw"]

ColorSelect = ""

while str.upper(ColorSelect) != "STOP":
    ColorSelect = input("Typ een kleurnaam: ")
    if (Colors.count(ColorSelect) >= 1):
        print("De kleur staat in de lijst!")
    elif (str.upper(ColorSelect) != "STOP"):
        print("De kleur staat niet in de lijst.")
