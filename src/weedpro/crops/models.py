from django.db import models
from django.utils import timezone
import datetime

class Crop (models.Model):
    name = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Crop_Detail (models.Model):
    crop = models.ForeignKey(Crop)
    crop_type = models.CharField(max_length=200)
    underseed = models.CharField(blank=True, max_length=200)
    def __unicode__(self):
        if not self.underseed:
            return self.crop.name + ': ' + self.crop_type
	else:
	    return self.crop.name + ': ' + self.crop_type + ' underseeded with ' + self.underseed
