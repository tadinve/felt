<?php

$sql = mysqli_connect("localhost","root","");
if(!$sql)
{
	echo "Connection Not Created";
}
$con = mysqli_select_db($sql, "graphs");
if(!$sql)
{
	echo "Database Not Connected";
}

?>