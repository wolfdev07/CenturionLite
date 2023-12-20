from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User

from Costumers.models import Profile, LessorModel, AddressModel, LeasePropertyModel, DataPaymentModel


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


bancos_nacionales=[
    ('BBVA', 'BBVA'),
    ('CitiBanamex', 'CitiBanamex'),
    ('HSBC', 'HSBC'),
    ('Santander', 'Santander'),
    ('Actinver', 'Actinver'),
    ('Banco Azteca', 'Banco Azteca'),
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

    postal_code = forms.CharField(label='Código Postal', required=True)
    state = forms.CharField(label='Estado', required=True, disabled=True)
    city = forms.CharField(label='Municipio', required=True, disabled=True)
    settlement = forms.ChoiceField(label='Colonia', required=True, choices=[('', '---')])

    class Meta:
        model = AddressModel
        fields = ['postal_code', 'state', 'city', 'settlement', 'street', 'number', 'internal_number']
        labels = {
            'street': 'Calle',
            'number': 'Numero',
            'internal_number': 'Numero Interior',
        }

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['postal_code'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['settlement'].widget.attrs['class'] = 'form-control'




class LeasePropertyForm(forms.ModelForm):

    class Meta:
        model = LeasePropertyModel
        fields = ['rental_price', 
                'maintenance_price', 
                'maintenance_included', 
                'cfe_service_number', 
                'water_service_number',
                'location',]
        labels = {
            'rental_price': 'Precio de Renta',
            'maintenance_price': 'Precio de Mantenimiento',
            'maintenance_included': 'Incluir costo en monto de renta',
            'cfe_service_number': 'Número de Servicio CFE*',
            'water_service_number': 'Número de Servicio Agua*',
            'location': 'URL ubicación maps',
        }


class DataPaymentForm(forms.ModelForm):

    class Meta:
        model=DataPaymentModel
        fields=['bank', 'interbank_account', 'account',]

        labels={
            'bank':'Banco',
            'interbank_account':'Clabe Interbancaria',
            'account': 'Cuenta',
        }

        widgets={
            'bank': forms.Select(choices=(bancos_nacionales), attrs={'class': 'form-group form-control'}),
        }