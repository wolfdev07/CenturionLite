from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User


from CenturionApi.models import NoticeOfPrivacy
from CenturionApi.forms import NoticeOfPrivacyForm
from Costumers.models import LessorModel, TenantModel, Profile
from Costumers.forms import ProfileForm, LessorForm


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
        
        
        profile = Profile.objects.get(user=user)
        profile_complete = profile.finished

        if profile_complete:
            self.context['is_lessor']= is_lessor
            self.context['form_name'] = 'Complementaria'
            self.context['description']='Completa los campos'
            self.context['form'] = LessorForm(instance=lessor)
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