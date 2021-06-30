from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewsupplierdetailView.as_view(),name="supplierdetail-new"),
    path("view/",ListsupplierdetailView.as_view(),name="supplierdetail-view"),
    path("update/<int:pk>",UpdatesupplierdetailView.as_view(),name="supplierdetail-update"),
    path("delete/<int:pk>",DeletesupplierdetailView.as_view(),name="supplierdetail-delete")
]
