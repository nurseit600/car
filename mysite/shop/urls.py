from .views import ProductViewSet
from django.urls import path

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}, name='product_list'))]