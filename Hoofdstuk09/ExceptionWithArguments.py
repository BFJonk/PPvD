import sys

try:
   File = open('myfile.txt')
except IOError as e:
    for Args in e.args:
        print(Args)
    print("Bestand wordt niet geopend!\r\n" +
          "Foutnummer: {0}\r\n".format(e.errno) +
          "Fouttekst: {0}".format(e.strerror))
else:
   print("Bestand probleemloos geopend.")
   File.close();
