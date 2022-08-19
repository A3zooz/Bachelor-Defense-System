import random
import json
from copy import deepcopy


def neighbor(solution):
    candidates = []

    for i in range(len(solution[0])):


        
        
        if len(solution[1][solution[0][i]['Examiner']][solution[0][i]['Time']]) > 1:
            candidates.append(i)
            # print(solution[0][i])

        
        
        if solution[2][solution[0]['Supervisor'][i]][solution[0]['Time'][i]] > 1:
            candidates.append(i)
            #print(solution[0][i])

    
        if solution[3][solution[0]['Room'][i]][solution[0]['Time'][i]] > 1:
            candidates.append(i)
            #print(solution[0][i])

    print(set(candidates))
    
