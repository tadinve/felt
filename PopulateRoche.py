import os, django, csv
from django.db import connection
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GoogleSignin.settings' )
django.setup()

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

def populateRocheNewData():
    str_delete = "delete from roche_app_rochenewmodel where id > 0;"
    c = connection.cursor()
    c.execute(str_delete)
    with open('RocheUpdatedData.csv', 'r') as csvfile:
        datafile = csv.DictReader(csvfile)
        for row in datafile:
            i=1
            str1 = "Insert into roche_app_rochenewmodel(process_order_number,order_type_packaging_or_repackaging_field,material_number,product_name,process_order_creation_date,batch_number,process_order_release_date,packaging_line_start,packaging_line_finish,packaging_final_check_date,brr_start_date,brr_end_date,qa_release_date,product,batch_status,po_create_to_po_release,po_release_to_pkg_start,pkg_start_to_pkg_finish,pkg_finish_to_pkg_final_check,pkg_final_check_to_brr_begin,brr_begin_to_brr_finish,brr_finish_to_qp_release,fg_e2e,check_column) values('"+row['Process Order Number']+"','"+row['Order Type (packaging or repackaging)']+"','"+row['Material Number']+"','"+row['Product Name']+"','"+row['Process Order Creation Date']+"','"+row['Batch Number']+"','"+row['Process Order Release Date']+"','"+row['Packaging Line  Start']+"','"+row['Packaging Line Finish']+"','"+row['Packaging  Final Check Date']+"','"+row['BRR Start Date']+"','"+row['BRR End Date']+"','"+row['QA Release Date']+"','"+row['Product']+"',"+row['Batch Status']+","+row['PO Create to PO Release']+","+row['PO Release to Pkg Start']+","+row['Pkg Start to Pkg Finish']+","+row['Pkg Finish to Pkg Final Check']+","+row['Pkg Final Check to BRR Begin']+","+row['BRR Begin To BRR Finish']+","+row['BRR Finish to QP Release']+","+row['FG E2E']+",'"+row['Check']+"');"
            print(str1)
            c = connection.cursor()
            c.execute(str1)
            i += 1



if __name__ == '__main__':
    print("Starting to populate data")
    #populateRocheData()
    populateRocheNewData()


