<?php
include('db.php');
//$sqlq = "select * from courses group by testyear";
$product = (isset($_POST['product']))?$_POST['product']:'';
$productname = (isset($_POST['productname']))?$_POST['productname']:'';
$batchnumber = (isset($_POST['batchnumber']))?$_POST['batchnumber']:'';
$from = (isset($_POST['from']))?$_POST['from']:'';
$to = (isset($_POST['to']))?$_POST['to']:'';


$sqlq = "select "
        . "product,"
        . "product_name,"
        . "batch_number,"
        . "YEAR(process_order_creation_date) as order_creation_year,"
        . "QUARTER(process_order_creation_date) as order_creation_quarter,"
        . "MONTH(process_order_creation_date) as order_creation_month,"
        . "WEEK(process_order_creation_date) as order_creation_week,"
        . "avg(po_create_po_release) as bar1,"    //PO Create to PO Release
        . "avg(po_release_to_pkg_start) as bar2," //PO Release to Pkg Start
        . "avg(pkg_start_pkg_finish) as bar3, "    //Pkg Start to Pkg Finish
        . "avg(pkg_finish_pkg_final_check) as bar4, "     //BRR Begin To BRR Finish
        . "avg(pkg_final_check_brr_begin) as bar5," //BRR Finish to QP Release
        . "avg(brr_begin_brr_finish) as bar6, "
        . "avg(brr_finish_qp_release) as bar7 "
        . "from roche_new ";
$where = '  WHERE 1=1 ';
if($from!='' && $to!=''){
$where .= ' and process_order_creation_date
    BETWEEN CAST("'.$from.'" AS DATE)
        AND CAST("'.$to.'" AS DATE) ';
}
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



$order = '';
$order = ' ORDER by product';

$sqlq = $sqlq.$where.$group.$order;
//echo $sqlq;exit;
$query = mysqli_query($sql,$sqlq);
$count = mysqli_num_rows($query);

if($batchnumber){
    $myurl[] = array('Batch Number','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['batch_number'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}else if($productname){
    $myurl[] = array('Batch Number','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['batch_number'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}else if($product){
    $myurl[] = array('Product Name','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['product_name'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}else{
    $myurl[] = array('Product','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['product'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}

echo json_encode($myurl);
?>








