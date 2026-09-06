from django.shortcuts import render
import os
import joblib
import pandas as pd


# Get the folder where this views.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained ML model
MODEL_PATH = os.path.join(BASE_DIR, "price_model.pkl")

model = joblib.load(MODEL_PATH)


def home(request):
    return render(request, "properties/home.html")


def property_list(request):

    location = request.GET.get("location")

    properties = [
        {
            "title": "House in Kathmandu",
            "location": "Kathmandu",
            "price": "Rs. 25,000,000",
            "bedrooms": 4,
            "bathrooms": 3,
            "area": "2,500 sq.ft",
            "type": "HOUSE",
        },
        {
            "title": "Land in Lalitpur",
            "location": "Lalitpur",
            "price": "Rs. 12,000,000",
            "bedrooms": None,
            "bathrooms": None,
            "area": "1,800 sq.ft",
            "type": "LAND",
        },
        {
            "title": "Apartment in Bhaktapur",
            "location": "Bhaktapur",
            "price": "Rs. 18,500,000",
            "bedrooms": 3,
            "bathrooms": 2,
            "area": "1,600 sq.ft",
            "type": "APARTMENT",
        },
    ]

    if location:
        properties = [
            property for property in properties
            if location.lower() in property["location"].lower()
        ]

    return render(
        request,
        "properties/property_list.html",
        {"properties": properties}
    )


def property_detail(request):
    return render(request, "properties/property_detail.html")