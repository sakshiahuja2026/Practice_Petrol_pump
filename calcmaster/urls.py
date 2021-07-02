from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewcalcmasterView.as_view(),name="calcmaster-new"),
    path("view/",ListcalcmasterView.as_view(),name="calcmaster-view"),
    path("update/<int:pk>",UpdatecalcmasterView.as_view(),name="calcmaster-update"),
    path("delete/<int:pk>",DeletecalcmasterView.as_view(),name="calcmaster-delete"),
    path("detail/<int:pk>",DetailcalcmasterView.as_view(),name="calcmaster-detail")
]
