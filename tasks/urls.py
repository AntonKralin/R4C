from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('add', views.add, name='add'),
    path('report', views.report, name='report'),
]
