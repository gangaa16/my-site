from itertools import product
from multiprocessing import context
from pydoc import render_doc
from unicodedata import name
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render,redirect
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
@login_required
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
    if request.method=='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        p = Product(name=name,price=price,description=desc,image=image)
        p.save()
        return redirect('/myapp/products') 
    return render(request,'myapp/add_product.html')
     # p=Product(name="Samsung 32 inch moniter")

    #p.price = 36000.0
    #p.description = "This is a Samsung TV"
    #p.save()
    #return HttpResponse(p)
def update_product(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}
    if request.method=='POST':
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.description = request.POST.get('desc')

        try:
            p.image = request.FILES['upload']
        except:
            pass

        #p = Product(name=name,price=price,description=desc,image=image)
        p.save()
        return redirect('/myapp/products') 
    return render(request,'myapp/update_product.html',context=context)
    

def delete_product(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}
    if request.method=='POST':
        p.delete()
       
        return redirect('/myapp/products') 
    return render(request,'myapp/update_product.html',context=context)