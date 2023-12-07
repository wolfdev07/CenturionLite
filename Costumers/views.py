from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User


from CenturionApi.models import NoticeOfPrivacy, Settlement
from CenturionApi.forms import NoticeOfPrivacyForm
from Costumers.models import LessorModel, TenantModel, Profile, AddressModel, TenantEconomicModel, TenantSocioModel, LeasePropertyModel
from Costumers.forms import ProfileForm, LessorForm, AddressForm, LeasePropertyForm


# COSTUMERS VIEWS

class Compilance(View):
    template_name = 'compilance.html'
    context = {}
    def get(self, request):

        user = request.user
        privacy = NoticeOfPrivacy.objects.get(user=user)
        privacy_accepted = privacy.accept

        self.context['viewname'] = "Costumers"
        self.context['is_broker'] = False
        self.context['privacy_accepted'] = privacy_accepted

        if not privacy_accepted:
            self.context['form'] = NoticeOfPrivacyForm
            return render(request, self.template_name, self.context)
        elif privacy_accepted:
    
            return redirect('profile_costumer')
    
    def post(self, request):

        user = request.user

        try:
            privacy_notice = request.POST['privacy-notice']
        except:
            privacy_notice = False

        if not privacy_notice:
            return redirect('compilance')
        elif privacy_notice:
            update_privacy =  NoticeOfPrivacy.objects.get(user=user)
            update_privacy.accept = True
            update_privacy.save()
            self.context['success'] = "Aviso Aceptado"
            return redirect('compilance')




class ProfileUser(View):

    template_name =  "forms.html"
    context = {'viewname': "Profile",
                "is_broker": False,}
    
    def get(self, request):
        # IDENTIFICAR AL USER POR REQUEST
        user =  request.user

        # COMPROBAR SI ES ARRENDADOR
        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor = True
        except LessorModel.DoesNotExist:
            
            try: 
                tenant = TenantModel.objects.get(user=user)
            except TenantModel.DoesNotExist:
                is_lessor = False
        
        instance_profile = Profile.objects.get(user=user)


        self.context['is_lessor']= is_lessor
        self.context['form_name'] = 'Perfil'
        self.context['description']='Completa tu información'
        self.context['form'] = ProfileForm(instance=instance_profile)
        self.context['url_post'] = "/costumers/profile/"
        self.context['form_finished'] = instance_profile.finished

        if instance_profile.finished:
            self.context['next_button'] = 'Siguiente'
            #self.context['prev_button'] = 'Anterior'

        # RENDERIZA PRIMER FORM PROFILE
        return render(request, self.template_name, self.context)
    
    def post(self, request):

        # IDENTIFICAR AL USER POR REQUEST
        user =  request.user
        instance_profile = Profile.objects.get(user=user)

        form = ProfileForm(request.POST, instance=instance_profile)

        if form.is_valid():
            form.save()
            finished_form = Profile.objects.get(user=user)
            finished_form.finished = True
            finished_form.save()

        is_lessor = False

        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor = True
        except LessorModel.DoesNotExist:
            tenant = TenantModel.objects.get(user=user)

        if is_lessor:
            return redirect('lessors')
        elif not is_lessor:
            return redirect('tenants')



class Lessors(View):

    template_name = "forms.html"
    context = {'viewname': "Arrendadores",
                "is_broker": False,}
    
    def get(self, request):
        
        user = request.user

        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor = True
        except LessorModel.DoesNotExist:
            return redirect('tenants')
        
        instance = LessorModel.objects.get(user=user)
        profile = Profile.objects.get(user=user)
        profile_complete = profile.finished

        if profile_complete:
            self.context['is_lessor']= is_lessor
            self.context['form_name'] = 'Complementaria'
            self.context['description']='Completa los campos'
            self.context['form'] = LessorForm(instance=instance)
            self.context['url_post'] = "/costumers/lessors/"
            self.context['form_finished'] = profile_complete
            self.context['prev_btn_url']= "/costumers/profile/"
            self.context['prev_button'] = 'Anterior'
        
        
        if lessor.curp and lessor.elector_key:
            self.context['next_button'] = 'Siguiente'
        
        return render(request, self.template_name, self.context)


    def post(self, request):

        user = request.user
        lessor = LessorModel.objects.get(user=user)
        form = LessorForm(request.POST, instance=lessor)
        
        if form.is_valid():
            form.save()

        return redirect('lessors')




class ConcurrentAddress(View):
    template_name = "forms.html"
    context = {'viewname': "Profile",
                "is_broker": False,}
    
    def get(self, request):
        user = request.user

        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor=True
        except LessorModel.DoesNotExist:
            try:
                tenant = TenantModel.objects.get(user=user)

                is_lessor=False
            except  TenantModel.DoesNotExist:
                return redirect('signin')
        
        if is_lessor:
            instance = lessor.address_current
            self.context['prev_btn_url']= "/costumers/lessors/"
            self.context['prev_button'] = 'Anterior'
        
        else:
            data_tenant_socio = TenantSocioModel.objects.get(user=user)
            instance = data_tenant_socio.previous_address
        
        self.context['form_name'] = 'Domicilio Actual'
        self.context['description']='Ingresa tu domicilio actual'
        self.context['form'] = AddressForm(instance=instance)
        self.context['url_post'] = "/costumers/address/"

        return render(request, self.template_name, self.context)
    
    def post(self, request):

        user = request.user

        # DATA ADDRESS

        settlement_id = request.POST['settlement']
        street = request.POST['street']
        number = request.POST['number']

        try:
            internal_number = request.POST['internal_number']
        except:
            internal_number = ''

        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor=True
        except LessorModel.DoesNotExist:
            try:
                tenant = TenantModel.objects.get(user=user)
                is_lessor=False
            except  TenantModel.DoesNotExist:
                return redirect('signin')
            
        try:
                settlement = Settlement.objects.get(pk=settlement_id)
        except Settlement.DoesNotExist:
            self.context['error']="no existe el codigo postal"
            return render(request, self.template_name, self.context)
            
        
        current_address = AddressModel.objects.create(user=user,
                                                    street=street,
                                                    number=number,
                                                    internal_number=internal_number,
                                                    settlement=settlement,)
        current_address.save()
        
        if is_lessor:
            lessor.address_current = current_address
            lessor.save()
            return redirect('')
        else:
            previuos_address = TenantSocioModel.objects.get(user=user)
            previuos_address.previous_address = current_address
        
        return redirect('addres_costumer')




class CreateLeaseProperty(View):
    template_name = 'forms.html'
    context = {'viewname': "Profile",}

    def get(self, request):
        user =  request.user
        
        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor=True
        except LessorModel.DoesNotExist:
            try:
                tenant = TenantModel.objects.get(user=user)

                is_lessor=False
            except  TenantModel.DoesNotExist:
                return redirect('signin')
        
        if is_lessor:
            try:
                instance  = LeasePropertyModel.objects.get(lessor=lessor)
            except LeasePropertyModel.DoesNotExist:
                instance = False
            
            if instance:
                form = LeasePropertyForm(instance=instance)
            else:
                form = LeasePropertyForm

            self.context['form_name'] = 'Porpiedad en Renta'
            self.context['description']='Por favor, ingrese los datos para renta'
            self.context['form'] = form
            self.context['url_post'] = "/costumers/create/lease/property/"

            return render(request, self.template_name, self.context)
    
    def post(self, request):
        user = request.user

        rental_price = request.POST['rental_price']
        maintenance_price = request.POST['maintenance_price']

        try:
            id_maintenance_included = request.POST['id_maintenance_included']
        except:
            id_maintenance_included = False
        
        cfe_service_number = request.POST['cfe_service_number']
        water_service_number = request.POST['water_service_number']
        location = request.POST['location']

        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor=True
        except LessorModel.DoesNotExist:
            try:
                tenant = TenantModel.objects.get(user=user)

                is_lessor=False
            except  TenantModel.DoesNotExist:
                return redirect('signin')
        
        if is_lessor:
            lease_property = LeasePropertyModel.objects.create(lessor=lessor,
                                                                location=location,
                                                                rental_price=rental_price,
                                                                maintenance_price=maintenance_price,
                                                                maintenance_included=id_maintenance_included,
                                                                cfe_service_number=cfe_service_number,
                                                                water_service_number=water_service_number,
                                                                )
            lease_property.save()
        
            return redirect('lease_property_details')




class AddressLeaseProperty(View):
    template_name = 'forms.html'
    context = {'viewname': "Address",}

    def get(self, request):

        user =  request.user
        
        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor=True
        except LessorModel.DoesNotExist:
            try:
                tenant = TenantModel.objects.get(user=user)

                is_lessor=False
            except  TenantModel.DoesNotExist:
                return redirect('signin')
        
        if is_lessor:
            try:
                lease_property  = LeasePropertyModel.objects.get(lessor=lessor)
                instance = lease_property.property_address
            except LeasePropertyModel.DoesNotExist:
                instance = False
            
            if instance:
                form = AddressForm(instance=instance)
            else:
                form = AddressForm

            self.context['form_name'] = 'Porpiedad en Renta'
            self.context['description']='Ingrese la dirección de la propiedad'
            self.context['form'] = form
            self.context['url_post'] = "/costumers/address/lease/property/"

            return render(request, self.template_name, self.context)
        
    def post(self, request):

        user = request.user

        # DATA ADDRESS

        settlement_id = request.POST['settlement']
        street = request.POST['street']
        number = request.POST['number']

        try:
            internal_number = request.POST['internal_number']
        except:
            internal_number = ''

        try:
            lessor = LessorModel.objects.get(user=user)
            is_lessor=True
        except LessorModel.DoesNotExist:
            try:
                tenant = TenantModel.objects.get(user=user)
                is_lessor=False
            except  TenantModel.DoesNotExist:
                return redirect('signin')
            
        try:
            settlement = Settlement.objects.get(pk=settlement_id)
        except Settlement.DoesNotExist:
            self.context['error']="no existe el codigo postal"
            return render(request, self.template_name, self.context)
            
        if is_lessor:
            lease_property_address = AddressModel.objects.create(user=user,
                                                        street=street,
                                                        number=number,
                                                        internal_number=internal_number,
                                                        settlement=settlement,)
            lease_property_address.save()

            # SEARCH MODEL
            lease_property  = LeasePropertyModel.objects.get(lessor=lessor)
            lease_property.property_address = lease_property_address
            lease_property.save()
            
            return redirect('lease_property_address')
        else:
            return redirect('lease_property_address')