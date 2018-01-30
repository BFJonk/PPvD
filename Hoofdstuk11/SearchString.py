SearchMe = "De appel is rood en de bes is blauw!"

print(SearchMe.find("is"))
print(SearchMe.rfind("is"))

print(SearchMe.count("is"))

print(SearchMe.startswith("De"))
print(SearchMe.endswith("De"))

print(SearchMe.replace("appel", "auto")
      .replace("bes", "fiets"))
