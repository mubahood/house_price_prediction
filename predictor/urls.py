# predictor/urls.py

from django.urls import path
from .views import predict_price

urlpatterns = [
    path('', predict_price, name='predict_price'),
]
