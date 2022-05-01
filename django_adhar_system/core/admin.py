from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','is_manager','is_staff')

admin.site.register(User , UserAdmin)
admin.site.register(Aadhar)
admin.site.register(Address)
admin.site.register(Qalification)
admin.site.register(Bank)
admin.site.register(PersonalDetails)
admin.site.register(PastJobExperience)

