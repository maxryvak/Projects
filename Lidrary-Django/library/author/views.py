from .models import Author
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

def authors(request):
    return render(request, "author/author_page.html")


def get_all_authors(request):
    authors = Author.objects.all()
    return render(request, "author/all_authors.html", {"authors": authors})


def create_author_page(request):
    return render(request, "author/create_author.html")

def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('namee')
        surname = request.POST.get('surnamee')
        patronymic = request.POST.get('patronymice')
        author = Author(name=name, surname=surname, patronymic=patronymic)
        author.save()
        return render(request, "author/create_author.html", {"message": "Created!!!"})

def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return render(request, "author/create_author.html", {"message": "Deleted!!!"})

