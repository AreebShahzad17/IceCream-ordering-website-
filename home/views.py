from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def abc(request):
    return render(request,'index.html')

# Create your views here.
context = {
    "variable1":"hello Areeb",
    "variable2":"hello Sikandar"
}
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        order = request.POST.get('order')
        image = request.FILES['image']
        desc = request.POST.get('desc')
        contact = Contact(name=name,address=address,phone=phone,order=order,image=image,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")

    return render(request,"contact.html")

# def contact(request):
#     return HttpResponse("this is contact page")