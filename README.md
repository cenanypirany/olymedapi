# olymedapi

Rest API for patient / practitioner data developed with Django Rest Framework


## Installation

## API Endpoint Guide

[ Authentication Endpoints ]

All data sent and received in JSON format.

http://(server)/api/token [ POST ]
http://(server)/api/token/refresh [ POST ]

Keys: (username) (password)

[ Data Endpoints ]

http://(server)/api/patient [ GET , POST ]

GET Notes:

- Retrieves all patients with contact information

POST Notes:

- Post a single patient with all information
- Practioner records are posted with patient records
- Practioner will not duplicate if Practioner already exists

POST Fields (All fields required unless specified):

{
"firstname"
"lastname"
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

POST Example:
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

http://(server)/api/practioner [ GET ]

GET Notes:

- Retrieves all practioners with contact information

http://(server)/api/patient/(id) [ GET ]

GET Notes:

- Retrieves patient information including practioner NPI and icd10s

http://(server)/api/practioner/(id) [ GET ]

GET Notes:

- Retrieves practioner information including all associated patients with all information including ICD10s
