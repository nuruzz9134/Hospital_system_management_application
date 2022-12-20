from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from activities.serializer import (
    ServicesRequestSerializers,
    DiagnosticReportSerializers,
    AdmitedPatitentSerializers,
    )
from activities.models import ServicesRequest,DiagnosticReport,AdmitedPatitent

from .models import (Customerprofile,
                    profile,
                    ServicesRequest,



                     )





class ServiceRequestCreatViews(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):

        ids = ServicesRequest.objects.filter(doctor=request.data['doctor'],
                                          service_type=request.data['service_type'],
                                          apointment_day=request.data['apointment_day'],
                                          service_complete = False
                                        )
        count=0
        for i in ids:
            print("seat book id: ",i)
            count+=1
            print("Seat fulfiled : ",count)
        if count<5:
            c_id = request.user.id
            if Customerprofile.objects.filter(id=c_id).exists():
                customerid = Customerprofile.objects.get(id=c_id).id
                request.data['user'] = customerid
                serializer = ServicesRequestSerializers(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg":"no available seats, try another day"})






class ServiceRequestFulfilled(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                ServicesRequest.objects.filter(id=pk,service_complete=False).update(
                                                             service_complete=True)
                return Response({"msg":"Service request fulfilled"})
        except Exception as w:
                    return Response({"msg":str(w)}, status=HTTP_400_BAD_REQUEST)





class RequestedServiceViews(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
                # search = request.query_params.get('search','')
                # filter_dict = {}

                # if search:
                #     data = ServicesRequest.objects.filter(
                #         Q(Q(service_type__icontains = search) | 
                #           Q(apointment_day__icontains = search) )&
                #         Q(**filter_dict)
                #     )

                # else:
                #     data = ServicesRequest.objects.filter(**filter_dict)
                try:
                    data = ServicesRequest.objects.filter(service_complete = False)
                    requested_data = []
                    for i in data:
                        print("all datas  >>>>  ",i.__dict__)
                        filtered_data ={}
                        filtered_data = {
                                "Name":i.user.name,
                                "Service Type":i.service_type,
                                "Doctor":i.doctor.name,
                                "Apointment Day":i.apointment_day
                            }
                        user_name = Customerprofile.objects.filter(id=i.user_id).first().name
                        filtered_data['Name'] = user_name
                        requested_data.append(filtered_data)

                    return Response({"msg":requested_data})

                except Exception as w:
                    return Response({"msg":str(w)}, status=HTTP_400_BAD_REQUEST)




class DiagnosticReportCreatViews(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                serviceid = request.data['service']
                doctorid = request.data['doctor']
                if ServicesRequest.objects.filter(id = serviceid).exists():
                    doctorid = profile.objects.get(id = doctorid).id
                request.data['doctor'] =doctorid
                serializer = DiagnosticReportSerializers(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)

        except Exception as w:
            return Response({"error msg":str(w)}, status=HTTP_400_BAD_REQUEST)





class DiagnosticReportUpdateViews(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                # serviceid = request.data['service']
                # doctorid = request.data['doctor']
                reportid = DiagnosticReport.objects.get(id = pk)
                # serviceid = Customerprofile.objects.get(id = serviceid).id
                # doctorid = profile.objects.get(id = doctorid).id
                # request.data['service'] =serviceid
                # request.data['doctor'] =doctorid
                serializer = DiagnosticReportSerializers(reportid,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)

        except Exception as w:
            return Response({"error msg":str(w)}, status=HTTP_400_BAD_REQUEST)





class DiagnosticReportViews(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            requested_data = []

            search = request.query_params.get('search','')
            filter_dict = {}
            if search:
                data = DiagnosticReport.objects.filter(
                        Q(Q(service__user__name__icontains = search))&
                        Q(**filter_dict)
                    )
            else:
                data = DiagnosticReport.objects.filter(**filter_dict)


            for i in data:
                print("all datas  >>>>  ",i.__dict__)
                filtered_data ={}
                filtered_data={
                    "Name":i.service.user.name,
                    "Service-Type":i.service.service_type,
                    "Doctor":i.doctor.name,
                    "case_summery":i.case_summery,
                    "doctors_opinion":i.doctors_opinion,
                    "medicin_provide":i.medicin_provide,
                    "medical_test":i.medical_test,
                    "reporting_date":i.reporting_date
                }
                requested_data.append(filtered_data)
            return Response(requested_data)
        except Exception as w:
            return Response({"error msg":str(w)}, status=HTTP_400_BAD_REQUEST)





class AdmitedPatientCreatViews(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            a=request.user.is_admin
            if str(a)=="True":

                patientid = request.data['patient']
                doctorid = request.data['doctor']
                if Customerprofile.objects.filter(id= patientid).exists():
                    customerid = Customerprofile.objects.get(id=patientid).id
                request.data['patient'] = customerid

                if profile.objects.filter(id= doctorid).exists():
                    doctorid = Customerprofile.objects.get(id = doctorid).id
                request.data['under_doctor'] = doctorid

                serializer = AdmitedPatitentSerializers(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)
        except Exception as w:
            return Response({"msg":str(w)}, status=HTTP_400_BAD_REQUEST) 




class AdmitedPatientUpdateViews(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                admitid = AdmitedPatitent.objects.get(id=pk)
                serializer = AdmitedPatitentSerializers(admitid,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)

                    
        except Exception as w:
            return Response({"msg":str(w)}, status=HTTP_400_BAD_REQUEST)




class ReleasePatientViews(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self,request,pk):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                id = AdmitedPatitent.objects.get(id=pk)
                id.delete()
                return Response({"msg":"Admited patient Released"})

        except Exception as w:
            return Response({"msg": str(w)}, status = HTTP_400_BAD_REQUEST)

