from django.urls import path
from base.views import company_views as views



urlpatterns = [
  path('createWork/', views.createWork, name="create-work"),
  path('allWork/', views.getAllWOrk, name="all-work"),
  path('registertailor/', views.AddTailor, name="register-tailor"),
  path('registercustomer/', views.AddCustomer, name="register-customer"),
  path('tailors/', views.getTailors, name="get-tailors"),
  path('customers/', views.getCustomers),
  path('styles/', views.getStyles),
  path('stylecreate/', views.AddStyleView.as_view(), name="class-craete-style"),
  path('gettailor/<str:pk>/', views.getTailorByid, name="get tailor by id"),
  path('deletetailor/<str:pk>',views.deleteTailor, name='delete-tailor'),
  path('work/<str:pk>',views.getWorkById, name='work'),
  path('deletework/<str:pk>',views.DeleteWork, name='delete-work'),
  path('deletecustomer/<str:pk>', views.deleteCustomer),
  path('updatework/<str:pk>',views.updateWork, name='update-work'),
  path('customer/<str:pk>/', views.getCustomer),
  path('deletestyle/<str:pk>/', views.deleteStyle),
  path('styleupdate/<str:pk>/', views.AddStyleView.as_view(), name="class-update-style"),


      
]
