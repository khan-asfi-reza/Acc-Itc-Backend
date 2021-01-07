from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm, UserChangeForm
from django.contrib.auth import get_user_model

from Accounts.forms import AdminCreationForm, UserAdminChangeForm


# The Customized User Admin Interface
class UserAdminInterface(BaseUserAdmin):
    # Change Password Form
    form = UserChangeForm
    add_form = AdminCreationForm
    change_password_form = AdminPasswordChangeForm
    # List of information that will be displayed in the table of User Model Admin Panel
    list_display = ('username', 'name', 'id', 'phone_number', 'admin', 'staff')
    list_filter = ('admin', 'staff')
    # Fields Sets For Each User's information
    fieldsets = (
        (None, {'fields': ('username', 'name',)}),
        ('Security', {'fields': ('password',)}),
        ('Contact Info', {'fields': ('phone_number', 'email')}),
        ('Contact Info', {'fields': ('admin', 'staff')}),
    )
    readonly_fields = ['id', 'created']
    # Add User Form Fields
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'name', 'email', 'country_code', 'phone_number', 'password1', 'password2', 'admin',
                'staff')}
         ),
    )

    # Search using phone number and name
    search_fields = ('phone_number', 'name', 'email', 'username')
    # Order Using Id
    ordering = ('-id', 'admin',)
    filter_horizontal = ('user_permissions',)


# Registering in admin panel
admin.site.register(get_user_model(), UserAdminInterface)
admin.site.site_header = 'ACCITC Admin'
admin.site.site_title = "ACCITC Admin"
admin.site.index_title = "ACCITC Admin"
admin.site.site_url = "ACCITC Admin"