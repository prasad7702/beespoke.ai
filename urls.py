# fashion_app/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import default_view

urlpatterns = [
    path('', default_view),  
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
    path('shop/', include('api.urls')), 
]
