from django.db import models
from django.contrib.auth import get_user_model


gender_choice= (
    ("M","Male"),
    ("F","Femal")
)

class Customerprofile(models.Model):
    name = models.CharField(max_length=15,blank=True,null=True)
    age = models.CharField(max_length=5,blank=True,null=True)
    gender = models.CharField(max_length=10, choices=gender_choice)
    blood_group = models.CharField(max_length=5,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
            get_user_model(), related_name='patient_profile_created_by',
            on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
            get_user_model(), related_name='patient_profile_updated_by',
            on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)






