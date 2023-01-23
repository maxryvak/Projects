from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.all_books, name="all_books"),
    path('<int:id>/', views.specific_book, name="specific_book"),
]