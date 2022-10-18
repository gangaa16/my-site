from multiprocessing import context
from pydoc import render_doc
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Product
from django.db.models import Q 

# Create your views here.
def index(request):
    d ={
        "name" : "Arun",
        "age" : 30,
    }
    li = ["Alen","sreerag","Alwin","Allu"]
    for i in range (0,10):
        print(i)

    context = {'names':li} 
    return render(request,'myapp/index.html',context=context)
def new_one(request):
     return render(request,'listing/new-one.html')

def products(request):
    p = Product.objects.all()
    context = {'products': p}
    return render(request,'myapp/products.html',context=context)

    return HttpResponse(p)