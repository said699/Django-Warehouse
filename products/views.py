from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddProductForm, ExitProducts
from .models import Product

@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('sellers:profile')
        else:
            print(form.errors.as_data())
    else:
        form = AddProductForm()

    return render(request, 'products/add_prod.html', {'form': form})

@login_required
def exit_product(request):
    if request.method == 'POST':
        form = ExitProducts(request.POST)
        if form.is_valid():
            indeficator = form.cleaned_data['indeficator']
            count_exit = form.cleaned_data['count']
            product = Product.objects.get(indeficator=indeficator)
            product.count -= count_exit
            if product.count == 0:
                product.delete()
            else:
                product.save()
            return redirect('sellers:profile')
    else:
        form = ExitProducts()
    return render(request, 'products/exit_product.html', {'form': form})


@login_required
def products_list(request):
    products = Product.objects.filter(owner=request.user)
    return render(request, 'products/product_list.html', {'products': products})
    
@login_required
def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_info.html', {'product': product})
