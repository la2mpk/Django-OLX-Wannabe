from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.product_list, name='product_list'),
    path('list/<slug:category_slug>', views.product_list, name='product_list_category'),
    path('details/<int:product_id>', views.product_detail, name='product_detail')
    #path('<slug:product_slug>/details', views.product_detail, name='product_detail')
]
