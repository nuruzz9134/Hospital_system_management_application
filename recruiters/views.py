
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q



from recruiters.models import (
    profile,
    DutySchedule
)




from recruiters.serializer import(
    ProfileSerializers,
    DutyScheduleSerializers
)





class ProfileCreatViews(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                serializer = ProfileSerializers(data=request.data)
                if serializer.is_valid():
                    serializer.save()              
                    return Response({"msz": "Profile Creation successfully."}, status=HTTP_201_CREATED)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)
        except Exception as w:
            return Response({"msg":str(w)}, status=HTTP_400_BAD_REQUEST)





class DutyScheduleCreatViews(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            a=request.user.is_admin
            if str(a)=="True":

                serializer = DutyScheduleSerializers(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"msz": "Duty Schedule  Creation successfully."}, status=HTTP_201_CREATED)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)
        except Exception as w:
            return Response({"msg":str(w)}, status=HTTP_400_BAD_REQUEST)





class DutyScheduleUpdateViews(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                id = DutySchedule.objects.get(id=pk)
                serializer = DutyScheduleSerializers(id,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)
            else:
                return Response({"msg":"recruiter access id does not matched "})
        except Exception as w:
            return Response({"msg":str(w)}, status=HTTP_400_BAD_REQUEST)





class DoctorDetailedViews(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):

        search = request.query_params.get('search',"")
        name = request.query_params.get('name',"")
        department = request.query_params.get('department','')
        filter_dict = {}
    
        if search:
            data = DutySchedule.objects.filter(
                Q(Q(id__name__icontains=search)|
                Q(id__department__icontains=search)) &
                Q(**filter_dict)
                )
        else:
            data = DutySchedule.objects.filter(**filter_dict)

        doctors_data = []
        for j in data:
                        time_schedule = {}
                        time_schedule = {
                            "Name":j.id.name,
                            "Degrees":j.id.degree,
                            "Specialization":j.id.department,
                            "Sunday": j.sunday,
                            "Sunday Time":j.sunday_time,
                            "Monday":j.monday,
                            "Monday time":j.monday_time,
                            "Tuesday":j.tuesday,
                            "Tuesday Time":j.tuesday_time,
                            "wednesday":j.wednesday,
                            "Wednesday Time":j.wednesday_time,
                            "Thusday":j.thusday,
                            "Thusday Time":j.thusday_time,
                            "Friday":j.friday,
                            "Friday Time":j.friday_time,
                            "Saturday":j.saturday,
                            "Saturday Time":j.saturday_time
                        }
                        doctors_data.append(time_schedule)


        return Response({"msg":doctors_data})


