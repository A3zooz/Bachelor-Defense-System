import json


def cost(solution):
    examiner_cost = 0
    supervisor_cost = 0
    room_cost = 0
    examiner_empty = 0
    examiner_distinct_room = 0

    #Check for hard constraints

    for single_assignment in solution[0]:
        for i in range(179):
            for Examiner in single_assignment['Examiner']:
                if len(solution[1][single_assignment['Examiner']][i]) > 1:
                    examiner_cost += 1
            for Supervisor in single_assignment['Supervisor']:
                if solution[1][single_assignment['Supervisor']][i] > 1:
                    supervisor_cost += 1
            if solution[3][single_assignment['Room']][i] > 1:
                room_cost += 1

    for Examiner in solution[1]:
        for day in range(12):
            last_seen = 0
            found = False
            for slot in range(15):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    if not found:
                        found = True
                    else:
                        if (time - last_seen - 1) >= 2:
                            examiner_cost += (time - last_seen - 1)
                        found = False
                    last_seen = time

    for Examiner in solution[1]:
        for day in range(12):
            rooms = []
            for slot in range(15):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    rooms=[*set(solution[1][Examiner][time])]
            if len(rooms) > 1:
                examiner_cost += len(rooms)

    
    return examiner_cost + supervisor_cost + room_cost


    
