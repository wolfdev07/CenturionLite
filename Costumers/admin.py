from django.contrib import admin
from Costumers.models import *

# Register your models here.


admin.site.register(AddressModel)
admin.site.register(ReferencesModel)
admin.site.register(LessorModel)
admin.site.register(DataPaymentModel)
admin.site.register(LessorDocumentsModel)
admin.site.register(LeasePropertyModel)

# TENANT ADMIN MODELS

admin.site.register(TenantModel)
admin.site.register(TenantEconomicModel)
admin.site.register(TenantSocioModel)
admin.site.register(TenantDocumentsModel)
admin.site.register(SolidarityEconomicModel)