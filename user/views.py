from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Home page
def home_view(request):
    return render(request, "home.html")


# Login page
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Temporary redirect to home; later we’ll redirect by role
            return redirect("/")
    return render(request, "user/login.html")
