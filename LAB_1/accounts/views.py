# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_view(request):   # <-- function name
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # change 'home' to your home page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
