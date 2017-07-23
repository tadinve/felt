<?php
include('db.php');
//$sqlq = "select * from courses group by testyear";
$product = (isset($_POST['product']))?$_POST['product']:'';
$productname = (isset($_POST['productname']))?$_POST['productname']:'';
$batchnumber = (isset($_POST['batchnumber']))?$_POST['batchnumber']:'';
$timeline = (isset($_POST['timeline']))?$_POST['timeline']:'';

$sqlq = "select "
        . "product,"
        . "product_name,"
        . "batch_number,"
        . "YEAR(process_order_creation_date) as order_creation_year,"
        . "QUARTER(process_order_creation_date) as order_creation_quarter,"
        . "MONTH(process_order_creation_date) as order_creation_month,"
        . "WEEK(process_order_creation_date) as order_creation_week,"
        . "avg(po_create_release) as bar1,"
        . "avg(release_to_pkg_start) as bar2,"
        . "avg(pkg_finish_begin) as bar3, "
        . "avg(brr_start_finish) as bar4, "
        . "avg(brr_finish_qp_release) as bar5,"
        . "avg(pkg_start_bbr_finish) as bar6 "
        . "from roche ";
$where = '  WHERE 1=1 ';
$group = ' group by ';
if($batchnumber){
    $where .= "and batch_number = '".$batchnumber."'";
     $group .= " batch_number " ;
}else if($productname){
    $where .= "and product_name = '".$productname."'";
    $group .= " batch_number " ;
}else if($product){
    $where .= "and product = '".$product."'";
    $group .= " product_name " ;
}else{
    $group .= " product " ;
}

if($timeline=='quarter'){
    $group .= " ,QUARTER(process_order_creation_date)";
}else if($timeline=='month'){
    $group .= " ,MONTH(process_order_creation_date)";
}else if($timeline=='week'){
    $group .= " ,WEEK(process_order_creation_date)";
}else {
    $group .= " ,YEAR(process_order_creation_date)";
}

$order = '';
$order = ' ORDER by process_order_creation_date';

$sqlq = $sqlq.$where.$group.$order;

$query = mysqli_query($sql,$sqlq);



if($batchnumber){
    $myurl[] = array('Batch Number','PO create to release', 'Release to Pkg Start','PKG Start to BRR Finish','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['order_creation_week']." ".$row['batch_number'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar6'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
    }
}else if($productname){
    $myurl[] = array('Batch Number','PO create to release', 'Release to Pkg Start','PKG Start to BRR Finish','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['order_creation_year']." ".$row['batch_number'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar6'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
    }
}else if($product){
    $myurl[] = array('Product Name','PO create to release', 'Release to Pkg Start','PKG Start to BRR Finish','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['order_creation_year']." ".$row['product_name'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar6'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
    }
}else{
    $myurl[] = array('Product','PO create to release', 'Release to Pkg Start','PKG Start to BRR Finish','PKG Finish to BRR Begin','BRR Start to Finish','BRR Finish to QP Release');
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['order_creation_year']." ".$row['product'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar6'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5']);
    }
}


echo json_encode($myurl);
?>








