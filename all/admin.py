from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('name', 'email', 'phone','date_updated','date_posted')
    list_filter = ('email',)
    readonly_fields = ('message',)
    search_fields = ('email',)
    date_hierarchy = 'date_posted'
    ordering = ('-pk',)
    list_per_page = 20