from django.shortcuts import render, redirect
from . models import Shoes
from .forms import ProductForm
# Create your views here.

def Home(request):
    shoe_data = Shoes.objects.all()
    content = {
        'data': shoe_data
    }
    return render(request,'index.html',context=content)

def signup(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a view that displays the list of products
    else:
        form = ProductForm() 

    return render(request, 'add_product.html', {'form': form})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a view that displays the list of products
    else:
        form = ProductForm() 

    return render(request, 'add_product.html', {'form': form})


def product_list(request):
    products = Shoes.objects.all()
    return render(request, 'product_list.html',context= {'products': products})