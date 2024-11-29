from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # Django Admin route
    path('task2/', include('task2.urls')),     # Routes for task2
    path('task3/', include('task3.urls')),     # Routes for task3
]

