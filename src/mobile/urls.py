from django.contrib import admin
from django.urls import path, include
from mobile.views import *

urlpatterns = [
   
    path('', ListView.as_view(), name='mobile_list'),
    path('show/<int:pk>/', MobileDetail.as_view(), name='mobile_view'),
    path('create', MobileCreate.as_view(), name='mobile_create'),
    path('delete/<int:pk>/', MobileDelete.as_view(), name='mobile_delete'),
    path('edit/<int:pk>/', MobileUpdate.as_view(), name='mobile_edit'),

    path('search', search, name='search'),
    path('search-page', index_js, name='search_mobile'),

]