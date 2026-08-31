from django.contrib import admin
from django.urls import path
from core.views import contador

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contador/", contador),
]