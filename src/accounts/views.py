from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        form.save()

        messages.info(request, f'Your account has been created successfully. An e-mail has been sent to confirm your registration.')
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)

def login(request):
    context = {}

    return render(request, 'accounts/login.html', context)