from django.contrib import admin
from django.urls import path
from properties.views import home, property_list, property_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("properties/", property_list, name="property_list"),
    path("properties/detail/", property_detail, name="property_detail"),
]