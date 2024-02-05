from django.contrib import admin
from mymodel.models import Mymodel

class ModelAdmin(admin.ModelAdmin):
    list_display=('name','email','desc')

admin.site.register(Mymodel,ModelAdmin)

# Register your models here.
