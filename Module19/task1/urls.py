from django.urls import path
from . import views  # Import views from task1

urlpatterns = [
    path('platform/', views.platform_view, name='platform'),        # Home page
    path('platform/games/', views.games_view, name='games'),        # Games page
    path('platform/cart/', views.cart_view, name='cart'),           # Cart page
    path('register/', views.register_view, name='register'),  # Correct name
    path('platform/news/', views.news_view, name='news'),  # Route for the news view

]
