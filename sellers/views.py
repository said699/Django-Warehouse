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
            if request.POST.get('remember_me'):
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            return redirect('sellers:profile')
        else:
            print("Ошибки: ", form.errors)
    else:
        form = SellerRegisterForm()
    return render(request, 'sellers/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = SellerLoginForm(request, data=request.POST)
        if form.is_valid():
            seller = form.get_user()
            login(request, seller)
            if request.POST.get('remember_me'):
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            return redirect('sellers:profile')
        else:
            print(form.errors.as_data())
    else:
        form = SellerLoginForm()
    return render(request, 'sellers/login.html', {'form': form})

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = SellerUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('sellers:profile')
    else:
        form = SellerUpdateForm(instance=request.user)
    return render(request, 'sellers/profile_update.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'sellers/profile.html')

@login_required
def seller_logout(request):
    logout(request)
    return redirect('sellers:login')

@login_required
def delete_acc(request):
    user = request.user
    user.delete()
    return redirect('sellers:register')
