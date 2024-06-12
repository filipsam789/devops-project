from django.shortcuts import render, redirect
from .forms import ProductForm
from products_app.models import Product


# Create your views here.


def index(request):
    return render(request, 'index.html')


def out_of_stock(request):
    if request.method == "POST":
        product = ProductForm(request.POST, files=request.FILES)
        if product.is_valid():
            saved_product = product.save(commit=False)
            saved_product.user = request.user
            saved_product.image = product.cleaned_data['image']
            saved_product.save()
            return redirect('/')
    else:
        product = ProductForm()
        products = Product.objects.filter(quantity=0, category__active=True)
        return render(request, 'out_of_stock.html', {"form": product, "products": products})
