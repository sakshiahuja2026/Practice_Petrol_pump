from django.urls import path
from .views import *
urlpatterns=[
        path("new/",Newemp_paydetailView.as_view(),name="emp_paydetail-new"),
        path("view/",Listemp_paydetailView.as_view(),name="emp_paydetail-view"),
        path("update/<int:pk>",Updateemp_paydetailView.as_view(),name="emp_paydetail-update"),
        path("delete/<int:pk>",Deleteemp_paydetailView.as_view(),name="emp_paydetail-delete"),
        path("detail/<int:pk>",Detailemp_paydetailView.as_view(), name="emp_paydetail-detail")
]
