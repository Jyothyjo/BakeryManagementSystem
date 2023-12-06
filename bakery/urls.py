from django.urls import path
from . import views

# from django.contrib.auth.views import LoginView
urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/', views.product_view, name='product_view'),
    path('products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),


    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', views.customer_view, name='customer_view'),
    path('customer/create/', views.customer_create, name='customer_create'),
    path('customer/delete/<int:customer_id>/', views.customer_delete, name='customer_delete'),


    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),


    path('inventoryitems/', views.inventoryitem_list, name='inventoryitem_list'),
    path('inventoryitems/<int:item_id>/', views.inventoryitem_view, name='inventoryitem_view'),
    path('inventoryitems/create/', views.inventoryitem_create, name='inventoryitem_create'),
    path('inventoryitems/<int:item_id>/delete/', views.inventoryitem_delete, name='inventoryitem_delete'),

    path('orderitems/', views.orderitem_list, name='orderitem_list'),
    path('orderitems/<int:pk>/', views.orderitem_detail, name='orderitem_detail'),
    path('orderitems/create/', views.orderitem_create, name='orderitem_create'),
    path('orderitems/<int:pk>/update/', views.orderitem_update, name='orderitem_update'),
    path('orderitems/<int:pk>/delete/', views.orderitem_confirm_delete, name='orderitem_delete'),

    path('logout/', views.logout_view, name='logout'),
    path('', views.bakery_home, name='bakery_home'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
]
