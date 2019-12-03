#***************  McbrideD_CSCI1470_HW9.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #9
#
# Algorithm:
#   Start
#   
#**********************************************************

temperatureStats = []

with open("TexasTemperatures.txt") as temperatureFile:
    firstLine = True
    
    for line in temperatureFile:
        if firstLine == False:
            lineparts = line.split("    ")
            
            city = lineparts[0]
            avgAnnual = lineparts[1]
            recordHigh = lineparts[2]
            recordLow = lineparts[3]
            recordHighMonth = lineparts[4]
            recordLowMonth = lineparts[5]
            recordHighSummer = lineparts[6]
            recordLowWinter = lineparts[7]
            recordHighYear = lineparts[8]
            recordLowYear = lineparts[9]

            tempDict = {
                "city" : city,
                "avgAnnual" : avgAnnual,
                "recordHigh" : recordHigh,
                "recordLow" : recordLow,
                "recordHighMonth" : recordHighMonth,
                "recordLowMonth" : recordLowMonth,
                "recordHighSummer" : recordHighSummer,
                "recordLowWinter" : recordLowWinter,
                "recordHighYear" : recordHighYear,
                "recordLowYear" : recordLowYear
            }

            temperatureStats.append(tempDict)
        else:
            firstLine = False

newTempsFile = open("modifiedTexasTemperatures.txt", "w+")

newTempsFile.write("City Name    Average Annual Temperature    Record High Temperature    Average/Record High Temp Difference\n")

for city in temperatureStats:
    cityName = city["city"]
    avgAnnual = city["avgAnnual"]    
    recordHigh = city["recordHigh"].split(" ")[0]    
    tempDiff = round(float(recordHigh) - float(avgAnnual), 1)

    newLine = cityName + "    " + avgAnnual + "    " + recordHigh + "    " + str(tempDiff) + "\n"

    newTempsFile.write(newLine)

newTempsFile.close()
