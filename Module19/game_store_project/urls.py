from django.contrib import admin
from django.urls import path, include  # Include is needed to link other apps

urlpatterns = [
    path('admin/', admin.site.urls),              # Django Admin
    path('', include('task1.urls')),              # Include task1 app URLs
]
