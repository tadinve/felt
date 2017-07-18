<?php
include('db.php');
//$sqlq = "select * from courses group by testyear";
$sqlq = "select "
        . "product,"
        . "YEAR(process_order_creation_date) as order_creation_year,"
        . "sum(po_create_release) as bar1,"
        . "sum(release_to_pkg_start) as bar2,"
        . "sum(pkg_finish_begin) as bar3, "
        . "sum(brr_start_finish) as bar4, "
        . "sum(brr_finish_qp_release) as bar5 "
        . "from roche "
        . "group by "
        . "YEAR(process_order_creation_date),"
        . "product";
$query = mysqli_query($sql,$sqlq);

$myurl[] = array('Product','PO create to release', 'Release to Pkg Start','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
while ($row = mysqli_fetch_assoc($query)) {
    $myurl[] = array($row['order_creation_year']." ".$row['product'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
}

echo json_encode($myurl);
?>








