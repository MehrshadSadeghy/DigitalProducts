from django.urls import path

from .views import *

urlpatterns = [
    path('product/', AllProductsView.as_view(), name='all products'),
    path("product/<int:pk>/", ProductDetailView.as_view(), name='product detail'),
    path("category/", AllCategoriesView.as_view(), name='all categories'),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category detail"),
    path("file/<int:product_pk>/", FileListView.as_view(), name="products files"),
    path("file/<int:product_pk>/<int:file_pk>/", FileDetailView.as_view(), name="file detail")
]
