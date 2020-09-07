from django.urls import path
from . import views
urlpatterns = [
    path('', views.news, name='news'),
    path('prices', views.prices, name='prices'),
    path('lookup', views.lookup, name='lookup'),
]