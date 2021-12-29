from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q

from mobile.models import *
from mobile.forms import *
from mobile.serializers import *


def index_js(request):
    return render(request, "mobiles/list.html")

def add_mobiles(request):

    form = MobileForm(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        print(data)
        mobile = form.save()
        form  = MobileForm()
        return redirect('mobile_list')

    else:
        form = MobileForm()
        context = {
            'form': form
        }
        return render(request, "mobiles/mobile_form.html", {'form':form})

class ListView(ListView):
    model = Mobile
    template_name = 'mobiles/index.html'
    context_object_name = 'mobiles'

class MobileDetail(generic.DetailView):
    model = Mobile
    template_name = 'mobiles/mobile_detail.html'

class MobileUpdate(SuccessMessageMixin, UpdateView): 
    model = Mobile
    template_name = 'mobiles/mobile_form.html'
    form_class = MobileForm
    success_url = reverse_lazy('mobile_list')
    success_message = "Mobile successfully updated!"

class MobileCreate(SuccessMessageMixin, CreateView): 
    model = Mobile
    template_name = 'mobiles/mobile_form.html'
    form_class = MobileForm
    success_url = reverse_lazy('mobile_list')
    success_message = "Mobile successfully created!"

class MobileDelete(SuccessMessageMixin, DeleteView):
    model = Mobile
    template_name = 'mobiles/delete.html'
    success_url = reverse_lazy('mobile_list')
    success_message = "Mobile successfully deleted!"


def search(request):
    print('hello')

    query = request.GET.get('search_text')
    print(query)
    try:
        mobiles = Mobile.objects.filter(
            Q(jan_code__contains=query) |  Q(model__icontains=query))
    except:
        mobiles = Mobile.objects.all()
 
    context={
        'search':mobiles,
        }
    print(mobiles)
    return render(request, "mobiles/search_results.html", context)


