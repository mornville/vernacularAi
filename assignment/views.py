import json
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

ATTRIBUTES = ['values', 'supported_values', 'invalid_trigger', 'key', 'support_multiple', 'pick_first']
RESPONSE = ['filled', 'partially_filled', 'trigger', 'parameters']

@api_view(['POST'])
def finite_entity(request):
    body = json.loads(request.body.decode('utf-8'))
    data = {}
    try:
        for attr in ATTRIBUTES:
            data[attr] = body.get(attr)
            if data[attr] == None:
                return Response(attr.upper() + " Not sent in body", status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response("Internal Server Error -> " + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(json.dumps(data), status=status.HTTP_200_OK)
  
@api_view(['POST'])
def numeric_entity(request):
    body = json.loads(request.body.decode('utf-8'))
    data = {}
    try:
        for attr in ATTRIBUTES:
            data[attr] = body.get(attr)
            if data[attr] == None:
                return Response(attr.upper() + " Not sent in body", status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response("Internal Server Error -> " + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(json.dumps(data), status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def index(request):
    return HttpResponse("Welcome, this is working.")