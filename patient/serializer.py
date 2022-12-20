from rest_framework.serializers import ModelSerializer
from patient.models import Customerprofile

class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Customerprofile
        fields='__all__'