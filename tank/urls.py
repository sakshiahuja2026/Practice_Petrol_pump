from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewTankView.as_view(),name="Tank-new"),
    path("view/",ListTankView.as_view(),name="Tank-view"),
    path("update/<int:pk>",UpdateTankView.as_view(),name="Tank-update"),
    path("delete/<int:pk>",DeleteTankView.as_view(),name="Tank-delete")
]
