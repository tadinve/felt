from django.db import models

# Create your models here.
from django.conf import settings

# Create your models here.

class Roche(models.Model):
    rochekey = models.CharField(max_length=125, blank=True, null=True)
    process_order_number = models.CharField(max_length=255, blank=True, null=True)
    order_type = models.CharField(max_length=255, blank=True, null=True)
    material_number = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    process_order_creation_date = models.DateField(blank=True, null=True)
    batch_number = models.CharField(max_length=255, blank=True, null=True)
    process_order_release_date = models.DateTimeField(blank=True, null=True)
    packaging_start_date = models.DateField(blank=True, null=True)
    packaging_end_date = models.DateField(blank=True, null=True)
    packaging_head_pkg_signoff = models.DateField(blank=True, null=True)
    bbr_start = models.DateField(blank=True, null=True)
    bbr_end = models.DateField(blank=True, null=True)
    qa_release_date = models.DateField(blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    batch_status = models.IntegerField(blank=True, null=True)
    po_create_release = models.IntegerField(blank=True, null=True)
    release_to_pkg_start = models.IntegerField(blank=True, null=True)
    pkg_start_bbr_finish = models.IntegerField(blank=True, null=True)
    pkg_finish_begin = models.IntegerField(blank=True, null=True)
    brr_start_finish = models.IntegerField(blank=True, null=True)
    brr_finish_qp_release = models.IntegerField(blank=True, null=True)
    fge2e = models.IntegerField(blank=True, null=True)
    check_column = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
    	return str(self.product_name)