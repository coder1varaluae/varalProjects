from django import forms
from models import Form_Name


class Form_Name(forms.Form):
    Jurisdiction = models.CharField(max_length = 200)
    Formname = models.CharField(max_length = 200)
