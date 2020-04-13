from django.contrib import admin
from .models import Realtors

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','email','phone','hire_date')
    list_display_links=('id','name')
    search_fields=('name',)
    list_per_page=25
    sortable_by=('hire_date',)

admin.site.register(Realtors,RealtorAdmin)