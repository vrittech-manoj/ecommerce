from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact
# Create your views here.



def contact(request):
    # return HttpResponse("this is contact page")
    data= {
        'contacts':Contact.objects.all()
    }
    return render(request,'contact.html',data)

def SaveContact(request):
    # data = request.GET.items
    # email = request.GET['email'] 
    email = request.POST['email']
    first_name = request.POST['name']
    message = request.POST['message']

    Contact.objects.create(email = email,name=first_name,message=message)

    data= {
        'contacts':Contact.objects.all()
    }
    # return HttpResponse(f"Your contact has been saved {email},{first_name},{message},{}")


    return render(request,'contact.html',data)

