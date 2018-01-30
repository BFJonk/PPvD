Formatted = "{:d}"
print(Formatted.format(7000))

Formatted = "{:,d}"
print(Formatted.format(7000))

Formatted = "{:^15,d}"
print(Formatted.format(7000))

Formatted = "{:*^15,d}"
print(Formatted.format(7000))

Formatted = "{:*^15.2f}"
print(Formatted.format(7000))

Formatted = "{:*>15X}"
print(Formatted.format(7000))

Formatted = "{:*<#15x}"
print(Formatted.format(7000))

Formatted = "Een {0} {1} en een {0} {2}."
print(Formatted.format("blauwe", "auto", "fiets"))
