from django.shortcuts import render

def index(request):
    """ a view to return index page """
    return render(request, 'home/index.html')