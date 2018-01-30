try:
    Ex = ValueError()
    Ex.strerror = "Waarde moet liggen tussen 1 en 10."
    raise Ex
except ValueError as e:
    print("ValueError-exception!", e.strerror)
