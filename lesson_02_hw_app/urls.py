from django.urls import path, include
from . import views 

products_by_client_patterns = [
    path('', views.get_products_by_client, name='products_by_client'), 
    path('week/', views.get_products_by_client_week, name='products_by_client_week'), 
    path('month/', views.get_products_by_client_month, name='products_by_client_month'), 
    path('year/', views.get_products_by_client_year, name='products_by_client_year'), 
    
]

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('about/', views.about, name='about'),
    path('clients/', views.get_clients, name='clients'),
    path('products/', views.get_products, name='products'),
    path('orders_by_client/<int:client_id>', views.get_orders_by_client, name='orders_by_client'), 
    path('create_order/', views.create_order, name='create_order'),
    path('add_product_to_order/', views.add_product_to_order, name='add_product_to_order'),
    path('update_product_price/<int:product_id>/<int:price>', views.update_product_price, name='update_product_price'),
    path('delete_order/<int:order_id>', views.delete_order, name='delete_order'),    
    path('products_by_client/<int:client_id>/', include(products_by_client_patterns)),
    path('update_product/<int:product_id>', views.update_product, name='update_product'),
    
]