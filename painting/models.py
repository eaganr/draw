from django.db import models

# Create your models here.

class Dot(models.Model):
	#hex color
	color = models.CharField(max_length=7)
	xpos = models.DecimalField(max_digits=5,decimal_places=2)
	ypos = models.DecimalField(max_digits=5,decimal_places=2)
