# from tkinter import SOLID
from importlib.resources import as_file
from operator import length_hint
import data as dt
from tabulate import tabulate
import cost_function
import neighboring
from copy import deepcopy
import Inputcreation
import Outputcreation
import json
import random

# List of all examiners in the right slots 
# Have all rooms 
# Have avaialbe rooms 
# Loop over all days
# Add each examiner with an avaialable room
# Loop over each examiner in the day and add his roomn in a hash 
# Loop over each slot and check if an extra examiner exists 
# add him in hash too
# # at the end of the day empty the hash
def Room(solution):
    examiners=[""]*180
    numberofexaminers=[""]*180
    rooms = [[solution[8]] for x in range(180)]
    availablerooms = rooms
    examinerroomdict = {}
    for x in range(len(solution[0])):
        examiners[solution[0][x]['Time']] += (solution[0][x]['Examiner']) + ","
    for x in range(len(examiners)):
        numberofexaminers[x] += examiners[x].count(',')
    for x in range(12):
        # all rooms are now empty 
        availablerooms=rooms
        # empty all dics
        examinerroomdict = {}
        for y in range(15):
            f =  examiners[x*15+y].split(",")
            for w in range(len(f)):
                if f(w) in examinerroomdict:
                    continue
                croom = random.choice(availablerooms)
                availablerooms[x*15+y].remove(croom)
                examinerroomdict[f[w]] = croom
                for u in range(len(solution[0])):
                    if(solution[0][u]["Examiner"] == f(w) and solution[0][u]["Time"] == x*15+y):
                        solution[0][u]["Room"] = croom
                for r in range(15):
                    t =  examiners[x*15+r].split(",")
                    for z in range(len(t)):                                  
                        if(t[z] == f[w]):
                            for u in range(len(solution[0])):
                                if(solution[0][u]["Examiner"] == f(w) and solution[0][u]["Time"] == x*15+r):
                                    solution[0][u]["Room"] = croom
                                    availablerooms[x*15+r].remove(croom)
                            
            # else:


def testing():
    w = [["a","b","c"] for i in range(180)]
    # room = [[w] for x in range(180)]
    room= [""]
    room[0] = "anas,ahmed,moh,"
    # room[0] += "anas,ahmed,moh,"
    f = room[0].split(',')
    x = len(f)
    del f[len(f)-1:]
    # if f[0] == "anas" :
    # 
    # return "Yayyyyyyyyyy"
    x = random.choice(w[90])

    return x


print(testing())