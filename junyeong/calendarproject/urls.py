from django.contrib import admin
from django.urls import path
import calendarapp.views


urlpatterns = [
    path('', calendarapp.views.main, name='main'), 
    path('create/', calendarapp.views.create, name='create'), 
    path('read/', calendarapp.views.read, name='read'), 
    path('read/<str:date>/', calendarapp.views.read, name='read'), 
    path('read/update/<int:id>/', calendarapp.views.update, name='update'), 
    path('read/delete/<int:id>/', calendarapp.views.delete, name='delete'),
    path('admin/', admin.site.urls), 
]