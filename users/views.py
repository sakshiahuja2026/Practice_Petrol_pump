from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tank.models import tank_master
from creditor_master.models import creditor
from ntransaction.models import ntransaction
# Create your views here.
@login_required
def home(request):
    return render(request,"users/home.html")
def dashboard(request):
    from datetime import datetime
    today=tank_master.objects.get(date=datetime.utcnow().date());
    petrol_stock=today.petrolafter
    diesel_stock = today.dieselafter

    from django.db.models import Sum
    data = creditor.objects.all().aggregate(Sum('pendingbalance'))
    print(data)
    data1=ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('amount'))
    print(data1)


    return render(request,"users/dashboard.html",{
        "petrol_stock":petrol_stock,
        "diesel_stock":diesel_stock,
        'pending_amount':data['pendingbalance__sum'],
        'Kamani':data1['amount__sum']

    })