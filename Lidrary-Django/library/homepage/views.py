from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authentication.models import CustomUser


def index(request):
    return render(request, "./homepage/index.html")


def mylogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "./homepage/index.html", {"fname": f" {fname}"})
        else:
            messages.error(request, "Bad Credentials!")
            redirect("homepage:index")

    return render(request, "./homepage/login.html")


def mylogout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("homepage:index")


def all_users(request):
    all_users = CustomUser.get_all()
    return render(request, "./homepage/all_users.html", {"users": all_users})


def specific_user(request, id):
    sp_user = CustomUser.get_by_id(user_id=id)
    return render(request, "./homepage/specific_user.html", {"sp_user": sp_user})