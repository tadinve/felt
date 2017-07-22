import os, django, csv
from roche_app.models import Roche


def populateRocheData():
    with open('RocheData.csv', 'r') as csvfile:
        datafile = csv.DictReader(csvfile)
        for row in datafile:
            RocheObj = Roche()
            rochekey = row[0]
            process_order_number = row[1]
            order_type = row[2]
            material_number = row[3]
            product_name = row[4]
            process_order_creation_date = row[5]
            batch_number = row[6]
            process_order_release_date = row[7]
            packaging_start_date = row[8]
            packaging_end_date = row[9]
            packaging_head_pkg_signoff = row[10]
            bbr_start = row[11]
            bbr_end = row[12]
            qa_release_date = row[13]
            product = row[14]
            batch_status = row[15]
            po_create_release = row[16]
            release_to_pkg_start = row[17]
            pkg_start_bbr_finish = row[18]
            pkg_finish_begin = row[19]
            brr_start_finish = row[20]
            brr_finish_qp_release = row[21]
            fge2e = row[22]
            check_column =row[23]



if __name__ == '__main__':
    print("Starting to populate data")
    populateRocheData()