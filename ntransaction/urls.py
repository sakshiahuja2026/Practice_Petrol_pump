from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewCtransactionView.as_view(),name="ntransaction-new"),
    path("view/",ListCtransactionView.as_view(),name="ntransaction-view"),
    path("update/<int:pk>",UpdateCtransactionView.as_view(),name="ntransaction-update"),
    path("delete/<int:pk>",DeleteCtransactionView.as_view(),name="ntransaction-delete"),
    path("detail/<int:pk>",DetailCtransactionView.as_view(),name="ntransaction-detail")
]