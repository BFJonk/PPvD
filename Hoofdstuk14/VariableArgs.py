class MyClass:
    def PrintList1(*args):
        for Count, Item in enumerate(args):
            print("{0}. {1}".format(Count, Item))

    def PrintList2(**kwargs):
        for Name, Value in kwargs.items():
            print("{0} houdt van {1}".format(Name, Value))


MyClass.PrintList1("Rood", "Blauw", "Groen")
MyClass.PrintList2(Gerard="Rood", Suzan="Blauw",
                   Zarah="Groen")
