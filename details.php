<?php
include('db.php');

$sqlq = "select "
        . " Product "
        . " from roche_felt_tb "
        . " group by "
        . "Product";
$query = mysqli_query($sql,$sqlq);

while ($row = mysqli_fetch_assoc($query)) {
    $products[] = $row['Product'];
}

?>








