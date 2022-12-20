from django.db import models
from django.contrib.auth import get_user_model
from recruiters.models import profile,DutySchedule
from patient.models import Customerprofile

bed_number_choice=(
    ("A1","A1"),("B1","B1"),
    ("A2","A2"),("B2","B2"),
    ("A3","A3"),("B3","B3"),
    ("A4","A4"),("B4","B4"),
    ("A5","A5"),("B5","B5"),
    ("A6","A6"),("B6","B6"),
    ("A7","A7"),("B7","B7"),
    ("A8","A8"),("B8","B8"),
    ("A9","A9"),("B9","B9"),
    ("A10","A10"),("B10","B10"),
)

day_choice = (
    ("sunday","sunday"),
    ("monday","monday"),
    ("tuesday","tuesday"),
    ("wednesday","wednesday"),
    ("thusday","thusday"),
    ("friday","friday"),
    ("saturday","saturday"),
)

service_choice= (
    ("outdoor","outdoor"),
    ("emergency","emergency"),
    ("blood test","blood test"),
    ("urine test","urin test"),
    ("ultrasonography","ultrasonography"),
    ("pregnancy test","pregnancy test"),
    ("angiography","angiography"),
    ("echocardiography","echocardiography"),
    ("autopsy","autopsy"),
    ("biopsy","biopsy"),
    ("endoscopy","endoscopy"),
    ("chemotherapy","chemotherapy")
)

department_choice=(
    ("general medicine","general medicine"),
    ("surgery","surgery"),
    ("dermatology","dermatology"),
    ("nurosurgery","nurosurgery"),
    ("cardiology","cardiology"),
    ("psychiatry","psychiatry"),
    ("radiology","radiology"),
    ("pediatric surgery","pediatric surgery"),
    ("ICCU","ICCU"),
    ("CCU","CCU"),
    ("general","general"),
)

class ServicesRequest(models.Model):
    user = models.ForeignKey(Customerprofile,related_name='service_request_patient',
        on_delete=models.CASCADE,blank=True,null=True
        )
    service_type = models.CharField(max_length=20, choices=service_choice)
    doctor = models.ForeignKey(profile,related_name='service_request_to_doctor',
        on_delete=models.CASCADE,blank=True,null=True
        )
    apointment_day = models.CharField(max_length=20, choices=day_choice)
    service_complete = models.BooleanField(default=False)



class AdmitedPatitent(models.Model):
    patient = models.ForeignKey(Customerprofile,related_name='admited_patient',
        on_delete=models.CASCADE,blank=True,null=True
        )
    under_doctor = models.ForeignKey(profile,related_name='under_doctor',
        on_delete=models.CASCADE,blank=True,null=True
        )
    department = models.CharField(max_length=20, choices=department_choice)
    bed_number = models.CharField(max_length=5, choices=bed_number_choice)
    admission_date = models.DateField(null=True,blank=True)
    release_date= models.DateField(null=True,blank=True)
    is_released = models.BooleanField(default=False)



class DiagnosticReport(models.Model):
    service = models.ForeignKey(ServicesRequest,related_name='service_request_id',
        on_delete=models.CASCADE,blank=True,null=True
        )
    doctor = models.ForeignKey(profile,related_name='doctor_profile',
        on_delete=models.CASCADE,blank=True,null=True
        )
    case_summery = models.TextField(blank=True,null=True)
    doctors_opinion = models.TextField(blank=True,null=True)
    medicin_provide = models.TextField(blank=True,null=True)
    medical_test = models.TextField(blank=True,null=True)
    reporting_date = models.DateField(null=True,blank=True)
