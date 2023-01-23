from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("exampleRadios")

        new_user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )
        new_user.is_active = True

        if int(role):
            new_user.role = 1

        new_user.save()
        
        return redirect('homepage:index')
    
    return render(request, "./authentication/signup.html")