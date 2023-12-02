from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User

from Brokers.forms import CustomerCreationForm
from Brokers.models import Broker
from Brokers.utils import generate_temp_password, validate_phone_number
from CenturionApi.utils import create_costumer_membership, send_wa_credentials
from CenturionApi.models import NoticeOfPrivacy
from Costumers.models import LessorModel, TenantModel


class Dashboard(View):
    template_name = "dashboard.html"
    context={}

    def get(self, request):

        user = request.user

        try: 
            broker = Broker.objects.get(user=user)
            is_broker = True
        except Broker.DoesNotExist:
            is_broker = False
        

        if is_broker:

            try:
                costumers_lessors = LessorModel.objects.filter(broker=broker)
            except LessorModel.DoesNotExist:
                costumers_lessors = {}

            try:
                costumers_tenants = TenantModel.objects.filter(broker=broker)
            except TenantModel.DoesNotExist:
                costumers_tenants = {}

            context = {
                'viewname': 'Dasboard',
                'broker': broker,
                'is_broker' : is_broker,
                'form': CustomerCreationForm,
                'costumers_lessors' : costumers_lessors,
                'costumers_tenants': costumers_tenants,
            }

            return render(request, self.template_name, context=context)
        
        else: 
            return redirect('signin')
    
    def post(self, request):

        user = request.user
        broker = Broker.objects.get(user=user)

        phone = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_code = request.POST['phone_code']

        try:
            is_lessor = request.POST['is_lessor']
            is_lessor = True
        except:
            is_lessor = False

        phone_is_valid = validate_phone_number(phone)
        
        if phone_is_valid & bool(first_name) & bool(last_name):

            temp_password, hashed_temp_password = generate_temp_password()

            user_costumer = User.objects.create(username=phone, password=hashed_temp_password)
            user_costumer.first_name = first_name
            user_costumer.last_name = last_name
            user_costumer.is_active = True
            user_costumer.save()
            print(f"{user_costumer}: {temp_password}")

            phone_complete = f"{phone_code}{phone}"
            membership = create_costumer_membership()

            if is_lessor:
                create_lessor = LessorModel.objects.create( user=user_costumer, 
                                                            phone=phone_complete, 
                                                            broker=broker, 
                                                            membership=membership )
                create_lessor.save()

            else:
                create_tenant = TenantModel.objects.create( user=user_costumer,
                                                            phone=phone_complete, 
                                                            broker=broker, 
                                                            membership=membership )
                create_tenant.save()

            NoticeOfPrivacy.objects.create(user=user_costumer, accept=False) 

            data = {
                'brokername': f"{request.user.first_name} {request.user.last_name}",
                'code_country':phone_code,
                'phone': phone,
                'name': f"{first_name} {last_name}",
                'user': phone,
                'password': temp_password,
                'is_lessor' : is_lessor,
            }
            
            send = send_wa_credentials(data)

            if send:
                self.context['success'] = "Usuario creado con exito."
                return redirect('dashboard')
            else:
                user_costumer.delete()
                self.context['error'] = "No se pudo guardar los cambios"
                return render(request, self.template_name, self.context)
