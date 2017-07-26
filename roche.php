<?php
include('db.php');
//$sqlq = "select * from courses group by testyear";
$product = (isset($_POST['product']))?$_POST['product']:'';
$productname = (isset($_POST['productname']))?$_POST['productname']:'';
$batchnumber = (isset($_POST['batchnumber']))?$_POST['batchnumber']:'';
$from = (isset($_POST['from']))?$_POST['from']:'';
$to = (isset($_POST['to']))?$_POST['to']:'';


$sqlq = "select "
        . "Product,"
        . "Product_Name,"
        . "Batch_Number,"
        . "YEAR(PO_creation_date) as order_creation_year,"
        . "QUARTER(PO_creation_date) as order_creation_quarter,"
        . "MONTH(PO_creation_date) as order_creation_month,"
        . "WEEK(PO_creation_date) as order_creation_week,"
        . "avg(PO_Create_to_PO_Release) as bar1,"    //PO Create to PO Release
        . "avg(PO_Release_to_PKG_Start) as bar2," //PO Release to Pkg Start
        . "avg(PKG_Start_to_PKG_Finish) as bar3, "    //Pkg Start to Pkg Finish
        . "avg(PKG_Finish_to_PKG_Final_Check) as bar4, "     //BRR Begin To BRR Finish
        . "avg(Final_Check_to_BRR_Begin) as bar5," //BRR Finish to QP Release
        . "avg(BRR_Begin_to_BRR_Finish) as bar6, "
        . "avg(BRR_Finish_to_QP_Release) as bar7 "
        . "from roche_felt_tb ";
$where = '  WHERE 1=1 ';
if($from!='' && $to!=''){
$where .= ' and PO_creation_date
    BETWEEN CAST("'.$from.'" AS DATE)
        AND CAST("'.$to.'" AS DATE) ';
}
$group = ' group by ';

if($batchnumber){
    $where .= "and Batch_Number = '".$batchnumber."'";
     $group .= " Batch_Number " ;
}else if($productname){
    $where .= "and Product_Name = '".$productname."'";
    $group .= " Batch_Number " ;
}else if($product){
    $where .= "and Product = '".$product."'";
    $group .= " Product_Name " ;
}else{
    $group .= " Product " ;
}


$order = '';
$order = ' ORDER by Product';

$sqlq = $sqlq.$where.$group.$order;
//echo $sqlq;exit;
$query = mysqli_query($sql,$sqlq);
$count = mysqli_num_rows($query);

if($batchnumber){
    $myurl[] = array('Batch Number','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['Batch_Number'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}else if($productname){
    $myurl[] = array('Batch Number','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['Batch_Number'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}else if($product){
    $myurl[] = array('Product Name','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['Product_Name'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}else{
    $myurl[] = array('Product','PO Create to PO Release', 'PO Release to Pkg Start','Pkg Start to Pkg Finish','Pkg Finish to Pkg Final Check','Pkg Final Check to BRR Begin','BRR Begin To BRR Finish','BRR Finish to QP Release');
    if($count>0)
    while ($row = mysqli_fetch_assoc($query)) {
        $myurl[] = array($row['Product'],(int)$row['bar1'],(int)$row['bar2'],(int)$row['bar3'],(int)$row['bar4'],(int)$row['bar5'],(int)$row['bar6'],(int)$row['bar7']);
    }
}

    echo json_encode($myurl);
?>