from django.db import models

# Create your models here.
from django.conf import settings

# Create your models here.

class Pivot_table(models.Model):
	ProductName = models.CharField(max_length=15)
	PO_Crearte_to_Release = models.FloatField(blank=False, default = 0.0)
	Pkg_Start_to_Finish = models.FloatField(blank=False, default = 0.0)
	Release_to_Pkg_Start = models.FloatField(blank=False, default = 0.0)
	BRR_Start_To_Finish = models.FloatField(blank=False, default = 0.0)
	BRR_Finish_to_QP_Release = models.FloatField(blank=False, default = 0.0)

	def __str__(self):
		return str(self.id)