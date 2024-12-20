from django.contrib import admin
from .models import Buyer, Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Fields displayed in the list view
    list_display = ['title', 'cost', 'size', 'age_limited']

    # Enable filtering by size and cost
    list_filter = ['size', 'cost', 'age_limited']

    # Add a search bar for title
    search_fields = ['title']

    # Limit the number of records per page
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Fields displayed in the list view
    list_display = ['name', 'balance', 'age']

    # Enable filtering by balance and age
    list_filter = ['balance', 'age']

    # Add a search bar for name
    search_fields = ['name']

    # Limit the number of records per page
    list_per_page = 30

    # Make balance read-only
    readonly_fields = ['balance']
