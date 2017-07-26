<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Roche</title>
<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
<!-- Optional Bootstrap theme -->
<link rel="stylesheet" href="bootstrap/css/bootstrap-theme.min.css">
</head>
<body>
        <nav class="navbar navbar-default  navbar-fixed-top" >
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" style="padding:7px 0px 5px 15px;" href="#">
                    <img src="http://www.rocheindia.com/etc/docroot/corporate/common/img/roche-logo.png" style="display: inline-block;">
                    <span style="display: inline-block; padding-top: 10px; padding-left: 15px;" >FELT Dashboard</span>
                </a>
                
            </div>
            <div id="navbar" class="navbar-collapse collapse">
              <ul class="nav navbar-nav pull-right">
                <li><a href="home.php">Home</a></li>
                <li><a href="dashboardlayout.php">Dashboard</a></li>
                <li class="active"><a href="brr_report.php">BRR Priority Report</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
                       Welcome Guest &nbsp;<span class="caret"></span>
                    </a>

                    <ul class="dropdown-menu" role="menu">
                        <li><a href="index.php"><i class="fa fa-btn fa-sign-out pull-left"></i>Logout</a></li>
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </nav>
    <div class="row" style="margin-top:80px;">
        <?php
            include('db.php');

            $sqli = "select * "
                    . "from roche_new"
                    //. "where process_order_creation_date != '0000-00-00' "
                    . " order by process_order_creation_date limit 100";

            $query = mysqli_query($sql,$sqli);
            while($result = mysqli_fetch_assoc($query))
            {
                $data[] = $result;
            }
            //echo "<pre>";print_r($data);
        ?>
        <div class="col-lg-1">&nbsp;</div>
        <div class="col-lg-10">
        <table class="table table-striped table-bordered table-responsive">
            <tr>
                <th>&nbsp;</th>
                <th>Process Order Number</th>
                <th>Order Type (packaging or repackaging)</th>
                <th>Material Number</th>
                <th>Product Name</th>
                <th>Process Order Creation Date</th>
                <th>Batch Number</th>
                <th>Process Order Release Date</th>
                <th>Packaging Line  Start</th>
                <th>Packaging Line Finish</th>
                <th>Packaging  Final Check Date</th>
                <th>BRR Start Date</th>
                <th>BRR End Date</th>
                <th>QA Release Date</th>
            </tr>
            <?php foreach ($data as $key => $val){?>
            <tr>
                <td><?php echo $val['product'];?></td>
                <td><?php echo $val['process_order_number'];?></td>
                <td><?php echo $val['order_type'];?></td>
                <td><?php echo $val['material_number'];?></td>
                <td><?php echo $val['product_name'];?></td>
                <td><?php echo $val['process_order_creation_date'];?></td>
                <td><?php echo $val['batch_number'];?></td>
                <td><?php echo $val['process_order_release_date'];?></td>
                <td><?php echo $val['packaging_start_date'];?></td>
                <td><?php echo $val['packaging_end_date'];?></td>
                <td><?php echo $val['packaging_head_pkg_signoff'];?></td>
                <td><?php echo $val['bbr_start'];?>
                <td><?php echo $val['bbr_end'];?></td>
                <td><?php echo $val['qa_release_date'];?></td>
            </tr>
            <?php } ?>
        </table>      
        </div>
        <div class="col-lg-1">&nbsp;</div>
    </div>
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
</body>
</html>