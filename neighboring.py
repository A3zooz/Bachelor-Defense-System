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
    # if(solution[4][selected_examiner][time] == 0):
    #     max = 0
    #     temp = 0
    #     endslot = 0
    #     # Find the most continous slots in the day
    #     for x in range(sday,eday):
    #         if(x % 5  == 0 and not(x % 3 == 0)) :
    #           continue
    #         if(not(solution[1][selected_examiner][x]=="")):
    #             temp+=1
    #         else:
    #             if(temp>max):
    #                 max=temp
    #                 temp=0
    #                 endslot=x
                   
    # if exists continous slots check before them and after them for free slot
        # if endslot != 0:
        #  if(solution[3][selected_room][endslot-max] ==0 and not (endslot-max % 5  == 0 and not(endslot-max % 3 == 0)) ):
        #     solution[0][i]['Time'] = endslot-max
        #     solution[1][selected_examiner][endslot-max].append(selected_room)
        #     solution[2][selected_supervisor][endslot-max] += 1
        #     solution[3][selected_room][endslot-max] += 1
            
        #  elif(solution[3][selected_room][endslot+1] ==0 and not (endslot % 5  == 0 and not(endslot % 3 == 0)) ):
        #     solution[0][i]['Time'] = endslot+1
        #     solution[1][selected_examiner][endslot+1].append(selected_room)
        #     solution[2][selected_supervisor][endslot+1] += 1
        #     solution[3][selected_room][endslot+1] += 1
        #  return 
    # if no continous slots exist then check next and previous slots
        # if(solution[3][selected_room][time-1] ==0 and not (time-1 % 5  == 0 and not(time-1 % 3 == 0)) ):
        #     solution[0][i]['Time'] = time-1
        #     solution[1][selected_examiner][time-1].append(selected_room)
        #     solution[2][selected_supervisor][time-1] += 1
        #     solution[3][selected_room][time-1] += 1
            
        # elif(solution[3][selected_room][time+1] ==0 and not (time+1 % 5  == 0 and not(time+1 % 3 == 0)) ):
        #     solution[0][i]['Time'] = time+1
        #     solution[1][selected_examiner][time+1].append(selected_room)
        #     solution[2][selected_supervisor][time+1] += 1
        #     solution[3][selected_room][time+1] += 1
    # search for highest working day for external and insert in that day if possible else find 2nd highest else randomize
    
        # Find the day with most slots then most continous if no continous randmoize in a position that is continous
    for x in range(12):
        max = 0
        temp = 0
        mwday = 0
        for y in range(15):
            if(solution[4][selected_examiner][x*y] == 0):
             continue
            if(y % 5  == 0 and not(y % 3 == 0)) :
             continue
            if(solution[1][selected_examiner][x*y]==1):
             temp+=1  
        if( solution[6][selected_examiner] - 10 > 3): #14 and above
            if(temp>max and not(temp>=10)):
             max=temp
             temp=0
             mwday=x
        elif(solution[6][selected_examiner] > 10): # 11,12,13
            if(temp>max and not(temp >= solution[6][selected_examiner]-4) ): #7,8,9
             max=temp
             temp=0
             mwday=x
        else: # <10
            if(temp>max):
             max=temp 
             temp=0
             mwday=x
        
    max = 0
    temp = 0
    endslot = 0
    sday = mwday*15
    eday = sday + 15
    flag=True
    r = random.randint(0,14)
    while(flag):
       if(len(solution[1][selected_examiner][r])==0 and (len(solution[1][selected_examiner][r+1])==1 or len(solution[1][selected_examiner][r-1])==1) ):
           flag=False
       else:
         r  = random.randint(0,14)
    if(mwday!=0):
     r=r*mwday
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

    if endslot != 0:
        if(solution[3][selected_room][endslot-max] ==0 and not (endslot-max % 5  == 0 and not(endslot-max % 3 == 0)) ):
         solution[0][i]['Time'] = endslot-max
         solution[1][selected_examiner][endslot-max].append(selected_room)
         solution[2][selected_supervisor][endslot-max] += 1
         solution[3][selected_room][endslot-max] += 1
         return
        
        elif(solution[3][selected_room][endslot+1] ==0 and not (endslot+1 % 5  == 0 and not(endslot+1 % 3 == 0)) ):
         solution[0][i]['Time'] = endslot+1
         solution[1][selected_examiner][endslot+1].append(selected_room)
         solution[2][selected_supervisor][endslot+1] += 1
         solution[3][selected_room][endslot+1] += 1 
         return
    else:
        if(solution[3][selected_room][r] ==0 and not (r% 5  == 0 and not(r % 3 == 0)) ):
         solution[0][i]['Time'] = r
         solution[1][selected_examiner][r].append(selected_room)
         solution[2][selected_supervisor][r] += 1
         solution[3][selected_room][r] += 1
         return
        


    