from django.urls import path
from .import views

urlpatterns = [
    path('createCategory',views.createCategory,name='createCategory'),
    path('getProduct', views.getProducts, name="products"),
    path('getCategories', views.getCategories, name="categories"),
    path('getProduct/<str:pk>', views.singleProduct, name="singleProduct"),
    path('filterProducts', views.filterProducts, name="filterProducts"),

]