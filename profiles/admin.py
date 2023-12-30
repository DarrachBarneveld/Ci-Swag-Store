from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order

class OrderInline(admin.TabularInline):  
    model = Order
    fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'town_or_city',
        'order_total',
        'grand_total',
        'date',
    )
    readonly_fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'town_or_city', 'order_total', 'grand_total')


# Register your models here.
class ProfileInline(admin.StackedInline):
    """
    Inline representation of user profiles for the admin panel.

    """

    model = UserProfile
    inlines = [OrderInline]  



class UserAdmin(admin.ModelAdmin):
    """
    Admin model configuration for user accounts.

    This class defines the admin panel configuration for user accounts,
    allowing administrators to manage user information such as username,
    first name, last name, and email. It also includes an inline
    representation of user profiles using the `ProfileInline` class

    Example:
        To use this admin configuration for user accounts:

        admin.site.register(User, UserAdmin)

    """

    model = User
    fields = ("username", "first_name", "last_name", "email")
    inlines = [ProfileInline]

class ProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    inlines = [OrderInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, ProfileAdmin)