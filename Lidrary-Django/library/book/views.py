from django.shortcuts import render, redirect
from .models import Book

def all_books(request):
    books = Book.get_all()
    return render(request, "./book/all_books.html", {"books": books})


def specific_book(request, id):
    book = Book.get_by_id(book_id=id)
    return render(request, "./book/specific_book.html", {"book": book})