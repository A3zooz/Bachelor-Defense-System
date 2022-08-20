import imp
import json
import random
import cost_function
import neighboring

def load_data(path):
    with open(path, 'r') as read_file:
        data = json.load(read_file)
    external = []
    supervisor = []
    rooms = data['Rooms']
    defense = data['Defense']
    external_constraints = data['External Constraints']
    supervisor_constraints = data['Supervisor Constraints']
    for i in range(len(data['Defense'])):
        external.append(data['Defense'][i]['Examiner'])
    for i in range(len(data['Defense'])):
        supervisor.append(data['Defense'][i]['Supervisor'])


    return defense,rooms,external_constraints,supervisor_constraints,set(external),set(supervisor)

def generate_solution(defense, rooms, external, supervisor,external_constraints,supervisor_constraints):
    externals = {}
    supervisors = {}
    room = {}
    new_defense = {}
    new_data = []

    number_of_runs = 0
    number_of_rooms = len(rooms)
    for single_external in external:
        externals[single_external] = [[]*number_of_rooms for i in range(180)]
    for single_supervisor in supervisor:
        supervisors[single_supervisor] = [0]*180
    for single_room in rooms:
        room[single_room] = [0] * 180
    for single_assignment in defense:
        new_defense = single_assignment.copy()
        number = random.randrange(0,179)
        while number % 5  == 0 and not(number % 3 == 0)  :
            number = random.randrange(0,179)
        new_defense['Time'] = number
        room1 = random.choice(rooms)
        new_defense['Room'] = room1
        new_data.append(new_defense)
        
        externals[new_defense['Examiner']][number].append(room1)
        supervisors[new_defense['Supervisor']][number] += 1
        room[new_defense['Room']][number] += 1
        
        
    
    return new_data, externals, supervisors,room,external_constraints,supervisor_constraints

data = load_data('input.json')

sol = generate_solution(data[0],data[1],data[4],data[5],data[2],data[3])


print(sol[0])
neighboring.neighbor(sol)



