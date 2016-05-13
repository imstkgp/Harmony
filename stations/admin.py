from django.contrib import admin
from models import Station, Favourite, MostPlayed

class FavouriteAdminInline(admin.TabularInline):
    model = Favourite
    extra = 0
    readonly_fields = ('station',)
    pass


class MostPlayedAdminInline(admin.TabularInline):
    model = MostPlayed
    extra = 0
    readonly_fields = ('station',)
    pass

class StationAdmin(admin.ModelAdmin):
    inlines = [FavouriteAdminInline, MostPlayedAdminInline]
    list_display = ("id", "stationId", "name", "country_code", "stream_url", "genre_name", "language", "active")
    list_filter = ("active", "genre_name", "country_code", "language")
    search_fields = ("stationId","name")
admin.site.register(Station, StationAdmin)
