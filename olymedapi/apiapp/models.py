from django.db import models


class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10, null=True)
    dob = models.DateField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    policygroup = models.CharField(max_length=30)
    policynumber = models.CharField(max_length=30)
    policyname = models.CharField(max_length=100, null=True)
    policydob = models.DateField(null=True)
    lookupnpi = models.CharField(max_length=10, null=True)


class Practioner(models.Model):
    dr_firstname = models.CharField(max_length=50)
    dr_lastname = models.CharField(max_length=50)
    dr_address1 = models.CharField(max_length=50)
    dr_address2 = models.CharField(max_length=50, null=True)
    dr_city = models.CharField(max_length=30)
    dr_state = models.CharField(max_length=2)
    dr_zipcode = models.CharField(max_length=10)
    dr_phone1 = models.CharField(max_length=10)
    dr_phone2 = models.CharField(max_length=10, null=True)
    npi = models.CharField(max_length=10, unique=True)

    patients = models.ManyToManyField(Patient, related_name='practioner')


class ICD10(models.Model):
    icd10 = models.CharField(max_length=10)
    agediagnosis = models.IntegerField()
    relationship = models.CharField(max_length=20, null=True)
    SIDE_FAMILY = (
        ('M', 'Mother'),
        ('F', 'Father')
    )
    sidefamily = models.CharField(max_length=1, null=True, choices=SIDE_FAMILY)

    patient = models.ForeignKey(
        Patient, related_name='icd10s', null=True, on_delete=models.CASCADE)
