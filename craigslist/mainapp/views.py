from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    return render(request, 'mainapp/new_search.html')