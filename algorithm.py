# from tkinter import SOLID
import data as dt
import cost_function
import neighboring
from copy import deepcopy

max_generations = 5000
num_runs = 1
input_file = 'input.json'
# output_file = 'classes/output2.json' #lesa
cost_function = cost_function.cost




def evolutionary_algorithm():
    best_timetable = None
    data = dt.load_data(input_file)
    neighbor = neighboring.neighbor  # call the neighbor function from neighboring file

    for i in range(num_runs):
        solution = dt.generate_solution(data[0],data[1],data[4],data[5],data[2],data[3],data[6])  # generate a solution by creating the first timetable by random
        for j in range(max_generations):
            # change the new solution by calling the neighbor from neighboring by getteing a deepcopy from the original chromosom
            new_solution = neighbor(deepcopy(solution))


            # calculate the cost for the solution
            ft = cost_function(solution)
            # if the cost for the solution == 0 -> optimal solution (no violate of hard and soft constraint)
            if ft == 0:
                break
            # calculate the cost for the solution
            ftn = cost_function(new_solution)
            # ---- if the cost for the new_solution less than or equal the cost solution
            # change the value of solution to new_solution ----
            if ftn <= ft:
                solution = new_solution
            # print the iteration number and the cost for the current solution
            if j % 2 == 0:
                print('Iteration', j, 'cost', cost_function(solution))

        print('Run', i + 1, 'cost', cost_function(solution), 'solution', solution)
        # Soft constraint not important yet
        # if best_timetable is None or cost_function2(solution) <= cost_function2(best_timetable):
        if best_timetable is None:
            best_timetable = deepcopy(solution)

    solution = best_timetable
    # print(solution[0])

    
    """
            Soft constraint not important yet
    """
    # for j in range(3 * max_generations):
    #     new_solution = neighbor2(deepcopy(solution))
    #     ft = cost_function2(solution)
    #     ftn = cost_function2(new_solution)
    #     if ftn <= ft:
    #         solution = new_solution
    #     if j % 200 == 0:
    #         print('Iteration', j, 'cost', cost_function2(solution))
    #
    # print('Run', 'cost', cost_function2(solution), 'solution', solution)

    #dt.write_data(solution[0], output_file)

    examiner_hard = True
    supervisor_hard = True
    room_hard = True
    continued = True

    # Check hard constraints
    # for single_class in solution[0]:
    #     if len(solution[1][solution[0][i]['Examiner']][solution[0][i]['Time']]) > 1:
    #         examiner_hard = False
    # for profesor in solution[1]:
    #     for i in range(len(solution[1][profesor])):
    #         if solution[1][profesor][i] > 1:
    #             professor_hard = False
    # for ucionica in solution[2]:
    #     for i in range(len(solution[2][ucionica])):
    #         if solution[2][ucionica][i] > 1:
    #             classroom_hard = False
    # for grupa in solution[3]:
    #     for i in range(len(solution[3][grupa])):
    #         if solution[3][grupa][i] > 1:
    #             group_hard = False
                
    for i in range(len(solution[0])):             

        
        if len(solution[1][solution[0][i]['Examiner']][solution[0][i]['Time']]) > 1:
            examiner_hard = False
            # print(solution[0][i])

        if solution[2][solution[0][i]['Supervisor']][solution[0][i]['Time']] > 1:
            supervisor_hard = False
            #print(solution[0][i])

    
        if solution[3][solution[0][i]['Room']][solution[0][i]['Time']] > 1:
            room_hard = False
            #print(solution[0][i])

        if len(solution[1][solution[0][i]['Examiner']][solution[0][i]['Time']]) >= 1 and solution[4][solution[0][i]['Examiner']][solution[0][i]['Time']] == 1:
            examiner_hard = False
        
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
                            continued = False
                        found = False
                    last_seen = time
        
    print('Are hard restrictions for professors satisfied:', examiner_hard)
    print('Are hard restrictions for classrooms satisfied:', supervisor_hard)
    print('Are hard restrictions for groups satisfied:', room_hard)
    print('Are hard restrictions for allowed classrooms satisfied:', continued)
    
    
evolutionary_algorithm()
