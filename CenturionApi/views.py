from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from Brokers.models import Broker


# INDEX

def index(request):
    return redirect('signin')



# Iniciar Sesion
class SignIn(View):
    template_name = "auth/signin.html"
    context = {
            'form': AuthenticationForm,
        }
    def get(self, request):
        self.context['viewname']="Sign In"
        return render(request, self.template_name, self.context)
    
    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            print(f"{ username } es none")
            self.context['error'] = 'Usuario o password incorrectos'
            return render(request, self.template_name, self.context)
        
        else:
            login(request, user)
            
            user_login = request.user

            try:
                is_broker = Broker.objects.get(user=user_login)
            except Broker.DoesNotExist:
                is_broker = False
            
            if is_broker:
                return redirect('dashboard')
            else:
                return redirect('control_data')


# LOGOUT FUNCTION
def signout(request):
    logout(request)
    return redirect('signin')