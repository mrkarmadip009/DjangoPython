from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("home")
  # redirect after signup
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
