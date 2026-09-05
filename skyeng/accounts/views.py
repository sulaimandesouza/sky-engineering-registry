from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"User '{form.cleaned_data.get('username')}' created!")
            redirect('login')
        messages.error(request, "There were some problems with the information you provided.")
        return render(request, 'accounts/signup.html', {
            'form': form,
        })
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if not user:
                messages.error(request, 'A user was not found with the information you provided.')
                return render(request, 'accounts/login.html', {
                    'form': form,
                })
            auth_login(request, user)
            return redirect('dashboard')
        messages.error(request, 'There was some problems with the information you provided.')
    return render(request, 'accounts/login.html', {
        'form': form,
    })

def logout(request):
    auth_logout(request)
    return redirect('dashboard')