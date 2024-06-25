from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.
@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', 'is_private')

@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'message')