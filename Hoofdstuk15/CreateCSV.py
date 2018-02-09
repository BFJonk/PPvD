from FormattedData import FormatData

NewData = [FormatData("Gerard", 65, True),
           FormatData("Sally", 47, False),
           FormatData("Daan", 52, True)]

FormatData.SaveData("TestFile.csv", NewData)
