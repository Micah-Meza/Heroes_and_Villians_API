from django.db import models

# Create your models here.
class SuperType(models.Model):
    hero = 'Hero'
    villian = 'Villian'
    super_choices = [ (hero, 'Hero'),
                    (villian, 'Villian'),
    ]

    type = models.CharField(max_length = 7, choices = super_choices, default = hero)
