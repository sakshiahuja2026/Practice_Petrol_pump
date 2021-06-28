from django.urls import path
from .views import *
urlpatterns=[
        path("new/",NewRateView.as_view(),name="rate-new"),
        path("view/",ListRateView.as_view(),name="rate-view"),
        path("update/<int:pk>",UpdateRateView.as_view(),name="rate-update"),
        path("delete/<int:pk>",DeleteRateView.as_view(),name="rate-delete"),
        path("petrolprice/",petrol_same_date_rate,name="petrol-price"),
        path("dieselprice/",diesel_same_date_rate,name="diesel-price")

]
