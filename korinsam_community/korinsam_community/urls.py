from django.contrib import admin
from django.urls import path, include
from korin_user.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('korin_user/', include('korin_user.urls')),
    path('', home),
]
