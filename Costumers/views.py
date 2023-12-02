from django.shortcuts import render, redirect
from django.views.generic import View


from CenturionApi.models import NoticeOfPrivacy
from CenturionApi.forms import NoticeOfPrivacyForm
from Costumers.models import LessorModel, TenantModel

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



class Lessors(View):
    template_name = "forms.html"
    context = {'viewname': "Arrendadores",
                "is_broker": False,}
    
    def get(self, request):
        
        user = request.user

        try:
            lessor = LessorModel.objects.get(user=user)
        except LessorModel.DoesNotExist:
            return redirect('costumers')
        
        return render(request, self.template_name, self.context)
