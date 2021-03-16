from django.contrib import admin
# Register your models here.
from mainapp.models import UpdatedFiles, Fakultet, Smjer, Semestar


@admin.register(UpdatedFiles)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'webtag', 'date']


class SemestarAdmin(admin.ModelAdmin):
    model = Semestar
    list_display = ['fakultet', 'smjer', 'semestar']
    list_filter = ['fakultet', 'smjer', 'semestar']


admin.site.register(Fakultet)
admin.site.register(Smjer)
admin.site.register(Semestar, SemestarAdmin)
