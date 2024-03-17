from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from .models import Patient,Records

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        widgets = {
            "gender": forms.RadioSelect(attrs={"class": "form-check-inline"}),
        }
        fields=(
            'full_name',
            'age',
            'phone',
            'gender',
            'address',
        )
    
class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        refered_to=forms.CharField(label='refered_to',max_length=50,required=False)
        fields=(
            'patient_cause',
            'reports',
            'treatments',
            'doctor',)