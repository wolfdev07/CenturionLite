from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User

from Brokers.forms import CustomerCreationForm
from Brokers.models import Agencies, Broker
from Brokers.utils import generate_temp_password, validate_phone_number
from CenturionApi.utils import create_costumer_membership
from Costumers.models import LessorModel, TenantModel


class Dashboard(View):
    template_name = "dashboard.html"

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
                'broker': broker,
                'is_broker' : is_broker,
                'form': CustomerCreationForm,
                'costumers_lessors' : costumers_lessors,
                'costumers_tenants': costumers_tenants,
            }

            return render(request, self.template_name, context=context)
        
        else: 
            return redirect('signin')
    
    def post(sefl, request):

        user = request.user
        broker = Broker.objects.get(user=user)

        phone = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_code = request.POST['phone_code']

        try:
            is_lessor = request.POST['is_lessor']
        except:
            is_lessor = False

        phone_is_valid = validate_phone_number(phone)
        
        if phone_is_valid & bool(first_name) & bool(last_name):

            temp_password = generate_temp_password()

            user_costumer = User.objects.create(username=phone, password=temp_password)
            user_costumer.first_name = first_name
            user_costumer.last_name = last_name
            user_costumer.is_active = False
            user_costumer.save()

            phone_lessor = f"{phone_code}{phone}"
            membership = create_costumer_membership()

            if is_lessor:
                create_lessor = LessorModel.objects.create( user=user_costumer, 
                                                            phone=phone_lessor, 
                                                            broker=broker, 
                                                            membership=membership )
                create_lessor.save()
                return redirect('dashboard')

            else:
                create_tenant = TenantModel.objects.create( user=user_costumer,
                                                            phone=phone_lessor, 
                                                            broker=broker, 
                                                            membership=membership )
                create_tenant.save()
                return redirect('dashboard')
