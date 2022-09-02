# from tkinter import SOLID
import data as dt
from tabulate import tabulate
import cost_function
import neighboring
from copy import deepcopy

max_generations = 75000
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
            fti=[]
            fti = ft[0] + ft[1] + ft[2]
            # if the cost for the solution == 0 -> optimal solution (no violate of hard and soft constraint)
            if fti == 0:
                break
            # calculate the cost for the solution
            ftn = cost_function(new_solution)
            ftni = []
            ftni = ftn[0]+ftn[1]+ftn[2]
            # ---- if the cost for the new_solution less than or equal the cost solution
            # change the value of solution to new_solution ----
            if ftni <= fti:
                solution = new_solution
            # print the iteration number and the cost for the current solution
            if j % 10 == 0:
                print('Iteration', j, 'cost', cost_function(solution))

        print('Run', i + 1, 'cost', cost_function(solution), 'solution', solution)
        print(cost_function(solution))
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
        for day in range(12):
            temp = 0
            flag1=False
            for slot in range(15):
                time = day * 15 + slot
                if (len(solution[1][Examiner][time]) >= 1):
                    if (time - temp - 1 >= 2 and flag1):
                            continued=False
                            # print("Continouty violated")
                    flag1=True
                    temp = time

        
    print('Are hard restrictions for Examiner satisfied:', examiner_hard)
    print('Are hard restrictions for Supervisor satisfied:', supervisor_hard)
    print('Are hard restrictions for Room satisfied:', room_hard)
    print('Are hard restrictions for Continouity satisfied:', continued)
    return solution
    
f = evolutionary_algorithm()


        
# t = PrettyTable(['Saturday', 'Sunday','Monday', 'Tuesday','Wednesday', 'Thursday''Saturday', 'Sunday','Monday', 'Tuesday','Wednesday', 'Thursday'])
# t.add_row(['Alice', 24])
# t.add_row(['Bob', 19])
# print(t)
# x1=["---------\n Slot:1 \n---------",u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14]]
# x2=["---------\n Slot:2 \n---------",u[15],u[16],u[17],u[18],u[19],u[20],u[21],u[22],u[23],u[24],u[25],u[26],u[27],u[28]]
u=[""]*180
for x in range(len(f[0])):
    u[f[0][x]['Time']] += "("+ (f[0][x]['Examiner'] +" , "+ f[0][x]['Supervisor']) +")  "
x1=["Saturday",u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14]]
x2=["Sunday",u[15],u[16],u[17],u[18],u[19],u[20],u[21],u[22],u[23],u[24],u[25],u[26],u[27],u[28],u[29]]
x3=["Monday",u[30],u[31],u[32],u[33],u[34],u[35],u[36],u[37],u[38],u[39],u[40],u[41],u[42],u[43],u[44]]
x4=["Tuesday",u[45],u[46],u[47],u[48],u[49],u[50],u[51],u[52],u[53],u[54],u[55],u[56],u[57],u[58],u[59]]
x5=["Wednesday",u[60],u[61],u[62],u[63],u[64],u[65],u[66],u[67],u[68],u[69],u[70],u[71],u[72],u[73],u[74]]
x6=["Thursday",u[75],u[76],u[77],u[78],u[79],u[80],u[81],u[82],u[83],u[84],u[85],u[86],u[87],u[88],u[89]]
x7=["Saturday",u[90],u[91],u[92],u[93],u[94],u[95],u[96],u[97],u[98],u[99],u[100],u[101],u[102],u[103],u[104]]
x8=["Sunday",u[105],u[106],u[107],u[108],u[109],u[110],u[111],u[112],u[113],u[114],u[115],u[116],u[117],u[118],u[119]]
x9=["Monday",u[120],u[121],u[122],u[123],u[124],u[125],u[126],u[127],u[128],u[129],u[130],u[131],u[132],u[133],u[134]]
x10=["Tuesday",u[135],u[136],u[137],u[138],u[139],u[140],u[141],u[142],u[143],u[144],u[145],u[146],u[147],u[148],u[149]]
x11=["Wednesday",u[150],u[151],u[152],u[153],u[154],u[155],u[156],u[157],u[158],u[159],u[160],u[161],u[162],u[163],u[164]]
x12=["Thursday",u[165],u[166],u[167],u[168],u[169],u[170],u[171],u[172],u[173],u[174],u[175],u[176],u[177],u[178],u[179]]

with open('Solution.txt', 'w') as f: 
    f.write(tabulate([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12], headers=['Slot 1', 'Slot 2','Slot 3', 'Slot 4','Slot 5', 'Slot 6','Slot 7', 'SLot 8','Slot 9', 'Slot 10','Slot 11', 'Slot 12','Slot 13','Slot 14', 'Slot 15'], tablefmt="grid"))

# "External Constraints":
#         "Omar":[],  // 17
#         "Adel":[],  // 8
#         "Layla":[]  // 8 
#         "Malak":[], // 12
#         "Samir":[], // 15
# "Supervisor Constraints":
#         "Amr Mougy":[], // 11 (Omar,Adel)
#         "Nourhan Ehab":[], // 13 (Layla,Omar)
#         "Wael Abuelsadat":[], // 16 (Samir,Malak)
#         "Mervat Abuelkheir":[], // 15   (Malak,Samir,Adel,Omar)
#         "Milad Ghantous":[] // 5 (Adel,Omar)

# 75k RUN WITH FIXED COST FUNCTION COST=0 AFTER 6040 RUNS 

# ([{'Examiner': 'Omar', 'Supervisor': 'Amr Mougy', 'Student': '40-1', 'Time': 100, 'Room': 'C2.222'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Amr Mougy', 'Student': '40-2', 'Time': 51, 'Room': 'C2.222'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Amr Mougy', 'Student': '40-3', 'Time': 58, 'Room': 'C2.222'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Amr Mougy', 'Student': '40-4', 'Time': 93, 'Room': 'C3.333'},
# {'Examiner': 'Omar', 'Supervisor': 'Amr Mougy', 'Student': '40-5', 'Time': 98, 'Room': 'C1.111'},
# {'Examiner': 'Omar', 'Supervisor': 'Amr Mougy', 'Student': '40-6', 'Time': 95, 'Room': 'C2.222'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Amr Mougy', 'Student': '40-7', 'Time': 92, 'Room': 'C3.333'},
# {'Examiner': 'Omar', 'Supervisor': 'Nourhan Ehab', 'Student': '40-21', 'Time': 90, 'Room': 'C1.111'},
# {'Examiner': 'Omar', 'Supervisor': 'Nourhan Ehab', 'Student': '40-22', 'Time': 50, 'Room': 'C3.333'},        50 51 53 54 55 57 58 
# {'Examiner': 'Omar', 'Supervisor': 'Nourhan Ehab', 'Student': '40-23', 'Time': 57, 'Room': 'C1.111'},        90 92 93 94 95 96 98 100 101 102
# {'Examiner': 'Omar', 'Supervisor': 'Nourhan Ehab', 'Student': '40-20', 'Time': 54, 'Room': 'C3.333'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Nourhan Ehab', 'Student': '40-24', 'Time': 55, 'Room': 'C2.222'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-45', 'Time': 96, 'Room': 'C2.222'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-46', 'Time': 101, 'Room': 'C2.222'},
# {'Examiner': 'Omar', 'Supervisor': 'Milad Ghantous', 'Student': '40-58', 'Time': 94, 'Room': 'C3.333'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Milad Ghantous', 'Student': '40-59', 'Time': 102, 'Room': 'C1.111'}, 
# {'Examiner': 'Omar', 'Supervisor': 'Milad Ghantous', 'Student': '40-60', 'Time': 53, 'Room': 'C1.111'}, 


# {'Examiner': 'Adel', 'Supervisor': 'Amr Mougy', 'Student': '40-8', 'Time': 78, 'Room': 'C3.333'}, 
# {'Examiner': 'Adel', 'Supervisor': 'Amr Mougy', 'Student': '40-9', 'Time': 80, 'Room': 'C1.111'}, 
# {'Examiner': 'Adel', 'Supervisor': 'Amr Mougy', 'Student': '40-10', 'Time': 168, 'Room': 'C3.333'}, 
# {'Examiner': 'Adel', 'Supervisor': 'Amr Mougy', 'Student': '40-11', 'Time': 166, 'Room': 'C1.111'}, 
# {'Examiner': 'Adel', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-54', 'Time': 77, 'Room': 'C1.111'}, 
# {'Examiner': 'Adel', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-55', 'Time': 165, 'Room': 'C3.333'},    77 78 80 
# {'Examiner': 'Adel', 'Supervisor': 'Milad Ghantous', 'Student': '40-56', 'Time': 169, 'Room': 'C2.222'},       165 166 168 169 170
# {'Examiner': 'Adel', 'Supervisor': 'Milad Ghantous', 'Student': '40-57', 'Time': 170, 'Room': 'C1.111'}, 


# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-12', 'Time': 154, 'Room': 'C2.222'}, 
# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-13', 'Time': 156, 'Room': 'C3.333'}, 
# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-14', 'Time': 159, 'Room': 'C3.333'}, 
# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-15', 'Time': 162, 'Room': 'C1.111'}, 
# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-16', 'Time': 158, 'Room': 'C2.222'},        152 154 156 158 159 160 162 164
# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-17', 'Time': 160, 'Room': 'C2.222'}, 
# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-18', 'Time': 164, 'Room': 'C2.222'}, 
# {'Examiner': 'Layla', 'Supervisor': 'Nourhan Ehab', 'Student': '40-19', 'Time': 152, 'Room': 'C1.111'}, 


# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-33', 'Time': 115, 'Room': 'C1.111'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-34', 'Time': 118, 'Room': 'C3.333'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-35', 'Time': 126, 'Room': 'C3.333'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-36', 'Time': 121, 'Room': 'C1.111'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-37', 'Time': 117, 'Room': 'C3.333'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-38', 'Time': 124, 'Room': 'C3.333'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-39', 'Time': 122, 'Room': 'C2.222'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-40', 'Time': 130, 'Room': 'C3.333'},     114 115 117 118 119 121 122 124 126 127 129 130
# {'Examiner': 'Malak', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-47', 'Time': 127, 'Room': 'C1.111'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-48', 'Time': 129, 'Room': 'C3.333'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-49', 'Time': 119, 'Room': 'C1.111'}, 
# {'Examiner': 'Malak', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-50', 'Time': 114, 'Room': 'C2.222'}, 


# {'Examiner': 'Samir', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-41', 'Time': 6, 'Room': 'C1.111'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-42', 'Time': 5, 'Room': 'C1.111'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-43', 'Time': 8, 'Room': 'C3.333'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-44', 'Time': 4, 'Room': 'C2.222'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-51', 'Time': 135, 'Room': 'C2.222'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-52', 'Time': 137, 'Room': 'C3.333'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Mervat Abuelkheir', 'Student': '40-53', 'Time': 145, 'Room': 'C1.111'},    2 3 4 5 6 7 8
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-25', 'Time': 146, 'Room': 'C1.111'},      135 137 138 139 141 143 145 146
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-26', 'Time': 141, 'Room': 'C3.333'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-27', 'Time': 7, 'Room': 'C3.333'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-28', 'Time': 143, 'Room': 'C3.333'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-29', 'Time': 3, 'Room': 'C1.111'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-30', 'Time': 2, 'Room': 'C2.222'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-31', 'Time': 139, 'Room': 'C2.222'}, 
# {'Examiner': 'Samir', 'Supervisor': 'Wael Abuelsadat', 'Student': '40-32', 'Time': 138, 'Room': 'C3.333'}]
