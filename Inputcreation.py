import pandas as pd
import numpy as np
import json

def Create_input(name, Dates,rooms):
    df_excel = pd.read_csv('InputData.csv')
    print(len(df_excel))
    External = []
    Supervisor = []
    ID = []

    for i in range(len(df_excel)-1):
        External.append(df_excel["External Reviewer"][i])
    for i in range(len(df_excel)-1):
        Supervisor.append(df_excel["Supervisor"][i])
    for i in range(len(df_excel)-1):
        ID.append(df_excel["uniq_app_no"][i])
        
    External2=list(set(External))
    Supervisor2=list(set(Supervisor))

    dictionary = {
        "Rooms": rooms,
        "Defense": [],
        "External constraints":[],
        "Supervisor constraints":[]
    }
    dic2 ={}
    for i in range(len(External)):
        dic ={
            "Examiner":External[i],
            "Supervisor":Supervisor[i],
            "Student": ID[i]
        }
        dictionary["Defense"].append(dic)
        
    for i in range(len(External2)):
        test = {}
        test[External2[i]]=[0]*len(Dates)*15
        dictionary["External constraints"].append(test)
    for i in range(len(Supervisor2)):
        test = {}
        test[Supervisor2[i]]=[0]*len(Dates)*15
        dictionary["Supervisor constraints"].append(test)

    dictionary["dates"]=Dates
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    with open("InputData.json", "w") as outfile:
        outfile.write(json_object)
    return "InputData.json"