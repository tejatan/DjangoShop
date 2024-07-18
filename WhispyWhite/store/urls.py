from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_view, name='store'),  # This maps the root of store/ to the store_view
    path('<slug:category_slug>/', views.store_view, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]

