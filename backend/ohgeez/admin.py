from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('longitude', 'latitude')

admin.site.register(Category)
admin.site.register(Item)
