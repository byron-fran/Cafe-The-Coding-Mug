from django.contrib import admin
from .models import Review

# Register your models here.
 
admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display =[ 'user', 'title', 'created_at']