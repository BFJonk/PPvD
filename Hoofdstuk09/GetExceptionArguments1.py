import sys

try:
    File = open('myfile.txt')
except IOError as e:
    for Arg in e.args:
        print(Arg)
else:
    print("Bestand probleemloos geopend.")
    File.close();
