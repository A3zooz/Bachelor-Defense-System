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

        if len(solution[1][solution[0][i]['Examiner']][solution[0][i]['Time']]) >= 1 and solution[4][solution[0][i]['Examiner']][solution[0][i]['Time']] == 1:
            candidates.append(i)
        
        if solution[2][solution[0][i]['Supervisor']][solution[0][i]['Time']] >= 1 and solution[5][solution[0][i]['Supervisor']][solution[0][i]['Time']] == 1:
            candidates.append(i)

    if not candidates:
        i = random.randrange(len(solution[0]))
    else:
        i = random.choice(candidates)
    

    time = solution[0][i]['Time']
    selected_examiner = solution[0][i]['Examiner']
    selected_supervisor = solution[0][i]['Supervisor']
    selected_room = solution[0][i]['Room']    
    
    #Remove assignment from slot
    solution[1][selected_examiner][time].remove(selected_room)
    solution[2][selected_supervisor][time] -= 1
    solution[3][selected_room][time] -= 1

    



    