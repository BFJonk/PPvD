class CustomValueError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


try:
    raise CustomValueError("Waarde moet liggen tussen 1 en 10.")
except CustomValueError as e:
    for Entry in dir(e):
        if (not Entry.startswith("_")):
            try:
                print(Entry, " = ", e.__getattribute__(Entry))
            except AttributeError:
                print("Attribuut ", Entry, " niet toegankelijk.")
