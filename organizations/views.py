from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SellerRegisterForm, SellerLoginForm, SellerUpdateForm

def register(request):
    if request.method == 'POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('organizations:profile')
        else:
            print("Ошибки: ", form.errors)
    else:
        form = SellerRegisterForm()
    return render(request, 'organizations/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            saller = form.get_user()
            login(request, saller)
            if request.POST.get('remember_me'):
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            return redirect('organizations:profile')
    else:
        form = SellerLoginForm()
    return render(request, 'organizations/login.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = SellerUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('organizations:profile')
    else:
        form = SellerUpdateForm(instance=request.user)
    return redirect(request, 'organizations/profile_update.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'organizations/profile.html')

@login_required
def seller_logout(request):
    logout(request)
    return redirect('organizations:login')

@login_required
def delete_acc(request):
    user = request.user
    user.delete()
    return redirect('organizations:register')