from django.shortcuts import render
from django.views.generic import View

class Costumers(View):
    template_name = 'costumers.html'
    context = {}
    def get(self, request):
        self.context['viewname'] = "cOSTUMERS"

        return render(request, self.template_name, self.context)