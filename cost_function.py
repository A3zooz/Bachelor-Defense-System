import json


def cost(solution):
    examiner_cost = 0
    supervisor_cost = 0
    room_cost = 0
    examiner_empty = 0
    examiner_distinct_room = 0
    candidates = []

    #Check for hard constraints

    # for single_assignment in solution[0]:
    #     for i in range(179):
    #         for Examiner in single_assignment['Examiner']:
    #             if len(solution[1][Examiner][i]) > 1:
    #                 examiner_cost += 1
    #         for Supervisor in single_assignment['Supervisor']:
    #             if solution[2][Supervisor][i] > 1:
    #                 supervisor_cost += 1
    #         if solution[3][single_assignment['Room']][i] > 1:
    #             room_cost += 1

    #Examiner, Supervisor and Room can't be reserved more than once
    for Examiner in solution[1]:
        for i in range(179):
            if len(solution[1][Examiner][i]) > 1:
                examiner_cost += 1
    for Supervisor in solution[2]:
        for i in range(179):
            if solution[2][Supervisor][i] > 1:
                supervisor_cost += 1
    # for Room in solution[3]:
    #     for i in range(179):
    #         if solution[3][Room][i] > 1:
    #             room_cost += 1
    
    # maxmimum number of rooms*13 for day 
    # slot*number
    for slot in range(179):
        x=0
        for i in range(len(solution[0])):
            if(solution[0][i]['Time']==slot):
                x+=1
        if(x>len(solution[3])):
            room_cost += x-len(solution[3])
                
                
    for Examiner in solution[1]:
        for day in range(11):
            last_seen = 0
            found = False
            for slot in range(14):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    if not found:
                        found = True
                    else:
                        if (time - last_seen - 1) >= 2:
                            examiner_cost += (time - last_seen - 1)
                        found = False
                    last_seen = time

    # #Examiner in more than one room in a single day
    # for Examiner in solution[1]:
    #     for day in range(11):
    #         rooms = []
    #         for slot in range(14):
    #             time = day * 15 + slot
    #             if len(solution[1][Examiner][time]) >= 1:
    #                 rooms=[set(solution[1][Examiner][time])]
    #         if len(rooms) > 1:
    #             examiner_cost += len(rooms)
    for Examiner in solution[1]:
        for day in range(11):
            rooms = []
            for slot in range(14):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    rooms=[set(solution[1][Examiner][time])]
            if len(rooms) > 1:
                examiner_cost += len(rooms)

    #Examiner violated time constraints
    for Examiner in solution[1]:
        l = []
        for constrained_timing in solution[4][Examiner]:
            l.append(constrained_timing)
        for i in l:
            if len(solution[1][Examiner][i]) >= 1:
                examiner_cost += 1


    #Examiner has more than 2 days
    for Examiner in solution[1]:
        working_days = 0
        for day in range(11):
            for slot in range(14):
                time = day*15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    working_days += 1
                    break
        if working_days >= 2:
            examiner_cost += working_days



    
    return examiner_cost + supervisor_cost + room_cost


    
