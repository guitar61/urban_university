from django.shortcuts import render

def shop_page(request):
    games = {
        'game1': 'Minecraft',
        'game2': 'The Witcher 3',
        'game3': 'Cyberpunk 2077',
    }
    return render(request, 'third_task/shop.html', {'games': games})
