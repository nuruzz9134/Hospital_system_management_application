from django.urls import path

from recruiters.views import (
    ProfileCreatViews,
    DutyScheduleCreatViews,
    DutyScheduleUpdateViews,
    DoctorDetailedViews,
)


urlpatterns = [
    path('create_profile/',ProfileCreatViews.as_view()),
    path('create_dutyschedule/',DutyScheduleCreatViews.as_view()),
    path('dutyschedule_update/<int:pk>/',DutyScheduleUpdateViews.as_view()),
    path('doctor_detailed/',DoctorDetailedViews.as_view()),
]

