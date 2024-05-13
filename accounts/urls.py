from django.urls import path

from .views import EditUserView, RegisterUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("user/<int:pk>", EditUserView.as_view(), name="edituser"),
]
