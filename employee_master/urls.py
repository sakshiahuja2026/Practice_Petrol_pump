from django.urls import path
from .views import *
urlpatterns=[
        path("new/",NewemployeeView.as_view(),name="employee-new"),
        path("view/",ListemployeeView.as_view(),name="employee-view"),
        path("update/<int:pk>",UpdateemployeeView.as_view(),name="employee-update"),
        path("delete/<int:pk>",DeleteemployeeView.as_view(),name="employee-delete"),        path("detail/<int:pk>",DetailemployeeView.as_view(), name="employee-detail")
]
