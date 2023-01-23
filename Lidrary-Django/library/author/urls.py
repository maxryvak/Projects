from django.urls import path
from . import views

app_name='author'

urlpatterns = [
    path('', views.authors, name='authors_page'),
    path('all_authors/', views.get_all_authors, name="all_authors"),
    path('create_author/', views.create_author_page, name="create_author_page"),
    path('create_author/create/', views.create_author, name="create_author"),
    path('delete_author/<int:id>', views.delete_author, name="delete_author"),
]