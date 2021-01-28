from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserAdminCreationForm

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'

class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')

class UpdateUserView(UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
index = IndexView.as_view()