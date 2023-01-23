from django.urls import path
from . import views

app_name='authentication'

urlpatterns = [
    path('', views.signup, name="signup")
]