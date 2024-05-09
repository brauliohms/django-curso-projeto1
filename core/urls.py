from django.contrib import admin
from django.urls import include, path

from hello.views import helloworld, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teste/", helloworld),
    path("", home),
    path("escola/", include("escola.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
