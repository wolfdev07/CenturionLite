from django import forms
from django.contrib.auth.models import User

from Costumers.models import LessorModel


class UserLessorForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name' : 'Nombre(s)',
            'last_name': 'Apellidos',
            'email': 'Correo Electrónico',
        }


class LessorForm(forms.ModelForm):

    class Meta:
        model = LessorModel
        fields = ['curp', 'elector_key', 'birthday', 'gender', 'occupation']