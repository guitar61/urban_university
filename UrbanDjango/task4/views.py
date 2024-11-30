from django.shortcuts import render

# Platform view
def platform_view(request):
    return render(request, 'fourth_task/platform.html')

# Games view
def games_view(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']  # Pass list of games
    }
    return render(request, 'fourth_task/games.html', context)

# Cart view
def cart_view(request):
    return render(request, 'fourth_task/cart.html')
