# views.py

from django.shortcuts import render
from django.views import View
from .models import User, Product

class ProductSelectionView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'select_product.html', {'products': products})

    def post(self, request):
        name = request.POST.get('name')
        selected_products = request.POST.getlist('products')
        user = User.objects.create(name=name)
        for product_id in selected_products:
            product = Product.objects.get(id=product_id)
            user.products.add(product)

        return render(request, 'success.html')
