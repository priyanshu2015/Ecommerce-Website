from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('user_email', 'is_staff', 'is_active',)
    list_filter = ('user_email', 'is_staff', 'is_active', 'is_premium_activated')
    fieldsets = (
        (None, {'fields': ('user_phone', 'password','user_email','is_email_verified',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_premium_activated' , 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates',{'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_email', 'user_phone', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    search_fields = ('user_email',)     #search_filter
    ordering = ('user_email',)          # ordering through


admin.site.register(User, UserAdmin)

# Register your models here.
from .models import Product, Contact ,Orders, OrderUpdate      # Contact table for storing details of clients who have some query and asked through form

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

