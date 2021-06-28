from django.urls import path
from .views import *
urlpatterns=[
        path("new/",NewcreditorView.as_view(),name="creditor-new"),
        path("view/",ListcreditorView.as_view(),name="creditor-view"),
        path("update/<int:pk>",UpdatecreditorView.as_view(),name="creditor-update"),
        path("delete/<int:pk>",DeletecreditorView.as_view(),name="creditor-delete"),
        path("detail/<int:pk>",DetailcreditorView.as_view(), name="creditor-detail")
]
