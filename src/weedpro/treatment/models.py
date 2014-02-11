from django.db import models
from crops.models import Crop_Detail
from weeds.models import Weed

class Treatment (models.Model):
    crops = models.ManyToManyField(Crop_Detail)
    weed = models.ManyToManyField(Weed, through='Efficacy')
    name = models.CharField(max_length=200, unique=True)
    manufacturer = models.CharField(max_length=200)
    PREPLANT  = 'PP'
    POSTEMERG = 'PE'
    APPLICATION_TIMING = (
        (PREPLANT,  'Pre-Plant'),
        (POSTEMERG, 'Post-Emergence'),
    )
    timing = models.CharField(max_length=2, choices=APPLICATION_TIMING,
                              default=POSTEMERG)
    ingredients = models.CharField(max_length=200)
    rateHA = models.CharField(max_length=200)
    rateAC = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    NA           = '0'
    ONEHR        = '1'
    TWOHR        = '2'
    THREEHR      = '3'
    FOURHR       = '4'
    TWELVEHR     = '12'
    TWENTYFOURHR = '24'
    SEVENDAYS    = '7'
    THIRTYDAYS   = '30'
    SIXTYDAYS    = '60'
    RAIN_INTERVAL = (
        (ONEHR,  '1 hour'),
        (TWOHR,  '2 hours'),
        (THREEHR,'3 hours'),
        (FOURHR, '4 hours'),
    )
    interval_rain = models.CharField('Intverval before rainfall', max_length=2,
                                     choices=RAIN_INTERVAL, default=4)
    GRAZING = (
        (SEVENDAYS, '7 days'),
        (THIRTYDAYS,'30 days'),
        (SIXTYDAYS, '60 days'),
    )
    grazing_restrictions = models.CharField(max_length=2, choices=GRAZING, 
                                            default=7)
    PRE_HARVEST = (
        (SEVENDAYS, '7 days'),
        (THIRTYDAYS,'30 days'),
        (SIXTYDAYS, '60 days'),
    )
    pre_harvest = models.CharField('pre harvest interval', max_length=2, 
                                   choices=PRE_HARVEST, default=60)
    ENTRY = (
        (TWELVEHR,    '12 hours'),
        (TWENTYFOURHR,'24 hours'),
        (NA,          'NA'),
    )
    entry = models.CharField('entry into treated areas', max_length=2, 
                             choices=ENTRY, default=12)
    buffer = models.CharField(max_length=200,blank=True)
    storage = models.TextField(blank=True)
    back_crops = models.TextField(blank=True)
    labelled_weeds_emerged = models.TextField(blank=True)
    labelled_weeds_germination = models.TextField(blank=True)
    herbicide_MOA = models.TextField('herbicide mode of action',blank=True)
    faq = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Efficacy (models.Model):
    weed = models.ForeignKey(Weed)
    treatment = models.ForeignKey(Treatment)
    rating = models.SmallIntegerField()

    def __unicode__(self):
        return self.weed
