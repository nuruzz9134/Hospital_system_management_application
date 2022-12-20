from django.contrib import admin
from registration.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    
    list_display = ['id','name','phone','is_active','is_admin']

    list_filter =('is_admin',)

    ordering = ['id','phone']

    fieldsets = (
         (('User Credential'), {'fields': ('email', 'password')}),
         (('personal Info'), {'fields': ('name',)}),
         (('permissions'), {'fields': ('is_admin',)}),
         )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','name', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()

admin.site.register(User, UserModelAdmin)