from itertools import product
from multiprocessing import context
from pydoc import render_doc
from unicodedata import name
from django.http import HttpResponse, HttpResponseServerError
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
     return render(request,'listing/new_one.html')

def products(request):
    p = Product.objects.all()
   # p = Product.objects.get(id=3)
    context = {'products':p}
    return render(request,'myapp/products.html',context=context)

def product_details(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}
    return render(request,'myapp/product_details.html',context=context)

def add_product(request):
    p=Product(name="Samsung 32 inch moniter")

    p.price = 36000.0
    p.description = "This is a Samsung TV"
    p.save()
    return HttpResponse(p)