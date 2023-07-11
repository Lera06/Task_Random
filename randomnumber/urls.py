from django.urls import path
from .views import RandomNumberView, GetRandomNumberView


urlpatterns = [
    path('', RandomNumberView.as_view(), name='home'),
    path('number/', GetRandomNumberView.as_view(), name='number'),

]

