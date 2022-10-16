from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import data as dt
import json
from Inputcreation import Create_input

@api_view(['POST'])
def uploadFile(request):
    if request.method == 'POST':
        upload=request.data.get('File')
        data = upload.read()
        f = open(upload.name, "wb")
        f.write(data)
        f.close()
        Create_input(upload.name,request.data.get('Dates').split(','),request.data.get('Rooms').split(','))
        return Response({'data':'done'},status=status.HTTP_200_OK)

@api_view(['POST'])
def downloadFile(request):
    if request.method == 'POST':
        f = open('Solution.json', "r")
        response = Response({'data':f},status=status.HTTP_200_OK)
        f.close()
        return response

@api_view(['POST'])
def generate(request):
    if request.method == 'POST':
        res=[]
        with open('Solution.json', 'r') as read_file:
            inputData = json.load(read_file) 
        # generate function
        for i in inputData:
            if(i.get('color')=="Red"):
                res.append(i)
        return Response(res,status=status.HTTP_200_OK)

@api_view(['POST','GET','DELETE'])
def external(request):
    if request.method == 'POST':
        with open('InputData.json', 'r') as read_file:
            inputData = json.load(read_file) 
        for i in inputData["External constraints"]:
            if i.keys()== request.data.keys():
                inputData["External constraints"][inputData["External constraints"].index(i)]=request.data
        json_object = json.dumps(inputData, indent=4)

        with open("InputData.json", "w") as outfile:
            outfile.write(json_object)
        return Response(inputData)
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        data = request.data
        inputData = dt.load_data('InputData.json')
        if data.get('Name'):
            res=[{}]*180
            for i in inputData:
                if(data.get('Name') == i['Examiner']):
                    res[i.get('Time')]=i
            return Response({'data':res},status=status.HTTP_200_OK)
        return Response({'data':inputData},status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllExternals(request):
    if request.method == 'GET':
        defense,rooms,external_constraints,supervisor_constraints,external,supervisor,ex,dates =dt.load_data('inputData.json')
        return Response({'externals':external,'dates':dates},status=status.HTTP_200_OK)

@api_view(['POST','GET','DELETE'])
def supervisor(request):
    if request.method == 'POST':
        inputData = dt.load_data('InputData.json')
        print(request)
        inputData['Supervisor constraints']
        return Response(inputData)
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        inputData = dt.load_solution('solution.json')
        data = request.data
        if data.get('Name'):
            res=[{}]*180
            for i in inputData:
                if(data.get('Name')== i['Supervisor']):
                    res[i.get('Time')]=i
            return Response({'data':res},status=status.HTTP_200_OK)
        return Response({'data':inputData},status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllSupervisors(request):
    if request.method == 'GET':
        defense,rooms,external_constraints,supervisor_constraints,external,supervisor,ex =dt.load_data('inputData.json')
        return Response({'data':supervisor},status=status.HTTP_200_OK)

@api_view(['POST','GET','DELETE'])
def student(request):
    if request.method == 'POST':
        inputData = dt.load_data('InputData.json')
        print(request)
        inputData['Student constraints']
        return Response(inputData)
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        inputData = dt.load_solution('solution.json')
        data = request.data
        if data.get('Name'):
            res=[{}]*180
            for i in inputData:
                if(data.get('Name')== i['Student']):
                    res[i.get('Time')]=i
            return Response({'data':res},status=status.HTTP_200_OK)
        return Response({'data':inputData},status=status.HTTP_200_OK)
