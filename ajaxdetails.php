<?php
include('db.php');


if($_POST['level']==2){
    $sqlq = "select "
            . "product_name "
            . "from roche "
            . " where product = '".$_POST['product']."'"
            . "group by "
            . "product_name";
    //echo $sqlq;exit;
    $query = mysqli_query($sql,$sqlq);

    $options = "<option value=''>All</option>";
    while ($row = mysqli_fetch_assoc($query)) {
        //$product_name[] = $row['product_name'];
        $options .= "<option value='".$row['product_name']."'>".$row['product_name']."</option>";
    }
    echo $options;
    
}elseif($_POST['level']==3){
    $sqlq = "select "
            . "batch_number "
            . "from roche "
            . " where product_name = '".$_POST['product_name']."'"
            . "group by "
            . "batch_number";
    //echo $sqlq;exit;
    $query = mysqli_query($sql,$sqlq);

    $options = "<option value=''>All</option>";
    while ($row = mysqli_fetch_assoc($query)) {
        //$product_name[] = $row['product_name'];
        $options .= "<option value='".$row['batch_number']."'>".$row['batch_number']."</option>";
    }
    echo $options;
    
}

?>