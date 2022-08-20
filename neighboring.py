import random
import json
from copy import deepcopy


def neighbor(solution):
    candidates = []

    for i in range(len(solution[0])):


        
        
        if len(solution[1][solution[0][i]['Examiner']][solution[0][i]['Time']]) > 1:
            candidates.append(i)
            # print(solution[0][i])

        
        
        if solution[2][solution[0][i]['Supervisor']][solution[0][i]['Time']] > 1:
            candidates.append(i)
            #print(solution[0][i])

    
        if solution[3][solution[0][i]['Room']][solution[0][i]['Time']] > 1:
            candidates.append(i)
            #print(solution[0][i])

    print(set(candidates))

