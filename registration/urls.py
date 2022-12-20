from django.urls import path
from registration.views import Creatsuperuserview,UserRegistrationView,UserLoginView

urlpatterns = [
    path('superuser/',Creatsuperuserview.as_view()),
    path('register/',UserRegistrationView.as_view()),
    path('login/',UserLoginView.as_view()),
]