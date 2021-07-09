"""Project_Petrol_Pump URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.views import home
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from users.views import dashboard
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name="home-page"),
    path("",LoginView.as_view(template_name='users/login.html'),name="login"),
    path("logout",LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path("rates/",include("rates.urls")),
    path("nozzel/",include("nozzel_master.urls")),
    path("employee/",include("employee_master.urls")),
    path("tank/",include("tank.urls")),
    path("creditor/",include("creditor_master.urls")),
    path("vehicle/",include("vehicle.urls")),
    path("ctransaction/",include("c_transaction.urls")),
    path("cpayment/",include("cpayment.urls")),
    path("ntransaction/",include("ntransaction.urls")),
    path("emp_paydetails/",include("emp_paydetails.urls")),
    path("supplierdetail/",include("supplierdetail.urls")),
    path("calcmaster/",include("calcmaster.urls")),
    path("dashboard/", dashboard, name="dashboard")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)