from django.urls import path
from .import views

urlpatterns = [
    path('',views.Menulist.as_view(), name='home'),
]
