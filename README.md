# olymedapi

Rest API developed with Django Rest Framework to maintain patient disease data (ICD10s) along with related practitioner data.

## Installation

The server must have Python 3 installed along with Pip (Python Package Index) for version 3.

Use pip to install pipenv:
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
All data is transmited [GET/POST] in JSON format.

**Authentication Endpoints**

Keys: username, password

[POST]: http://localhost:8000/api/token

[POST]: http://(server)/api/token/refresh

**Data Endpoints**

[GET]: http://localhost:8000/api/patient

- Retrieves all patients with contact information

[POST]: http://localhost:8000/api/patient

- Post a single patient with all information
- Practioner records are posted with patient records
- Practioner will not duplicate if Practioner already exists

POST Fields:

Key Name | Required?
---------|----------
firstname | YES
lastname | YES

"address1"
"address2" (not required)
"city"
"state"
"zipcode"
"phone1"
"phone2" (not required)
"dob"
"gender" ('Male' or 'Female')
"policygroup"
"policynumber"
"policyname"
"policydob"
"dr_firstname"
"dr_lastname"
"dr_address1"
"dr_address2" (not required)
"dr_city"
"dr_state"
"dr_zipcode"
"dr_phone1"
"dr_phone2" (not required)
"npi"
"icd10s": [
{
"icd10"
"agediagnosis"
"relationship" (not required)
"sidefamily" <'Mother' or 'Father'>
}
]
}

#### Post Example
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

http://(server)/api/practioner [ GET ]

GET Notes:

- Retrieves all practioners with contact information

http://(server)/api/patient/(id) [ GET ]

GET Notes:

- Retrieves patient information including practioner NPI and icd10s

http://(server)/api/practioner/(id) [ GET ]

GET Notes:

- Retrieves practioner information including all associated patients with all information including ICD10s
