from django.contrib import admin

from .models import Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'subject', 'created_at')
    search_fields = ('recipient', 'subject')
