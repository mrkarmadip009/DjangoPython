from django.contrib import admin
from django.urls import path, include   # Import path and include
from .views import home                 # Your project-level home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),                     # Home page
    path('firstapp/', include('firstapp.urls')),  # Your firstapp URLs
    path('accounts/', include('accounts.urls')),  # Custom accounts app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
]
