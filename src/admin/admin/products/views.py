from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        pass



    # /api/products
    def create(self, request):
        pass
