from django import forms

PHONE_CODES = (
    ('+52', '🇲🇽(+52)MX'),  # México
    ('+1', '🇺🇸(+1)EEUU'),   # Estados Unidos
    ('+54', '🇦🇷(+54)ARG'),  # Argentina
    ('+55', '🇧🇷(+55)BRA'),  # Brasil
    ('+56', '🇨🇱(+56)CL'),  # Chile
    ('+57', '🇨🇴(+57)COL'),  # Colombia
    ('+506', '🇨🇷(+506)CRI'),  # Costa Rica
    ('+53', '🇨🇺(+53)CUB'),  # Cuba
    ('+593', '🇪🇨(+593)EC'),  # Ecuador
    ('+503', '🇸🇻(+503)SLV'),  # El Salvador
    ('+502', '🇬🇹(+502)GTM'),  # Guatemala
    ('+504', '🇭🇳(+504)HND'),  # Honduras
    ('+505', '🇳🇮(+505)NI'),  # Nicaragua
    ('+507', '🇵🇦(+507)PTY'),  # Panamá
    ('+595', '🇵🇾(+595)PAR'),  # Paraguay
    ('+51', '🇵🇪(+51)PER'),  # Perú
    ('+598', '🇺🇾(+598)UY'),  # Uruguay
    ('+58', '🇻🇪(+58)VEN'),  # Venezuela
    ('+591', '🇧🇴(+591)BOL'),  # Bolivia
    )


class CustomerCreationForm(forms.Form):

    phone_code = forms.ChoiceField(label='Código de país', choices=PHONE_CODES)
    username = forms.CharField(label='Teléfono', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    is_lessor = forms.BooleanField(label='Es Propietario', required=False)
