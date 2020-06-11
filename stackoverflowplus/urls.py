from django.urls import path
from .views import stackview

urlpatterns = [
    path('',stackview,name='home')
]