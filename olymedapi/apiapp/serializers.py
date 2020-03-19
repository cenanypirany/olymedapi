from rest_framework import serializers
from .models import Patient, Practioner, ICD10


class ICD10Serializer(serializers.ModelSerializer):
    class Meta:
        model = ICD10
        fields = (
            'icd10',
            'agediagnosis',
            'relationship',
            'sidefamily'
        )


class PatientSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'firstname',
            'lastname',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'phone1',
            'phone2',
            'dob',
            'gender',
            'lookupnpi'
        )


class PatientSerializer(serializers.ModelSerializer):
    icd10s = ICD10Serializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = (
            'id',
            'firstname',
            'lastname',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'phone1',
            'phone2',
            'dob',
            'gender',
            'policygroup',
            'policynumber',
            'policyname',
            'policydob',
            'lookupnpi',
            'icd10s'
        )


class PractionerSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Practioner
        fields = (
            'dr_firstname',
            'dr_lastname',
            'dr_address1',
            'dr_address2',
            'dr_city',
            'dr_state',
            'dr_zipcode',
            'dr_phone1',
            'dr_phone2',
            'npi'
        )


class PractionerSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = Practioner
        fields = (
            'dr_firstname',
            'dr_lastname',
            'dr_address1',
            'dr_address2',
            'dr_city',
            'dr_state',
            'dr_zipcode',
            'dr_phone1',
            'dr_phone2',
            'npi',
            'patients'
        )
