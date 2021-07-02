import json
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .utils.numeric_entity import *;
from .utils.finite_entity import *;
@api_view(['POST'])
def finite_entity(request):
    try: 
        body = json.loads(request.body.decode('utf-8'))

        data             = json.loads(request.body.decode("utf-8"))
        values           = body.get("values")
        supported_values = body.get("supported_values")
        invalid_trigger  = body.get("invalid_trigger")
        key              = body.get("key")
        support_multiple = body.get("support_multiple")
        pick_first       = body.get("pick_first")
        validator        = Finite_Entity()
        filled, partially_filled, trigger, parameters = validator.validate_finite_values_entity(values, supported_values, invalid_trigger, key, support_multiple, pick_first)
        response = {
                    "filled" : filled,
                    "partially_filled" : partially_filled,
                    "trigger" : trigger,
                    "parameters" : parameters
                }

        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response("Internal Server Error -> " + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  
@api_view(['POST'])
def numeric_entity(request):
    try:
        body             = json.loads(request.body.decode("utf-8"))
        values           = body.get("values")
        invalid_trigger  = body.get("invalid_trigger")
        key              = body.get("key")
        support_multiple = body.get("support_multiple")
        pick_first       = body.get("pick_first")
        constraint       = body.get("constraint")
        var_name         = body.get("var_name")
        validator = Numeric_Entity()
        filled, partially_filled, trigger, parameters = validator.validate_numeric_entity(values, invalid_trigger, key, support_multiple, pick_first, constraint, var_name)
        response = {
                    "filled" : filled,
                    "partially_filled" : partially_filled,
                    "trigger" : trigger,
                    "parameters" : parameters
                }

        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response("Internal Server Error -> " + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET', 'POST'])
def index(request=None):
    return HttpResponse("Welcome, this is working.")