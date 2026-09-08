from django.contrib import admin
from django.urls import path

from properties.views import (
    home,
    property_list,
    property_detail,
    predict_price,
    undervalued_properties,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
      

    path("undervalued/", undervalued_properties, name="undervalued"),
    
    path(
        "properties/",
        property_list,
        name="property_list"
    ),

    path(
        "properties/<int:property_id>/",
        property_detail,
        name="property_detail"
    ),

    path(
        "predict/",
        predict_price,
        name="predict_price"
    ),
]