<?php
include('db.php');
//$sqlq = "select * from courses group by testyear";
$sqlq = "select "
        . "product "
        . "from roche "
        . "group by "
        . "product";
$query = mysqli_query($sql,$sqlq);

while ($row = mysqli_fetch_assoc($query)) {
    $products[] = $row['product'];
}

?>








