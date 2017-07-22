import os, django, csv
from django.db import connection


def populateRocheData():
    with open('RocheData.csv', 'r') as csvfile:
        datafile = csv.DictReader(csvfile)
        for row in datafile:
            i=1
            str1 = "Insert into roche_app_roche(rochekey,process_order_number,order_type,material_number,product_name,process_order_creation_date,batch_number,process_order_release_date,packaging_start_date,packaging_end_date,packaging_head_pkg_signoff,bbr_start,bbr_end,qa_release_date,product,batch_status,po_create_release,release_to_pkg_start,pkg_start_bbr_finish,pkg_finish_begin,brr_start_finish,brr_finish_qp_release,fge2e,check_column) values('"+row['Key']+"','"+row['Process Order Number']+"','"+row['Order Type (packaging or repackaging)']+"','"+row['Material Number']+"','"+row['Product Name']+"','"+row['Process Order Creation Date']+"','"+row['Batch Number']+"','"+row['Process Order Release Date']+"','"+row['Packaging Start Date']+"','"+row['Packaging End Date']+"','"+row['Packaging Head Pkg Sigoff']+"','"+row['BRR Start']+"','"+row['BRR End']+"','"+row['QA Release Date']+"','"+row['Product']+"',"+row['Batch Status']+","+row['PO Crearte to Release']+","+row['Release to Pkg Start']+","+row['Pkg Start to Finish']+","+row['PKG Finish to BRR Begin']+","+row['BRR Start To Finish']+","+row['BRR Finish to QP Release']+","+row['FG E2E']+",'"+row['Check']+"');"
            print(str1)
            c = connection.cursor()
            c.execute(str1)
            i += 1



if __name__ == '__main__':
    print("Starting to populate data")
    populateRocheData()

    '''rochekey = models.CharField(max_length=125, blank=True, null=True)
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
    check_column = models.CharField(max_length=15, blank=True, null=True)'''