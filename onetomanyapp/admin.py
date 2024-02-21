from django.contrib import admin
from.models import University,College
# Register your models here.
class University_admin(admin.ModelAdmin):
    list_display = ['id','u_name','u_reg','u_address','u_email','u_mobile']

class College_admin(admin.ModelAdmin):
    list_display = ['id','c_name','c_address','c_mobile','c_code','c_email']

admin.site.register(University,University_admin)
admin.site.register(College,College_admin)