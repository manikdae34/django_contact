from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
from import_export.admin import ImportExportModelAdmin

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'gradation', 'designation', 'posting', 'mobile')
    list_editable = ('designation',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'gradation', 'designation', 'posting', 'mobile')
    list_filter = ('gender', 'date_added')

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
