from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h2>HEY!</h2>")
    #return render(request,template_name="index.html")
    return render(request,'FAQ/faq.html')