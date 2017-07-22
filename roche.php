<?php
include('db.php');
//$sqlq = "select * from courses group by testyear";
$product = (isset($_POST['product']))?$_POST['product']:'';
$productname = (isset($_POST['productname']))?$_POST['productname']:'';
$sqlq = "select "
        . "product,"
        . "product_name,"
        . "batch_number,"
        . "YEAR(process_order_creation_date) as order_creation_year,"
        . "avg(po_create_release) as bar1,"
        . "avg(release_to_pkg_start) as bar2,"
        . "avg(pkg_finish_begin) as bar3, "
        . "avg(brr_start_finish) as bar4, "
        . "avg(brr_finish_qp_release) as bar5 "
        . "from roche ";
$where = '  WHERE 1=1 ';
$group = ' group by ';
if($productname){
    $where .= "and product_name = '".$productname."'";
    $group .= " batch_number " ;
}else if($product){
    $where .= "and product = '".$product."'";
    $group .= " product_name " ;
}else{
    $group .= " product " ;
}
   
    //$group .= " ,YEAR(process_order_creation_date)";
$sqlq = $sqlq.$where.$group;
$query = mysqli_query($sql,$sqlq);
if($productname){
    $myurl[] = array('Batvh Number','PO create to release', 'Release to Pkg Start','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['batch_number'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
    }
}else if($product){
    $myurl[] = array('Product Name','PO create to release', 'Release to Pkg Start','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['product_name'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
    }
}else{
    $myurl[] = array('Product','PO create to release', 'Release to Pkg Start','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['product'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
    }
}


echo json_encode($myurl);
?>








