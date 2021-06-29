from django.urls import path
from .views import *
urlpatterns=[
        path("new/",NewcpaymentsView.as_view(),name="cpayment-new"),
        path("view/",ListcpaymentsView.as_view(),name="cpayment-view"),
        path("update/<int:pk>",UpdatecpaymentsView.as_view(),name="cpayment-update"),
        path("delete/<int:pk>",DeletecpaymentsView.as_view(),name="cpayment-delete"),
        path("detail/<int:pk>",DetailcpaymentsView.as_view(), name="cpayment-detail")
]
