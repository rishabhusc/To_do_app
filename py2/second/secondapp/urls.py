from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.first,name='first'),
    path('delete/<List_id>', views.delete, name='delete'),
    path('crossoff/<List_id>', views.crossoff, name='crossoff'),
    path('uncrossoff/<List_id>', views.uncrossoff, name='uncrossoff'),
    path('edit/<List_id>', views.edit, name='edit'),

]
