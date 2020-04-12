from django.shortcuts import render
from django.http import HttpResponse

        
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, wordcard_id):
    return HttpResponse("You're looking at question %s." % wordcard_id)

def results(request, wordcard_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % wordcard_id)

def vote(request, wordcard_id):
    return HttpResponse("You're voting on question %s." % wordcard_id)