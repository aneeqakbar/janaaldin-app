from django.contrib import admin
from .models import User, StaffMember

# Register your models here.

admin.site.register(User)
admin.site.register(StaffMember)

