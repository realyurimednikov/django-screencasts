from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import CreateView

from users.forms import SignupForm

class SignupView(CreateView):

    form_class = SignupForm
    success_url = reverse_lazy('users:login_view')
    template_name = 'users/signup_view.html'