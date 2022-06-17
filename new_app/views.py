from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("_____HI____")


def index(request):
    return HttpResponse("User")


def page(request):
    return HttpResponse("Third page")


def fb(request):
    return HttpResponse("No link")


def main(request):
    return render(request, 'index.html')
