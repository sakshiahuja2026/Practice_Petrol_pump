from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import rate
# Create your views here.
class NewRateView(CreateView):
    model = rate
    fields = '__all__'
#model_form.html

class ListRateView(ListView):
    model = rate
    context_object_name = 'rates'
#model_list.html
class UpdateRateView(UpdateView):
    model = rate
    fields = '__all__'

class DeleteRateView(DeleteView):
    model = rate
    success_url = '/rates/view'
#model_confirm_delete.html
class DetailRateView(DetailView):
    model = rate


