import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import PatientSerializer, PractionerSerializer, PatientSummarySerializer, PractionerSummarySerializer
from .models import Patient, Practioner, ICD10


class PractionerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, npi):

        try:
            practioner = Practioner.objects.get(npi=npi)
        except:
            return Response({"Error": "Practioner NPI does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PractionerSerializer(practioner)
        if serializer.is_valid:
            return Response(serializer.data)


class PractionerSummaryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        practioners = Practioner.objects.all()
        allpractioners = []

        for practioner in practioners:
            serializer = PractionerSummarySerializer(practioner)
            allpractioners.append(serializer.data)

        return Response(allpractioners)


class PatientView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        try:
            practioner = Practioner.objects.get(npi=request.data.get('npi'))
        except:
            practioner = Practioner(
                dr_firstname=request.data.get('dr_firstname'),
                dr_lastname=request.data.get('dr_lastname'),
                dr_address1=request.data.get('dr_address1'),
                dr_address2=request.data.get('dr_address2'),
                dr_city=request.data.get('dr_city'),
                dr_state=request.data.get('dr_state'),
                dr_zipcode=request.data.get('dr_zipcode'),
                dr_phone1=request.data.get('dr_phone1'),
                dr_phone2=request.data.get('dr_phone2'),
                npi=request.data.get('npi')
            )
            practioner.save()

        patient = Patient(
            firstname=request.data.get('firstname'),
            lastname=request.data.get('lastname'),
            address1=request.data.get('address1'),
            address2=request.data.get('address2'),
            city=request.data.get('city'),
            state=request.data.get('state'),
            zipcode=request.data.get('zipcode'),
            phone1=request.data.get('phone1'),
            phone2=request.data.get('phone2'),
            dob=request.data.get('dob'),
            gender=request.data.get('gender'),
            policygroup=request.data.get('policygroup'),
            policynumber=request.data.get('policynumber'),
            policyname=request.data.get('policyname'),
            policydob=request.data.get('policydob'),
            lookupnpi=request.data.get('npi')
        )

        json_str = json.dumps(request.data.get('icd10s'))
        icd10s = json.loads(json_str)

        try:
            patient.save()
            id = patient.id
            practioner.patients.add(patient)

            if icd10s:
                for item in icd10s:
                    relationship = None
                    sidefamily = None

                    if "relationship" in item:
                        relationship = item["relationship"]

                    if "sidefamily" in item:
                        sidefamily = item["sidefamily"]

                    ICD10.objects.create(
                        icd10=item["icd10"],
                        agediagnosis=item["agediagnosis"],
                        relationship=relationship,
                        sidefamily=sidefamily,
                        patient=patient
                    )

            return Response({"Patient Created": "Id: " + str(id)})
        except Exception as e:
            print(repr(e))
            return Response({"Error": "Check your post data for incorrectly formatted and required fields."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        patients = Patient.objects.all()
        allpatients = []

        for patient in patients:
            serializer = PatientSummarySerializer(patient)
            allpatients.append(serializer.data)

        return Response(allpatients)


class PatientByIdView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        try:
            patient = Patient.objects.get(id=id)
        except:
            return Response({"Error": "Patient Id does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PatientSerializer(patient)
        if serializer.is_valid:
            return Response(serializer.data)
