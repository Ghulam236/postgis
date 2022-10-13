from django.contrib import admin
from .models import Incidences, country,Indstates
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

# class IncidencesAdmin(admin.ModelAdmin):
class IncidencesAdmin(LeafletGeoAdmin):
    # pass
    list_display= ('name', 'location')
class countryAdmin(LeafletGeoAdmin):
    # pass
    list_display= ('name_1', 'id_1')
class IndstatesAdmin(LeafletGeoAdmin):
    # pass
    list_display= ('name_2', 'id_2')



admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(country, countryAdmin)
admin.site.register(Indstates, IndstatesAdmin)