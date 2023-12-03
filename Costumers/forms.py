from django import forms
from django.contrib.auth.models import User

from Costumers.models import Profile, LessorModel


class UserLessorForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'second_name', 'last_name', 'second_last_name','email']
        labels = {
            'first_name' : 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'last_name': 'Apellido Paterno',
            'second_last_name': 'Apellido Materno', 
            'email': 'Correo Electrónico',
        }


class LessorForm(forms.ModelForm):

    class Meta:
        model = LessorModel
        fields = ['curp', 'elector_key', 'birthday', 'gender', 'occupation']