from django.contrib import admin

# Register your models here.
from mainapp.models import UpdatedFiles

@admin.register(UpdatedFiles)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'webtag', 'date']
