from django.urls import path, include
from .views import PatientView, PractionerView, PractionerSummaryView, PatientByIdView

urlpatterns = [
    path('patient', PatientView.as_view()),
    path('patient/<id>', PatientByIdView.as_view()),
    path('practioner', PractionerSummaryView.as_view()),
    path('practioner/<npi>', PractionerView.as_view())
]
