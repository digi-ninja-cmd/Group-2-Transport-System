from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Shipping.urls')),
    path('shipping/', include('Shipping.urls')),
]
