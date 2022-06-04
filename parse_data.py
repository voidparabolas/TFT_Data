

#Dictionary Structure
#"hexTechKey_app" : int_appearances
#"hexTechKey_sum" : int sum
#"hexTechKey_first" : int total
#"hexTechKey_forth" : int forth
import time

fileRead = open("data.txt", "r")

myD = {}
myUnits = {}


for line in fileRead:
    stringList = line.split(",")
    if len(stringList) < 6:
        continue
    key0 = stringList[1]

    if key0 in myD:
        updateMe = myD[key0]
        updateMe["appears"] = updateMe["appears"] + 1

        if int(stringList[len(stringList)-1]) == 1:
            updateMe["first"] = updateMe["first"] + 1

        if int(stringList[len(stringList)-1]) >= 4:
            updateMe["top4"] = updateMe["top4"] + 1

        myD[key0] = updateMe

        if int(stringList[len(stringList)-1]) >= 4:
            heroList = myUnits[key0] #get the dict using the hextect augment as key
            for heroKey in range(4, len(stringList)-1):
                if stringList[heroKey] in heroList:
                    heroList[stringList[heroKey]] = heroList[stringList[heroKey]] + 1
                else:
                    heroList[stringList[heroKey]] = 1

            myUnits[key0] = heroList

    else:
        insertme = {"appears" : 1}
        if int(stringList[len(stringList)-1]) == 1:
            insertme["first"] = 1
        else:
            insertme["first"] = 0

        if int(stringList[len(stringList)-1]) >= 4:
            insertme["top4"] = 1
        else:
            insertme["top4"] = 0

        if int(stringList[len(stringList)-1]) >= 4:
            myD[key0] = insertme
            heroList = {}
            for heroKey in range(4, len(stringList)-1):
                heroList[stringList[heroKey]] = 1

            myUnits[key0] = heroList


sortedPos = sorted(myD.items(), key=lambda x:x[1]["top4"] / x[1]["appears"], reverse=True)
finalList = dict(sortedPos)

time.sleep(10)

for key,value in finalList.items():
    
    top4 = value["top4"] / value["appears"]
    top4 = top4 * 100

    count = value["appears"]
    first = value["first"]
    
    heroList = myUnits[key]

    sortMe = sorted(heroList.items(), key=lambda x:x[1], reverse=True)
    sortedDict = dict(sortMe)

    
#line below for printing out for excel spreadsheet
    print(key, ",",count, ",",first, ",", f'{top4:.2f}', ",", sortedDict)


for key,value in finalList.items():
    print("\"", key, end = "\"")

print("\n ")

for key,value in finalList.items():
        print("\"", key, end = "\",")

for key,value in finalList.items():
    top4 = value["top4"] / value["appears"]
    top4 = top4 * 100
    print(f'{top4:.2f}',end = ",")


fileRead.close()

