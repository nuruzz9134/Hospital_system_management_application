from rest_framework.serializers import ModelSerializer
from activities.models import ServicesRequest,AdmitedPatitent,DiagnosticReport

class ServicesRequestSerializers(ModelSerializer):
    class Meta:
        model = ServicesRequest
        fields='__all__'



class AdmitedPatitentSerializers(ModelSerializer):
    class Meta:
        model = AdmitedPatitent
        fields='__all__'



class DiagnosticReportSerializers(ModelSerializer):
    class Meta:
        model = DiagnosticReport
        fields='__all__'