from django.shortcuts import render,redirect
from Contact.models import ContactInquiry
from footer.models import media
def Home(request):
    return render(request,"home.html")
def social_media(request):
    data=media.objects.all()
    print(data)
    return render(request,"footer.html",{"data":data})

# Create your views here.
def projectData(request):
    return render(request,"Project.html")
def contact(request):
    if request.method == 'POST':
        inquiry = ContactInquiry(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message'),
        )
        inquiry.save() 
        return redirect('contact')
    return render(request, 'contact.html')

def service(request):
    return render(request,'service.html')
def price(request):
    return render(request,"price_prediction.html")