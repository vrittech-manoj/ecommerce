from django.shortcuts import render


def products(request):
    # return HttpResponse("this is products page")
    return render(request,'products.html')

def singleProduct(request):
    # return HttpResponse("this is singleProduct page")
    return render(request,'single_product.html')