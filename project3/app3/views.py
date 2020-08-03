from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	return render(request,"home.html")

def about(request):
	return render(request,"about.html")

def services(request):
	return render(request,"services.html")

def client(request):
	return render(request,"client.html")

def target(request):
	return render(request,"target.html")

def postresume(request):
	return render(request,"postresume.html")

def gallery(request):
	return render(request,"gallery.html")