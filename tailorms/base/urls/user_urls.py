from django.urls import path
from base.views import user_views as views



urlpatterns = [
      path('login/',views.MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'),
       path('register/', views.registerUser, name="register-user"),
       path('profile/', views.getUserProfile, name="profile-user"),
       path("user/<str:pk>/", views.getUserById , name="user"),
       
]
