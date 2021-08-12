from django.urls import path
from . import views

urlpatterns = [
    path('stockList/', views.board_list),
]
