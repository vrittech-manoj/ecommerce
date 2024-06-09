from django.shortcuts import render
from product.models import Products

def products(request):
    # return HttpResponse("this is products page")
    data = {
        'products':{
            'men_products':Products.objects.all().filter(category='men'),
            'female_products':Products.objects.all().filter(category='men'),
            'kids':Products.objects.all().filter(category='men'),
        }

    }
    return render(request,'products.html',data)

def singleProduct(request):
    # return HttpResponse("this is singleProduct page")
    return render(request,'single_product.html')