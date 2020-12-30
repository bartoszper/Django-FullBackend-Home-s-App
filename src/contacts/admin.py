from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','listing')
    list_display_links = ('id','name')
    list_per_page = 25
    list_filter = ('listing',)
    search_fields = ('listing','name','email')


admin.site.register(Contact, ContactAdmin)