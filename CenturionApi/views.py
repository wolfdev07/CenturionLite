from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


class SignIn(View):
    template_name = "auth/signin.html"

    def get(self, request):

        context = {
            'form': AuthenticationForm,
        }
    
        return render(request, self.template_name, context=context)
    
    