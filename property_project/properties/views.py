from django.shortcuts import render


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