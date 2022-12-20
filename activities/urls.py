from django.urls import path
from activities.views import (  ServiceRequestCreatViews,
                                ServiceRequestFulfilled,
                                RequestedServiceViews,
                                AdmitedPatientCreatViews,
                                DiagnosticReportCreatViews,
                                DiagnosticReportUpdateViews,
                                DiagnosticReportViews,
                                AdmitedPatientUpdateViews,
                                ReleasePatientViews,
                                )


urlpatterns = [
    path("service_creat/",ServiceRequestCreatViews.as_view()),
    path("requested_service/",RequestedServiceViews.as_view()),
    path("requested_service_fulfilled/<int:pk>/",ServiceRequestFulfilled.as_view()),
    path("diagnostic_report_creat/",DiagnosticReportCreatViews.as_view()),
    path("diagnostic_report_view/",DiagnosticReportViews.as_view()),
    path("diagnostic_report_update/<int:pk>/",DiagnosticReportUpdateViews.as_view()),
    path("patient_admission_creat/",AdmitedPatientCreatViews.as_view()),
    path("patient_admission_update/<int:pk>/",AdmitedPatientUpdateViews.as_view()),
    path("admited_patient_released/<int:pk>/",ReleasePatientViews.as_view()),
    
]
