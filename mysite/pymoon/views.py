from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    return HttpResponse("Hello! This is pymoon")
