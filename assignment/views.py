from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json
from django.views.generic import View

class Api1(View):
    def post(self, request):
        return HttpResponse("This is first api - POST")
    def get(self, request):
        return HttpResponse("This is first Api - GET")

class Api2(View):
    def post(self, request):
        data = request.body
        return HttpResponse("This is second Api - POST")

    def get(self, request):
        return HttpResponse("This is second Api - GET")

class LandingPage():
    def index(request):
        return HttpResponse("This is the landing page.")
