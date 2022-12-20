from django.urls import path
from patient.views import (
    ProfileCreatViews,
    ProfiletListView,
    ProfileUpdateView,
    ProfileDeleteView
)

urlpatterns = [
    path('creat_profile/',ProfileCreatViews.as_view()),
    path('profile_list/',ProfiletListView.as_view()),
    path('update_profile/<int:pk>/',ProfileUpdateView.as_view()),
    path('delete_profile/<int:pk>/',ProfileDeleteView.as_view()),
]
