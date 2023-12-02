from django.contrib import admin
from CenturionApi.models import State, City, PostalCode, Settlement, NoticeOfPrivacy


admin.site.register(NoticeOfPrivacy)
admin.site.register(State)
admin.site.register(City)
admin.site.register(PostalCode)
admin.site.register(Settlement)