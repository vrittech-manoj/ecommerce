from django.http import HttpResponse
from django.shortcuts import render
from product.models import Products

def index(request):
    # return HttpResponse("this is home page")
    item_menus = ['men','women','kids']
    datas = {
        'products':Products.objects.all(),
        'item_menus':item_menus,
    }
    return render(request,'index.html',datas) 

def products(request):
    # return HttpResponse("this is products page")
    return render(request,'products.html')

def singleProduct(request):
    # return HttpResponse("this is singleProduct page")
    return render(request,'single_product.html')

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("this is contact page")
    return render(request,'contact.html')

