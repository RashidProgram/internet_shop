from django.urls import path
from .views import TovarsListView, TovarsDetailView

app_name = 'shop'

urlpatterns = [
    path('', TovarsListView.as_view(), name='list'),
    path('detail/<int:pk>', TovarsDetailView.as_view(), name='detail')
    ]
