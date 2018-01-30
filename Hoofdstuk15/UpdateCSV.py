from FormattedData import FormatData
import os.path

if not os.path.isfile("Testfile.csv"):
    print("Voer het bestand CreateFile.py uit!")
    quit()

NewData = FormatData.ReadData("TestFile.csv")
for Entry in NewData:
    print(Entry)

print("\r\nEen record toevoegen voor Harry.")
NewRecord = "'Harry', 23, False"
NewData.append(NewRecord)
for Entry in NewData:
    print(Entry)

print("\r\nHet record van Daan verwijderen.")
Location = NewData.index("'Daan', 52, True")
Record = NewData[Location]
NewData.remove(Record)
for Entry in NewData:
    print(Entry)

print("\r\nHet record van Sally aanpassen.")
Location = NewData.index("'Sally', 47, False")
Record = NewData[Location]
Split = Record.split(",")
NewRecord = FormatData(Split[0].replace("'", ""),
                       int(Split[1]),
                       bool(Split[2]))
NewRecord.Married = True
NewRecord.Age = 48
NewData.append(NewRecord.__str__())
NewData.remove(Record)
for Entry in NewData:
    print(Entry)

FormatData.SaveData("ChangedFile.csv", NewData)
