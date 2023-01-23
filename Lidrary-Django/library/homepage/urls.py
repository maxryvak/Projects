from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('users/', views.all_users, name="all_users"),
    path('users/<int:id>/', views.specific_user, name="specific_user"),
]