from django.db import models

# Create your models here.

class SuperType(models.Model):
    hero = 'Hero'
    villain = 'Villain'
    super_choices = [ (hero, 'Hero'),
                    (villain, 'Villain'),
    ]

    type = models.CharField(max_length = 7, choices = super_choices, default = None)
