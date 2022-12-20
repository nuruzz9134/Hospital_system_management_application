
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('registration.urls')),
    path('patient/',include('patient.urls')),
    path('recruiters/',include('recruiters.urls')),
    path('activities/',include('activities.urls')),
    
]
