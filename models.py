# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class data(models.Model):
    temperature = models.DecimalField(max_digits=20,decimal_places=2)
