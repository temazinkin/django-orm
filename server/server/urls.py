from django.contrib import admin
from django.urls import path

from customer_db import views

urlpatterns = [
    path('', views.show, name='show'),
    path('admin/', admin.site.urls),
]
