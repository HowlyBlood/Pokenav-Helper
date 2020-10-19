# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:07:06 2020
@title : Quest Manager
@author: HowlyBood
"""

# -----------------------------
# INITIALISATION
# -----------------------------
import json
from pick import pick
Reward = "Reward"
stop = "Pokestop name"
Quest = "Action description"
jsonfile = "F:\Documents\Quest Manager\quetes.json"
rwd_Label = ["REWARD 1", "REWARD 2", "REWARD 3", "REWARD 4", "REWARD 5", "REWARD 6", "REWARD 7"]
types = []
quests = []
rewards = []
Type = ""
Quest = ""
typenum = 0
# -----------------------------
# JSON READING WiP
# -----------------------------


def read_type_from_json(file):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            if entry["TYPE"] not in values:
                values.append(entry["TYPE"])
    return values


def read_quests_from_json(file, Type):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            if entry["TYPE"] == Type :
                values.append(entry["ACTION"].replace("Ã©","é").replace("Ã¨","è").replace("Ã","à"))
    return values

def read_rewards_from_json(file, Type, Quest):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            if (entry["TYPE"] == Type) and (entry["ACTION"].replace("Ã©","é").replace("Ã¨","è").replace("Ã","à") == Quest) :
                for i in range(len(rwd_Label)):
                    if entry[rwd_Label[i]] != "":
                        values.append(entry[rwd_Label[i]].replace("Ã©","é").replace("Ã¨","è").replace("Ã","à"))
    return values

# -----------------------------
# USER INPUT WiP
# -----------------------------
stop = input("Quel est le nom du pokéstop ? \n")    

title = "Choisi le type de quête dans la liste ci-dessous"
types = read_type_from_json(jsonfile)
Type, typenum = pick(types, title)
quests = read_quests_from_json(jsonfile, Type)
title = "Choisi la quête dans la liste ci-dessous"
Quest, typenum = pick(quests, title)
rewards = read_rewards_from_json(jsonfile, Type, Quest)
title = "Choisi la récompense dans la liste ci-dessous"
Reward, typenum = pick(rewards, title)
# -----------------------------
# POKENAV OUTPUT
# -----------------------------
if " " not in Reward:
    print ("$q {} \"{}\" \"{}\" ".format(Reward, stop, Quest))
else:
    print ("$q \"{}\" \"{}\" \"{}\" ".format(Reward, stop, Quest))
