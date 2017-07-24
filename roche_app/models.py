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
    process_order_creation_date = models.CharField(max_length=12,blank=True, null=True)
    batch_number = models.CharField(max_length=255, blank=True, null=True)
    process_order_release_date = models.CharField(max_length=12,blank=True, null=True)
    packaging_start_date = models.CharField(max_length=12,blank=True, null=True)
    packaging_end_date = models.CharField(max_length=12,blank=True, null=True)
    packaging_head_pkg_signoff = models.CharField(max_length=12,blank=True, null=True)
    bbr_start = models.CharField(max_length=12,blank=True, null=True)
    bbr_end = models.CharField(max_length=12,blank=True, null=True)
    qa_release_date = models.CharField(max_length=12,blank=True, null=True)
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

class RocheNewModel(models.Model):
    rocheid = models.CharField(db_column='Key', max_length=18, blank=True, null=True)  # Field name made lowercase.
    process_order_number = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_type_packaging_or_repackaging_field = models.CharField(max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    material_number = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_name = models.CharField(max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    process_order_creation_date = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batch_number = models.CharField(max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    process_order_release_date = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    packaging_line_start = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    packaging_line_finish = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    packaging_final_check_date = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brr_start_date = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brr_end_date = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qa_release_date = models.CharField(max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    batch_status = models.CharField(max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    po_create_to_po_release = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    po_release_to_pkg_start = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pkg_start_to_pkg_finish = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pkg_finish_to_pkg_final_check = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pkg_final_check_to_brr_begin = models.CharField(max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brr_begin_to_brr_finish = models.CharField(max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brr_finish_to_qp_release = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fg_e2e = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    check_column = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.product_name)