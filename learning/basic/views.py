from django.shortcuts import render

def home(request):
    dict={'key':'hello world','number':100}

    return render (request,'basico/home.html',dict)
def other (request):
    return render (request,'basico/other.html')
def relative(request):
    return render (request,'basico/relative.html')

# Create your views here.
