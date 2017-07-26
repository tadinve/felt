<?php
include('db.php');
//$sqlq = "select * from courses group by testyear";
$product = (isset($_POST['product']))?$_POST['product']:'';
$productname = (isset($_POST['productname']))?$_POST['productname']:'';
$batchnumber = (isset($_POST['batchnumber']))?$_POST['batchnumber']:'';
$from = (isset($_POST['from']))?$_POST['from']:'';
$to = (isset($_POST['to']))?$_POST['to']:'';
 /*select 
 product
 , avg(if(datediff(process_order_release_date,process_order_creation_date)<0,0,datediff(process_order_release_date,process_order_creation_date))) as po_create_to_release 
 , avg(if(datediff(packaging_start_date,process_order_release_date)<0,0,datediff(packaging_start_date,process_order_release_date))) as po_release_to_pkg_start
 , avg(if(datediff(packaging_end_date,packaging_start_date)<0,0,datediff(packaging_end_date,packaging_start_date))) as pkg_start_pkg_finish
 , avg(if(datediff(packaging_head_pkg_signoff,packaging_end_date)<0,0,datediff(packaging_head_pkg_signoff,packaging_end_date))) as Pkg_Finish_to_Pkg_Final_Check
 , avg(if(datediff(bbr_start,packaging_head_pkg_signoff)<0,0,datediff(bbr_start,packaging_head_pkg_signoff))) as Pkg_Final_Check_to_BRR_Begin
 , avg(if(datediff(bbr_end,bbr_start)<0,0,datediff(bbr_end,bbr_start))) as BRR_Begin_To_BRR_Finish
 , avg(if(datediff(qa_release_date,bbr_end)<0,0,datediff(qa_release_date,bbr_end))) as BRR_Finish_to_QP_Release
 from 
 roche_modified 
 group by product;*/

$sqlq = "select "
        . "product,"
        . "product_name,"
        . "batch_number,"
        . "YEAR(process_order_creation_date) as order_creation_year,"
        . "QUARTER(process_order_creation_date) as order_creation_quarter,"
        . "MONTH(process_order_creation_date) as order_creation_month,"
        . "WEEK(process_order_creation_date) as order_creation_week,"
        . "avg(if(datediff(process_order_release_date,process_order_creation_date)<0,0,datediff(process_order_release_date,process_order_creation_date))) as bar1,"    //po_create_to_release
        . "avg(if(datediff(packaging_start_date,process_order_release_date)<0,0,datediff(packaging_start_date,process_order_release_date))) as bar2," //po_release_to_pkg_start
        . "avg(if(datediff(packaging_end_date,packaging_start_date)<0,0,datediff(packaging_end_date,packaging_start_date))) as bar3, "    //pkg_start_pkg_finish
        . "avg(if(datediff(packaging_head_pkg_signoff,packaging_end_date)<0,0,datediff(packaging_head_pkg_signoff,packaging_end_date))) as bar4, "     //Pkg_Finish_to_Pkg_Final_Check
        . "avg(if(datediff(bbr_start,packaging_head_pkg_signoff)<0,0,datediff(bbr_start,packaging_head_pkg_signoff))) as bar5," //Pkg_Final_Check_to_BRR_Begin
        . "avg(if(datediff(bbr_end,bbr_start)<0,0,datediff(bbr_end,bbr_start))) as bar6, "//BRR_Begin_To_BRR_Finish
        . "avg(if(datediff(qa_release_date,bbr_end)<0,0,datediff(qa_release_date,bbr_end))) as bar7 " //BRR_Finish_to_QP_Release
        . "from roche_modified ";
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








