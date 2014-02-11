from django.contrib import admin
from crops.models import Crop, Crop_Detail

class DetailInline(admin.TabularInline):
    model = Crop_Detail
    extra = 3
    verbose_name = "Crop Detail"
    verbose_name_plural = "Crop Details"

class CropAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date'], }),
    ]
    list_display = ('name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['name']
    inlines = [DetailInline]


admin.site.register(Crop, CropAdmin)

