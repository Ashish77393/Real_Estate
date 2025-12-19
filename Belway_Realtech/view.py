from django.shortcuts import render,redirect
from Contact.models import ContactInquiry
from footer.models import media
import joblib
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
    predicted_price = None   # ✅ initialize

    if request.method == "POST":   # ✅ uppercase POST
        location = request.POST.get("location")
        area_sqft = float(request.POST.get("area_sqft"))
        bedrooms = int(request.POST.get("bedrooms"))
        bathrooms = int(request.POST.get("bathrooms"))
        balcony = int(request.POST.get("balcony"))
        parking = int(request.POST.get("parking"))
        age_of_property = int(request.POST.get("age_of_property"))
        floor = int(request.POST.get("floor"))
        total_floors = int(request.POST.get("total_floors"))
        near_school_km = float(request.POST.get("near_school_km"))
        near_hospital_km = float(request.POST.get("near_hospital_km"))
        furnished = request.POST.get("furnished")

        # Load encoders & model
        location_encoder = joblib.load("location_encoder.pkl")
        furnished_encoder = joblib.load("furnished_encoder.pkl")
        model = joblib.load("Real_state_price_model.pkl")

        # Encode categorical features
        location_encoded = location_encoder.transform([location])[0]
        furnished_encoded = furnished_encoder.transform([furnished])[0]

        # Prepare input data
        input_data = [[
            location_encoded,
            area_sqft,
            bedrooms,
            bathrooms,
            balcony,
            parking,
            age_of_property,
            floor,
            total_floors,
            near_school_km,
            near_hospital_km,
            furnished_encoded
        ]]
        print(input_data[0])
        # Predict
        predicted_price = model.predict(input_data)[0]
        print("price is :",predicted_price)
        return render(request,"prediction.html",{"Price": round(predicted_price, 2) if predicted_price else None})
    return render(
        request,
        "price_prediction.html",
    )
def prediction(request):
    return render(request,'prediction.html')