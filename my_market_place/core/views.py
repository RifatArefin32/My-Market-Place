from django.shortcuts import render
from product.models import Product
from category.models import Category

# Create your views here.
def index(request):
    top_products = Product.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'products': top_products, 
    }
    return render(request, 'core/index.html', context=context)

def contact(request):
    return render(request, 'core/contact.html')