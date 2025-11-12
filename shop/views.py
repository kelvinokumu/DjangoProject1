# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Product, Category
# from .forms import ProductForm, CategoryForm

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'shop/product_list.html', {'products': products})


# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'shop/product_detail.html', {'product': product})


# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('shop:product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'shop/product_form.html', {'form': form})


# def category_create(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('shop:product_list')
#     else:
#         form = CategoryForm()
#     return render(request, 'shop/category_form.html', {'form': form})

from django.shortcuts import render , get_object_or_404, redirect
from .forms import CategoryForm, ProductForm
from .models import Product, Category

def product_list(request):
    # products = Product.objects.all()
    products = Product.objects.select_related('category').order_by('-created')
    return render(request, 'shop/product_list.html', {'products': products})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:add_category')
    else:
        form = CategoryForm()
    return render(request, 'shop/add_category.html',{'form':form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:add_product')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html',{'form':form})
            

