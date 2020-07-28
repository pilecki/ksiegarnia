from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('coming/', views.coming_soon, name='coming'),
    path('coming/<int:product_id>/', views.coming_soon_detail, name='coming_soon_detail'),
    path('coming/add', views.add_coming_soon, name='add_coming_soon'),
    path('coming/edit/<int:product_id>/', views.edit_coming_soon, name='edit_coming_soon'),
    path('coming/delete/<int:product_id>/', views.delete_coming_soon, name='delete_coming_soon'),



]