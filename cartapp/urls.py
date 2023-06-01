from django.urls import path
from . import views
app_name='cartapp'

urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.Cart_details,name='cart_details'),

]