from django.db import models 
from django.contrib.auth import get_user_model


user_type_choice= (
    ("Doctor","Doctor"),
    ("Nurse","Nurse"),
    ("Staff","Stuff")
)
gender_choice= (
    ("M","Male"),
    ("F","Femal")
)
department_choice=(
    ("general medicine","general medicine"),
    ("surgery","surgery"),
    ("dermatology","dermatology"),
    ("nurosurgery","nurosurgery"),
    ("cardiology","cardiology"),
    ("psychiatry","psychiatry"),
    ("radiology","radiology"),
    ("pediatric surgery","pediatric surgery")
)

shift_choice= (
    ("outdoor","outdoor"),
    ("emergency","emergency"),
    ("None","None")
)
time_choice=(
    ("8:00 am-8:00 pm","8:00 am-8:00 pm"),
    ("8:00 pm-8:00 am","8:00 pm-8:00 am"),
    ("9:00 am-11:00 am","9:00 am-11:00 am"),
    ("11:00 am-1:00 pm","11:00 am-1:00 pm"),
    ("2:00 pm-4:00 pm","2:00 pm-4:00 pm"),
    ("4:00 pm-6:00 pm","4:00 pm-6:00 pm"),
    ("6:00 pm-8:00 pm","6:00 pm-8:00 pm"),
    ("None","None"),

)



class profile(models.Model):
    user_type=models.CharField(max_length=10, choices=user_type_choice)
    name = models.CharField(max_length=15,blank=True,null=True)
    degree = models.CharField(max_length=15,blank=True,null=True)
    department = models.CharField(max_length=20, choices=department_choice)
    age = models.CharField(max_length=5,blank=True,null=True)
    gender = models.CharField(max_length=10, choices=gender_choice)
    blood_group = models.CharField(max_length=5,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    adress=models.TextField(blank=True,null=True)


    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
            get_user_model(), related_name='profile_created_by',
            on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
            get_user_model(), related_name='profile_updated_by',
            on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class DutySchedule(models.Model):
    id = models.OneToOneField(profile(),related_name='profile_id',primary_key=True,
    on_delete=models.CASCADE,
    )
    sunday = models.CharField(max_length=20, choices=shift_choice)
    sunday_time = models.CharField(max_length=20, choices=time_choice)
    monday = models.CharField(max_length=20, choices=shift_choice)
    monday_time = models.CharField(max_length=20, choices=time_choice)
    tuesday = models.CharField(max_length=20, choices=shift_choice)
    tuesday_time = models.CharField(max_length=20, choices=time_choice)
    wednesday = models.CharField(max_length=20, choices=shift_choice)
    wednesday_time = models.CharField(max_length=20, choices=time_choice)
    thusday = models.CharField(max_length=20, choices=shift_choice)
    thusday_time = models.CharField(max_length=20, choices=time_choice)
    friday = models.CharField(max_length=20, choices=shift_choice)
    friday_time = models.CharField(max_length=20, choices=time_choice)
    saturday = models.CharField(max_length=20, choices=shift_choice)
    saturday_time = models.CharField(max_length=20, choices=time_choice)

    def __str__(self):
        return str(self.id)



