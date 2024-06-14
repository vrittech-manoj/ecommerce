from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact
# Create your views here.


def MyContact(request):
    # return HttpResponse("this is contact")
    return render(request,"contact.html")

def SaveContact(request):
    print(request.POST.items)
    form_email = request.POST['email']
    form_name = request.POST['name']
    form_message = request.POST['message']
    my_image = request.FILES['image']

    Contact.objects.create(name=form_name,email=form_email,message=form_message,image=my_image)

    return HttpResponse(f"your data has saved")