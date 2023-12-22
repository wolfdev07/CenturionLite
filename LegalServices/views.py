from django.shortcuts import render
from django.views.generic import View

class ManagerView(View):
    template_name = 'manager.html'
    context ={'viewname':'Manager'}
    def get(self, request):
        return render(request, self.template_name, self.context)