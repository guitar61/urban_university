from django.urls import path
from . import views

urlpatterns = [
    path('platform/', views.platform_view, name='platform'),  # Main platform view
    path('games/', views.games_view, name='games'),           # Games page
    path('cart/', views.cart_view, name='cart'),              # Cart page
    path('', views.platform_view, name='home'),               # Root URL
]
