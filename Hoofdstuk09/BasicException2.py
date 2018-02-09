try:
   Value = int(input("Typ een getal tussen 1 en 10: "))
except:
   print("Gebruik een getal tussen 1 en 10!")
else:

   if (Value > 0) and (Value <= 10):
      print("Je typte: ", Value)
   else:
      print("De door jou getypte waarde is ongeldig!")
