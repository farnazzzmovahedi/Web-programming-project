from django.contrib import admin
from django.urls import path, include
from electro_shop.views import home_page

urlpatterns = [
    path('', include('electro_shop.urls'), name='home_page'),
    path('admin/', admin.site.urls),
]
