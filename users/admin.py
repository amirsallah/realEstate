from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Landlord


class LandlordInline(admin.StackedInline):
    model = Landlord
    can_delete = False
    verbose_name_plural = 'landlords'


class UserAdmin(BaseUserAdmin):
    inlines = (LandlordInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
