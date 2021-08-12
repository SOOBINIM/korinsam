from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.korin_user_reg),
    path('login/', views.korin_user_login),
    path('logout/', views.logout),
]
