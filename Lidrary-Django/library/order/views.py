# Create your views here.
from .models import Order
from book.models import Book
from authentication.models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

def all_orders(request):
    orders = Order.objects.all()
    return render(request, "order/all_orders.html", {"orders": orders})

def create_order_page(request):
    return render(request, "order/create_order.html")

def create_order(request):
    print(request.POST)
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        user_id = request.POST.get('user_id')
        user = get_object_or_404(CustomUser, pk=user_id)
        end_at = request.POST.get('end_at')
        plated_end_at = request.POST.get('plated_end_at')
        order = Order(book=book, user=user, end_at=end_at, plated_end_at=plated_end_at)
        order.save()
        return render(request, "order/create_order.html", {"message": "Created!!!"})

def close_order(request, id):
    order = Order.objects.get(id=id)
    order.end_at = timezone.now()
    order.save()
    orders = Order.objects.all()
    return render(request, "order/all_orders.html", {"orders": orders})
