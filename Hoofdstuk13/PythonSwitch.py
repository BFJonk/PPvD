def PrintBlue():
    print("Je koos blauw!\r\n")


def PrintRed():
    print("Je koos rood!\r\n")


def PrintOrange():
    print("Je koos oranje!\r\n")


def PrintYellow():
    print("Je koos geel!\r\n")


ColorSelect = {
    0: PrintBlue,
    1: PrintRed,
    2: PrintOrange,
    3: PrintYellow
}

Selection = 0

while (Selection != 4):
    print("0. Blauw")
    print("1. Rood")
    print("2. Oranje")
    print("3. Geel")
    print("4. Stop")

    Selection = int(input("Selecteer een kleuroptie: "))

    if (Selection >= 0) and (Selection < 4):
        ColorSelect[Selection]()
