from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello World welcome to my poll site</h1>")

def detail(request, question_id):
    return HttpResponse("<h2>You're looking at question %s.</h2>" % question_id)


def results(request, question_id):
    response = "<h2>You're looking at the results of question %s.</h2>"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("<h2>You're voting on question %s.</h2>" % question_id)