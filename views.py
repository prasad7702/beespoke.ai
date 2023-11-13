from django.shortcuts import render 

from rest_framework import generics
from .models import User, Product, load_catalog_from_excel
from .serializers import UserSerializer, ProductSerializer
from django.http import HttpResponse

class UserProfileView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class ProductRecommendationView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

def default_view(request):
    return HttpResponse("Welcome to the Fashion App!")
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
