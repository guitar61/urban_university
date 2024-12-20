from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Buyer, Game, News  # Import your models


# Home Page View
def platform_view(request):
    return render(request, 'task1/platform.html')  # Renders the home page


# Games List View
def games_view(request):
    # Fetch all Game entries from the database
    games = Game.objects.all()
    return render(request, 'task1/games.html', {'games': games})


# Cart View
def cart_view(request):
    return render(request, 'task1/cart.html')  # Renders the cart page


# Registration View
def register_view(request):
    info = {}
    if request.method == 'POST':
        # Get form data
        login = request.POST.get('login', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        age = request.POST.get('age', '').strip()

        # Validation checks
        if not login or not password1 or not password2 or not age:
            info['error'] = 'All fields must be filled.'
        elif password1 != password2:
            info['error'] = 'Passwords do not match.'
        elif not age.isdigit() or int(age) < 18:
            info['error'] = 'You must be 18 or older.'
        else:
            # Fetch all buyers and check for duplicate names
            buyers = Buyer.objects.all()
            for buyer in buyers:
                if buyer.name == login:
                    info['error'] = f"User '{login}' already exists."
                    break
            else:
                # If no duplicates, add the new user
                Buyer.objects.create(name=login, balance=0.0, age=int(age))
                info['success'] = f"Welcome, {login}! Your account has been created."

    return render(request, 'task1/registration_page.html', {'info': info})


def news_view(request):
    news_list = News.objects.all().order_by('-date')  # Fetch all news sorted by date
    items_per_page = request.GET.get('items', 5)  # Allow user to set items per page
    paginator = Paginator(news_list, items_per_page)  # Paginate with the selected number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the current page

    return render(request, 'task1/news.html', {'news': page_obj, 'items_per_page': items_per_page})