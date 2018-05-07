from django.urls import path
from .views import home, secret

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('secret/', secret, name='secret'),
]
