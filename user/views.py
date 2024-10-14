from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned.data.get('username')
            messages.success(request, f'Accounnt created successfully for {username}.')
            return redirect(request, 'register')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', { 'form': form})

