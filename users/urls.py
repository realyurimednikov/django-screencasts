from django.urls import path

from django.contrib.auth.views import LoginView

from users.views import SignupView

app_name = 'users'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('login/', LoginView.as_view(template_name='users/login_view.html'), name='login_view')
]