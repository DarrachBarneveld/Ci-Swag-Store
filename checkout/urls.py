from django.urls import path
from . import views

urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),

]
