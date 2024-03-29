from django.contrib import admin
from .models import Menu
# Register your models here.

admin.site.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    prepopulated_fields = {"slug": ("name", )}
