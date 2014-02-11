from django.db import models

class Weed (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

#class Efficacy (models.Model):
#    weed = models.ForeignKey(Weed)
#    treatment = models.ForeignKey(Treatment)
#    rating = models.SmallIntegerField()
    
