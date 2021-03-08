from django.contrib import admin

# Register your models here.
from mainapp.models import UpdatedFiles, Fakultet, Smjer, Semestar


@admin.register(UpdatedFiles)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'webtag', 'date']


admin.site.register(Fakultet)
admin.site.register(Smjer)
admin.site.register(Semestar)
