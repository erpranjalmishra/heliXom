from django.shortcuts import render
# Create your views here
# .

def homepage(request):
    return render(request, 'index.html')

def firstpage(request):
    return render(request, 'index.html')