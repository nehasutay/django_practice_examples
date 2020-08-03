from django.shortcuts import render

# Create your views here.
def fun1(request):

	context={
	"data1":[1,2,3,4,5],
	"data2":"",
	"data3":"Im Neha",
	"var1":"9",
	"var2":123456789,
	"var3":"nehasutay",
	"var4":['a','b','c'],
	"var5":"NEHA"
    }

	 
    
	return render(request,"if.html",context)

	
	   
	
	

	


		
