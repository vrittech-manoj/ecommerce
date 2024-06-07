from django.http import HttpResponse
from django.shortcuts import render
from product.models import Products

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    item_menus = ['men','women','kids']
    datas = {
        'products':Products.objects.all(),
        'item_menus':item_menus,
    }
    return render(request,'index.html',datas) 

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')
