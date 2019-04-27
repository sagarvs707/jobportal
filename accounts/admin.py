from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
User = get_user_model()

class UserAdmin(BaseUserAdmin):

    # The forms to add and change user instance
    form = UserAdminChangeForm #edit or update view
    add_from = UserAdminCreationForm #create view

    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('personal info', {'fields': ('full_name', 'phone_number', 'address',)}),
        ('permissions', {'fields':('admin', 'staff','active',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overides get_fieldsets to use this attribute when  creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ['email']
    ordering = ('email',)
    filter_horizontal = ()
    # class meta:
    #     model = User

admin.site.register(User, UserAdmin)

# Remove group maodel from admin. we're not using it

admin.site.unregister(Group)
