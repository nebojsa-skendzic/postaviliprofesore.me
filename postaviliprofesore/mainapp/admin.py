from django.contrib import admin
# Register your models here.
from mainapp.models import UpdatedFiles, Fakultet, Smjer, Semestar


@admin.register(UpdatedFiles)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'webtag', 'date']


class SemestarAdmin(admin.TabularInline):
    model = Semestar


class SmjerAdmin(admin.ModelAdmin):
    inlines = [
        SemestarAdmin,
    ]

    list_display = ['fakultet', 'smjer']
    list_filter = ['fakultet']


admin.site.register(Fakultet)
admin.site.register(Smjer, SmjerAdmin)
