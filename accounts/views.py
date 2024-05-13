from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm


class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    success_url = reverse_lazy("escola")
    template_name = "registration/register.html"


class RegisterUserView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


# def nomefuncao(request):
#     form = UserCreationForm()
#     return render(request, "registration/register.html", {"form": form})
