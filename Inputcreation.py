import pandas as pd
import numpy as np
import json


def Create_input(days,slots):
    df_excel = pd.read_csv('InputData.csv')
    # print(len(df_excel))
    External = []
    Supervisor = []
    ID = []
    Room = []
    # Dates = [""]
    # for i in range(len(df_excel)-1):
    #     Dates.append(df_excel["Defense Date"][i])
    for i in range(len(df_excel)-1):
        External.append(df_excel["External Reviewer"][i])
    for i in range(len(df_excel)-1):
        Supervisor.append(df_excel["Supervisor"][i])
    for i in range(len(df_excel)-1):
        ID.append(df_excel["uniq_app_no"][i])
    for i in range(len(df_excel)-1):
        Room.append(df_excel["Defense Location"][i])
        
    Room2=list(set(Room))
    External2=list(set(External))
    Supervisor2=list(set(Supervisor))

    dictionary = {
        "Rooms": Room2,
        "Defense": []
    }
    dic2 ={}
    for i in range(len(External)):
        dic ={
            "Examiner":External[i],
            "Supervisor":Supervisor[i],
            "Student": ID[i]
        }
        dictionary["Defense"].append(dic)
    dic2 = {}   
    for i in range(len(External2)):
        dic2[External2[i]]=[0]*slots  

    
    dic3 = {}
    for i in range(len(Supervisor2)):
        dic3[Supervisor2[i]]=[0]*slots
    dictionary = dictionary , dic2 , dic3


    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("InputData.json", "w") as outfile:
        outfile.write(json_object)
    return "InputData.json"