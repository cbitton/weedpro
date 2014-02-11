from django.contrib import admin
from treatment.models import Treatment, Efficacy
from weeds.models import Weed

class EfficacyInline(admin.TabularInline):
    model = Efficacy
    extra = 5

#class WeedAdmin (admin.ModelAdmin):
#    inlines = (EfficacyInline,)

class TreatmentAdmin (admin.ModelAdmin):
    filter_horizontal = ('crops',)
    fieldsets = [
        ('Treatment details', {'fields': ['name','manufacturer','ingredients','rateHA','rateAC','timing']}),
        ('Crops', {'fields': ['crops']}),
        ('Treatment warnings', {'fields': ['notes','interval_rain','grazing_restrictions','pre_harvest','entry','buffer','storage','back_crops']}),
        ('Labelled weeds', {'fields': ['labelled_weeds_emerged','labelled_weeds_germination']}),
        ('Misc', {'fields': ['herbicide_MOA','faq']}),
    ]
    inlines = (EfficacyInline,)

# Register your models here.
admin.site.register(Treatment, TreatmentAdmin)
#admin.site.register(Weed, WeedAdmin)
