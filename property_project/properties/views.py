from django.shortcuts import render, get_object_or_404
from .models import Property

import os
import pickle
import numpy as np
import pandas as pd


# -----------------------------
# Load ML model and lookup data
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "price_model.pkl")
FREQ_PATH = os.path.join(BASE_DIR, "neighborhood_frequency.csv")
PPSF_PATH = os.path.join(BASE_DIR, "neighborhood_median_ppsf.csv")

with open(MODEL_PATH, "rb") as file:
    price_model = pickle.load(file)

neighborhood_frequency = pd.read_csv(
    FREQ_PATH,
    index_col=0
)

neighborhood_median_ppsf = pd.read_csv(
    PPSF_PATH,
    index_col=0
)


def home(request):
    return render(request, "properties/home.html")


def property_list(request):
    location = request.GET.get("location")

    properties = Property.objects.all().order_by("-id")

    if location:
        properties = properties.filter(
            city__icontains=location
        )

    return render(
        request,
        "properties/property_list.html",
        {"properties": properties}
    )


def property_detail(request, property_id):
    property = get_object_or_404(
        Property,
        id=property_id
    )

    return render(
        request,
        "properties/property_detail.html",
        {"property": property}
    )


def predict_price(request):

    prediction = None

    if request.method == "POST":

        city = request.POST.get("city")
        area = float(request.POST.get("area"))
        bedroom = int(request.POST.get("bedroom"))
        bathroom = int(request.POST.get("bathroom"))
        floors = int(request.POST.get("floors"))
        parking = int(request.POST.get("parking"))
        road_width = float(request.POST.get("road_width"))
        property_age = int(request.POST.get("property_age"))
        face = request.POST.get("face")
        road_type = request.POST.get("road_type")
        amenity_count = int(request.POST.get("amenity_count"))

        # Default values for neighborhood features
        neighborhood_freq = 0
        neighborhood_median_ppsf = 0

        # Create input for the trained model
        input_data = pd.DataFrame([{
            "Log_Area": np.log1p(area),
            "Bedroom": bedroom,
            "Bathroom": bathroom,
            "Floors": floors,
            "Parking": parking,
            "Road_Width_Feet": road_width,
            "Property_Age": property_age,
            "Age_Unknown": 0,
            "Amenity_Count": amenity_count,
            "Neighborhood_Freq": neighborhood_freq,
            "Neighborhood_MedianPPSF": neighborhood_median_ppsf,
            "City": city,
            "Face": face,
            "Road Type": road_type,
        }])

        # Model predicts Log_Price
        log_prediction = price_model.predict(input_data)[0]

        # Convert log price back to actual NPR
        predicted_price = np.expm1(log_prediction)

        prediction = f"{predicted_price:,.0f}"

    return render(
        request,
        "properties/prediction.html",
        {"prediction": prediction}
    )
    