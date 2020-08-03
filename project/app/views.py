from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def loan(request):
    return render(request,"loan.html")
 
def emi(request):
    return render(request,"emi.html")

def aboutus(request):
    return render(request,"aboutus.html")

def gallery(request):
    return render(request,"gallery.html")

def services(request):
    return render(request,"services.html")