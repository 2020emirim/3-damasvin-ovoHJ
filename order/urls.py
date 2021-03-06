from django.urls import path

from order import views
from order.views import OrderListView, OrderCreateView, OrderUpdateView

app_name = 'order'

urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('add/', OrderCreateView.as_view(), name='add'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.order_delete, name='delete'),
]