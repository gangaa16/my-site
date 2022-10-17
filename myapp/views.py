from pydoc import render_doc
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    for i in range (0,10):
        print(i)
    return render(request,'index.html')
def new_one(request):
    return HttpResponse("<b>This is new one</b>")