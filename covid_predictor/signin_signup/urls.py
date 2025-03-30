from django.urls import path
from .views import auth_page, api_signup, api_login, api_logout

urlpatterns = [
    path('', auth_page, name='auth_page'),
    path('api/signup/', api_signup, name='api_signup'),
    path('api/login/', api_login, name='api_login'),
    path('api/logout/', api_logout, name='api_logout'),
]