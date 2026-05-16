from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import OrganizationRegisterForm
from .models import Organization

def register(request):
    if request.method == 'POST':
        form = OrganizationRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('organizations:profile')
        else:
            print(form.errors.as_data())
    else:
        form = OrganizationRegisterForm()
    return render(request, 'organizations/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'organizations/profile.html')

@login_required
def oranization_logout(request):
    logout(request)
    return redirect('organizations:register')

@login_required
def delete_acc(request):
    user = request.user
    user.delete()
    return redirect('organizations:register')