import random
import json
import math
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

    # Swap Room for the external 
    sday = (math.ceil(time/15)-1)*15
    eday = math.ceil(time/15)*15
    # check if this day doesnt break his constraint
    if(solution[4][selected_examiner][time] == 0):
        max = 0
        temp = 0
        endslot = 0
        # Find the most continous slots in the day
        for x in range(sday,eday):
            if(x % 5  == 0 and not(x % 3 == 0)) :
              continue
            if(solution[1][selected_examiner][x]==1):
                temp+=1
            else:
                if(temp>max):
                    max=temp
                    temp=0
                    endslot=x
                   
    # if exists continous slots check before them and after them for free slot
        if endslot != 0:
         if(solution[3][selected_room][endslot-max] ==0 and not (endslot-max % 5  == 0 and not(endslot-max % 3 == 0)) ):
            solution[0][i]['Time'] = endslot-max
            solution[1][selected_examiner][endslot-max].append(selected_room)
            solution[2][selected_supervisor][endslot-max] += 1
            solution[3][selected_room][endslot-max] += 1
            
         elif(solution[3][selected_room][endslot+1] ==0 and not (endslot % 5  == 0 and not(endslot % 3 == 0)) ):
            solution[0][i]['Time'] = endslot+1
            solution[1][selected_examiner][endslot+1].append(selected_room)
            solution[2][selected_supervisor][endslot+1] += 1
            solution[3][selected_room][endslot+1] += 1
         return 
    # if no continous slots exist then check next and previous slots
        if(solution[3][selected_room][time-1] ==0 and not (time-1 % 5  == 0 and not(time-1 % 3 == 0)) ):
            solution[0][i]['Time'] = time-1
            solution[1][selected_examiner][time-1].append(selected_room)
            solution[2][selected_supervisor][time-1] += 1
            solution[3][selected_room][time-1] += 1
            
        elif(solution[3][selected_room][time+1] ==0 and not (time+1 % 5  == 0 and not(time+1 % 3 == 0)) ):
            solution[0][i]['Time'] = time+1
            solution[1][selected_examiner][time+1].append(selected_room)
            solution[2][selected_supervisor][time+1] += 1
            solution[3][selected_room][time+1] += 1
    # search for highest working day for external and insert in that day if possible else find 2nd highest else randomize
    else:
        return
        


    