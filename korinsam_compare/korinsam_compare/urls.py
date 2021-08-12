from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('korinsam/', include('stock.urls')),
    path('board/', include('board.urls')),
]
