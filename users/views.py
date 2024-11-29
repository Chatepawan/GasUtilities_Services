# users/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('/')  # Redirect to homepage after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
