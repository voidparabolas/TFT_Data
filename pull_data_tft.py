from riotwatcher import LolWatcher, ApiError, TftWatcher
import pandas as pd
import json
import time

# golbal variables
api_key = '' #ADD API KEY HERE
#watcher = LolWatcher(api_key)
watcher = TftWatcher(api_key)
my_region = 'na1'

file1 = open("data.txt","w")

file2 = open("matches.txt","w")

masterMatch = []
#me = watcher.summoner.by_name(my_region, 'voidparabolus')
#print(me)

TopRatedLadderEntry = watcher.league.rated_ladders(my_region, 'RANKED_TFT_TURBO')
#print(TopRatedLadderEntry[0])
#print(TopRatedLadderEntry[1])



for z in TopRatedLadderEntry:
   #print(x)
    #get Name
    #first = TopRatedLadderEntry[0]
    name = z["summonerName"]
    #print("Type:",type(first))
    print(name)

    #Get puuid
    try:
        summ_info = watcher.summoner.by_name(my_region, name)
        print("Summner Info:", summ_info)
        puuid = summ_info["puuid"]

        print("puuid:", puuid)

    #last 20 matches
        matches = watcher.match.by_puuid(my_region, puuid,100)
    #print("Matches",matches)
        for m in matches:
            if m in masterMatch:
                print("dupe match")
            else:
                masterMatch.append(m)
                file2.write(m)
                file2.write("\n")

    except:
        print("Failed to get match ID")





    #Print a specific Match
for y in masterMatch:
    result = watcher.match.by_id(my_region, y)
    info = result["info"]
    parti = info["participants"]

    for q in parti:
        print(q["augments"], " ", q["units"]," ",q["placement"])
        file1.write(y)
        file1.write(",")
        for a in q["augments"]:        
            file1.write(a)
            file1.write(",")

        for a in q["units"]:
            file1.write(a["character_id"])
            file1.write(",")

        file1.write(str(q["placement"]))
        file1.write("\n")

file1.close()
file2.close()
