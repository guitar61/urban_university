from django.shortcuts import render

# View for the Main page
def platform_view(request):
    return render(request, 'third_task/platform.html')

# View for the Games page
def games_view(request):
    return render(request, 'third_task/games.html')

# View for the Cart page
def cart_view(request):
    return render(request, 'third_task/cart.html')
