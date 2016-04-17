from django.contrib import admin
from base.models import Language
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")

admin.site.register(Language, LanguageAdmin)
