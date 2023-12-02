from django import forms
from CenturionApi.models import NoticeOfPrivacy


class NoticeOfPrivacyForm(forms.ModelForm):

    class Meta:
        model = NoticeOfPrivacy
        fields = ['accept']
        labels = {
            'accept': 'He leído y acepto.'
        }