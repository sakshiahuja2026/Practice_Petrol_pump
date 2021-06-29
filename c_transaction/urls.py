from django.urls import path
from .views import *

urlpatterns=[
        path("new/",NewCtransactionView.as_view(),name="ctransaction-new"),
        path("view/",ListCtransactionView.as_view(),name="ctransaction-view"),
        path("update/<int:pk>",UpdateCtransactionView.as_view(),name="ctransaction-update"),
        path("delete/<int:pk>",DeleteCtransactionView.as_view(),name="ctransaction-delete"),
        path("detail/<int:pk>",DetailCtransactionView.as_view(), name="ctransaction-detail"),
        path("pp/",petrol_same_date_rate,name="petrol-price"),
        path("dp/",diesel_same_date_rate,name="diesel-price")
]
