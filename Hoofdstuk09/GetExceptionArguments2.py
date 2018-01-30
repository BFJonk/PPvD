import sys

try:
    File = open('myfile.txt')
except IOError as e:
    for Entry in dir(e):
        if (not Entry.startswith("_")):
            try:
                print(Entry, " = ", e.__getattribute__(Entry))
            except AttributeError:
                print("Attribuut ", Entry, " niet toegankelijk.")
else:
    print("Bestand probleemloos geopend.")
    File.close();
