from django.shortcuts import render

# Create your views here.

def stackview(request):
	return render(request,"stackoverflowplus/dog.html")
