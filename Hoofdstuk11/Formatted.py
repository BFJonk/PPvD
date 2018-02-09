Formatted = "{:d}"
print(Formatted.format(7000))

Formatted = "{:,d}" # met 1000-seprator
print(Formatted.format(7000))

Formatted = "{:^15,d}" # Breedte 15 , gecentreed
print(Formatted.format(7000))

Formatted = "{:*^15,d}"
print(Formatted.format(7000))

Formatted = "{:*^15.2f}" # 2 getallen achter de komma - float
print(Formatted.format(7000))

Formatted = "{:*>15X}" # Hex, > achterkant
print(Formatted.format(7000))

Formatted = "{:*<#15x}" # Hex, Linkerkant <
print(Formatted.format(7000))

Formatted = "Een {0} {1} en een {0} {2}."
print(Formatted.format("blauwe", "auto", "fiets"))
