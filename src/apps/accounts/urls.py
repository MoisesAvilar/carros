from django.urls import path
from accounts.views import (
    register_view, login_view,
    logout_view
)

app_name = 'auth'


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
