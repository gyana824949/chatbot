from django.contrib import admin
from django.urls import path
from app.views import chat,about,chatapi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat',chat,name='home'),
    path('about',about,name='about'),
    path('api',chatapi,name='api'),
]
