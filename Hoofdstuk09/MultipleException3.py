try:
    Value1 = int(input("Typ het eerste getal: "))
    Value2 = int(input("Typ het tweede getal: "))
    Output = Value1 / Value2
except ValueError:
    print("Gebruik een heel getal!")
except KeyboardInterrupt:
    print("Je gebruikte Ctrl+C!")
except ArithmeticError:
    print("Er ontstond een ongedefinieerde rekenfout.")
except ZeroDivisionError:
    print("Delen door nul kan niet!")
else:
    print(Output)
