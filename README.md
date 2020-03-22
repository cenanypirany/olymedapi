# olymedapi

Rest API developed with Django Rest Framework to maintain patient disease data (ICD10s) along with related practitioner data.

## Installation

The server must have Python 3 installed along with Pip (Python Package Index) for version 3.

Use Pip to install Pipenv:
```
pip install pipenv
```

Go to the project root directory with the 'Pipfile' and run the following command to install all the Django Rest and JWT project dependencies:
```
pipenv sync
```
Navigate to the root of Django project folder and migrate the data models:
```
cd olymedapi
python manage.py makemigrations
python manage.py migrate
```
Run script to create a Django admin super user:
```
python manage.py createsuperuser
```
Run the server:
```
python manage.py runserver
```

## API Endpoint Guide
All data is transmited (GET/POST) in JSON format.

**Authentication Endpoints**

KEYS: 'username', 'password'

POST: 
http://localhost:8000/api/token

POST: 
http://localhost:8000/api/token/refresh

**Data Endpoints**

GET: 
http://localhost:8000/api/patient

- Retrieves all patients with contact information

POST: 
http://localhost:8000/api/patient

- Post a single patient with all information
- Practioner records are posted with patient records
- Practioner will not duplicate if Practioner already exists

*POST data is refactored into three data models: Patient, Practioner, and ICD10:*

**Patient**

Key Name | Data Type | Required?
---------|-----------|----------
firstname | CharField(50) | YES
lastname | CharField(50) | YES
address1 | CharField(50) | YES
address2 | CharField(50) | NO
city | CharField(30) | YES
state | CharField(2) | YES
zipcode | CharField(10) | YES
phone1 | CharField(10) | YES
phone2 | CharField(10) | NO
dob | Date('YYYY-MM-DD') | YES
gender | CharField('Male' OR 'Female') | YES
policygroup | CharField(30) | YES
policynumber | CharField(30) | YES
policyname | CharField(100) | NO
policydob | Date('YYYY-MM-DD') | NO

**Practioner**

Key Name | Data Type | Required?
---------|-----------|----------
dr_firstname | CharField(50) | YES
dr_lastname | CharField(50) | YES
dr_address1 | CharField(50) | YES
dr_address2 | CharField(50) | NO
dr_city | CharField(30) | YES
dr_state | CharField(2) | YES
dr_zipcode | CharField(10) | YES
dr_phone1 | CharField(10) | YES
dr_phone2 | CharField(10) | NO
npi | CharField(10) | YES

**ICD10**

Key Name | Data Type | Required?
---------|-----------|----------
icd10 | CharField(10) | YES
agediagnosis | Integer | YES
relationship | CharField(20) | NO
sidefamily | CharField('Mother' OR 'Father') | NO

### Post Example

*Multiple ICD10 cases are nested into an array with the key 'ICD10s'*

```
{
  "firstname":"John",
  "lastname":"Joseph",
  "address1":"111 Lower East Side",
  "address2":"Apt 3F",
  "city":"New York",
  "state":"NY",
  "zipcode":"10001",
  "phone1":"9171231234",
  "dob":"1966-1-1",
  "gender":"Male",
  "policygroup":"Medicare",
  "policynumber":"1234567890",
  "dr_firstname":"Max",
  "dr_lastname":"Power",
  "dr_address1":"222 E 35th St",
  "dr_city":"Elmhurst",
  "dr_state":"NY",
  "dr_zipcode":"10012",
  "dr_phone1":"7182223456",
  "npi":"9879879876",
  "icd10s": [
    {
      "icd10":"Z23.123",
      "agediagnosis":"23"
    },
    {
      "icd10":"Z43.123",
      "agediagnosis":"63",
      "relationship":"Uncle",
      "sidefamily":"Mother"
    }
  ]
}
```

GET: 
http://localhost:8000/api/practioner

- Retrieves all practioners with contact information

GET:
http://localhost:8000/api/patient/(id)

- Retrieves patient information including practioner NPI and ICD10s

GET: http://localhost:8000/api/practioner/(id)

- Retrieves practioner information including all associated patients with all information including ICD10s
