from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('register/', views.registerUser, name='register'),

    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('', views.getUsers, name="users"),

    path('<str:pk>/', views.getUserById, name='user'),

    path('update/<str:pk>/', views.updateUser, name='user-update'),

    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),

    # Address paths
    path('address/all', views.getAddress, name='address'),
    path('address/create/', views.createAddress, name='address-create'),
    path('address/update/<str:pk>/', views.updateAddress, name='address-update'),
    path('address/delete/<str:pk>/', views.deleteAddress, name='address-delete'),
    path('address/<str:pk>/', views.getAddressById, name='address-by-id'),


]