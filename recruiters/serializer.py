from rest_framework.serializers import ModelSerializer
from recruiters.models import profile,DutySchedule

class ProfileSerializers(ModelSerializer):
    class Meta:
        model = profile
        fields='__all__'

class DutyScheduleSerializers(ModelSerializer):
    class Meta:
        model = DutySchedule
        fields='__all__'
