from django.contrib import admin
from patient.models import Customerprofile

@admin.register(Customerprofile)
class profile(admin.ModelAdmin):
    list_display = [
        field.name for field in Customerprofile._meta.fields
        ]

