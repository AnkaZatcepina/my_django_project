from django.urls import path 
from . import views 

urlpatterns = [
    path('coin/<int:count>/', views.random_coin, name='coin'), 
    path('dice/<int:count>/', views.random_dice, name='dice'), 
    path('hundred/<int:count>/', views.random_hundred, name='hundred'), 
    path('choice_game/', views.choice_game_form, name='choice'), 
]