from django.urls import path
from . import views

urlpatterns = [
    path('', views.platform_view, name='platform'),
    path('games/', views.games_view, name='games'),
    path('cart/', views.cart_view, name='cart'),
]
