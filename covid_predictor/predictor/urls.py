from django.urls import path
from .views import home,dash,acc,medical,log

urlpatterns = [
    path('', home, name='home'),
    path('dash/', dash, name='dash'),
    path('acc/', acc, name='acc'),
    path('medical/', medical, name='medical'),
    path('log/', log, name='log'),
]