import json
import csv

#with open("example.json") as file:
#    data = json.load(file)

#fname = "result.csv"

#with open(fname, "w") as file:
#    csv_file = csv.writer(file,lineterminator='\n')
#    csv_file = csv.writer(file)
#    csv_file.writerow(["ID", "Name", "Email", "Faculty", "Major", "Supervisor",  "Examiner", "Defense Location", "Defense Slot"])
#    for item in data["result"]:
#        csv_file.writerow([item['id'], item['name'], item['email'], item['faculty'], item['major'], item['supervisor'], item['examiner'], item['defense location'], item['defense slot']])


# Opening JSON file and loading the data into the variable data

with open('solution.json') as json_file:
    data = json.load(json_file)
#csv_file = csv.writer(json_file,lineterminator='\n')
 
student_data = data
solution_file = open('solution_file.csv', 'w', newline="")
csv_writer = csv.writer(solution_file)
 
# Counter variable used for writing headers to the CSV file
count = 0
for emp in student_data:
    if count == 0:
 
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(emp.values())
 
solution_file.close()


#Converts list/ tuple/ dictionary to json
#import json
#data = ["DisneyPlus", "Netflix", "Peacock"]
#json_string = json.dumps(data)
#print(json_string)
