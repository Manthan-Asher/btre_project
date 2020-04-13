from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','realtor')
    list_display_links=('id','title')
    list_editable=('is_published',)
    list_filter=('realtor',)
    list_per_page=25
    search_fields= ('title','city','state','price','realtor',)
    sortable_by= ('price','list_date',)

admin.site.register(Listing,ListingAdmin)
