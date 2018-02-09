import sys

try:
   raise ValueError
   print("Een exception wordt opgeworpen.")
except ValueError:
   print("ValueError-exception!")
   sys.exit()
finally:
   print("De laatste dingen worden gedaan.")
   
print("Deze code wordt nooit uitgevoerd.")
