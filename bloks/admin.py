from django.contrib import admin

from bloks.models import Blok, Revision

class BlokAdmin(admin.ModelAdmin):
    pass

class RevisionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blok, BlokAdmin)
admin.site.register(Revision, RevisionAdmin)
