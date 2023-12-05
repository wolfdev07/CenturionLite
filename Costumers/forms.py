from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User

from Costumers.models import Profile, LessorModel, AddressModel


ocupaciones_generales = [
    ('empleado', 'Empleado'),
    ('profesor', 'Profesor'),
    ('ingeniero', 'Ingeniero'),
    ('medico', 'Médico'),
    ('abogado', 'Abogado'),
    ('empresario', 'Empresario'),
    ('trabajador_independiente', 'Trabajador Independiente'),
    ('artista', 'Artista'),
    ('escritor', 'Escritor'),
    ('empleado_gobierno', 'Empleado de Gobierno'),
    ('periodista', 'Periodista'),
    ('vendedor', 'Vendedor'),
    ('consultor', 'Consultor'),
]


nacionalidades = [
    ('mexicana', '🇲🇽 Mexicana'),
    ('argentina', '🇦🇷 Argentina'),
    ('chilena', '🇨🇱 Chilena'),
    ('colombiana', '🇨🇴 Colombiana'),
    ('ecuatoriana', '🇪🇨 Ecuatoriana'),
    ('salvadoreña', '🇸🇻 Salvadoreña'),
    ('guatemalteca', '🇬🇹 Guatemalteca'),
    ('hondureña', '🇭🇳 Hondureña'),
    ('nicaragüense', '🇳🇮 Nicaragüense'),
    ('panameña', '🇵🇦 Panameña'),
    ('paraguaya', '🇵🇾 Paraguaya'),
    ('peruana', '🇵🇪 Peruana'),
    ('uruguaya', '🇺🇾 Uruguaya'),
    ('venezolana', '🇻🇪 Venezolana'),
    ('brasileña', '🇧🇷 Brasileña'),
    ('estadounidense', '🇺🇸 Estadounidense'),
    ('canadiense', '🇨🇦 Canadiense'),
    ('francesa', '🇫🇷 Francesa'),
    ('alemana', '🇩🇪 Alemana'),
    # Puedes agregar más nacionalidades y emojis aquí
]


class ProfileForm(forms.ModelForm):

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
        fields = ['nationality', 'curp', 'elector_key', 'birthday', 'occupation']

        labels = {
            'nationality': 'Nacionalidad',
            'curp': 'CURP*',
            'elector_key': 'Numero de ID*',
            'birthday': 'Fecha de Nacimiento',
            'occupation': 'Ocupacion*',
        }

        widgets = {
            'nationality' : forms.Select(choices=(nacionalidades), attrs={'class': 'form-group form-control'}),
            'curp': forms.TextInput(attrs={'class': 'form-group form-control',
                                            'required': 'required'}),
            'elector_key': forms.TextInput(attrs={'class': 'form-group form-control',
                                            'required': 'required'}),
            'birthday' : DateInput(attrs={'type':'date'}),
            'occupation': forms.Select(choices=(ocupaciones_generales), attrs={'class': 'form-group form-control'}),
        }


class AddressForm(forms.ModelForm):



    class Meta:
        model = AddressModel
        fields = ['street', 'number', 'internal_number']

        labels = {
            'street':'Calle',
            'number': 'Numero',
            'internal_number': 'Numero Interior',
        }