from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
	return render(request,'index.html')

def cal(request):
	val1=int(request.POST.get("val1"))
	val2=int(request.POST.get("val2"))
	opr=request.POST.get('opr')
	sol=0
	if(opr=="+"):
		sol=val1+val2
	elif(opr=="-"):
		sol=val1-val2
	elif(opr=="*"):
		sol=val1*val2
	elif(opr=="/"):
		sol=val1/val2
	return HttpResponse(sol)




