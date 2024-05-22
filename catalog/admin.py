from django.contrib import admin

# Register your models here.
from .models import Proletary, View, Work, WorkInstance,Ad


admin.site.register(Work)
admin.site.register(Proletary)
admin.site.register(View)
admin.site.register(WorkInstance)
admin.site.register(Ad)



