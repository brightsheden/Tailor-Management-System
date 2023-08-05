from django.urls import path
from base.views import admin_views as views

urlpatterns = [
    path('tailors/', views.get_all_tailors, name='get_all_tailors'),
    path('tailors/<int:pk>/', views.get_tailor_by_id, name='get_tailor_by_id'),
    path('tailors/add/', views.add_tailor, name='add_tailor'),
    path('tailors/<int:pk>/delete/', views.delete_tailor, name='delete_tailor'),
    path('tailors/<int:pk>/update/', views.update_tailor, name='update_tailor'),

    path('customers/', views.get_all_customers, name='get_all_tailors'),
    path('customers/<int:pk>/', views.get_customer_by_id, name='get_customer_by_id'),
    
    path('customers/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
    path('customers/<int:pk>/update/', views.update_customer, name='update_customer'),
]
