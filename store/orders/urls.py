from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.CreateOrderView.as_view(), name='create-order'),
]