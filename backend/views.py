from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import data as dt

@api_view(['POST','GET','DELETE'])
def external(request):
    if request.method == 'POST':
        inputData = dt.load_data('InputData.json')
        print(request)
        inputData['Extenal constraints']
        return Response(inputData)
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        inputData = dt.load_solution('solution.json')
        data = request.data
        if data.get('Name'):
            res=[{}]*180
            for i in inputData:
                if(data.get('Name')== i['Examiner']):
                    res[i.get('Time')]=i
            return Response({'data':res},status=status.HTTP_200_OK)
        return Response({'data':inputData},status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllExternals(request):
    if request.method == 'GET':
        defense,rooms,external_constraints,supervisor_constraints,external,supervisor,ex =dt.load_data('inputData.json')
        return Response({'data':external},status=status.HTTP_200_OK)

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
