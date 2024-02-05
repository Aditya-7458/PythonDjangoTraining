from django.contrib import admin
from mymodel.models import Mymodel

class Admin(admin.ModelAdmin):
    list_display=('name','email','phone')

admin.site.register(Mymodel,Admin)

# Register your models here.
