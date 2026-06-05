from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddProductForm
from .models import Product

@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('organizations:profile')
        else:
            print(form.errors.as_data())
    else:
        form = AddProductForm()

    return render(request, 'products/add_prod.html', {'form': form})

@login_required
def warehouse(request):
    products = Product.objects.filter(owner=request.user)
    return render(request, 'products/warehouse.html', {'products': products})

@login_required
def product_info(request, pk):
    product = Product.objects.filter(pk=pk)
    return render(request, 'products/product_info.html', {'product': product})