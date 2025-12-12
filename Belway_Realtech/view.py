from django.shortcuts import render
def Home(request):
    return render(request,"home.html")
def social_media(request):
    data=social_media.objects.first()
    print(data.facebook)
    return render(request,"footer.html",{"data":data})