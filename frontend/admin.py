from django.contrib import admin
from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    '''Admin View for Project'''

    list_display = ('title', 'date', 'location')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('name', 'date','phone','email')
    list_filter = ('date',)
    search_fields = ('name', 'phone', 'email', 'message',)
