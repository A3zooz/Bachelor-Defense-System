from django.http import JsonResponse
from .models import Constrain
from .serializers import ConstrainSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def constrains(request):
    if(request.method == 'GET'):
        Constrains = Constrain.objects.all;
        serializer = ConstrainSerializer(Constrains, many=True)
        return JsonResponse({'constrains':serializer.data})
    else:
        Constrains = Constrain.objects.all;
        serializer = ConstrainSerializer(Constrains, many=True)
        return JsonResponse({'constrains':serializer.data})
    