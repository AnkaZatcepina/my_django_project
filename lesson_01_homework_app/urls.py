from django.urls import path 
from . import views 

urlpatterns = [ 
    path('my_first_django/', views.my_first_django, name='my_first_django'),    
    path('about/', views.about, name='about'),
]