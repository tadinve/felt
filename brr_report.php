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
    <style type="text/css">
        
        .panel.with-nav-tabs .panel-heading{
            padding: 5px 5px 0 5px;
        }
        .panel.with-nav-tabs .nav-tabs{
                border-bottom: none;
        }
        .panel.with-nav-tabs .nav-justified{
                margin-bottom: -1px;
        }
        /********************************************************************/
        /*** PANEL DEFAULT ***/
        .with-nav-tabs.panel-default .nav-tabs > li > a,
        .with-nav-tabs.panel-default .nav-tabs > li > a:hover,
        .with-nav-tabs.panel-default .nav-tabs > li > a:focus {
            color: #777;
        }
        .with-nav-tabs.panel-default .nav-tabs > .open > a,
        .with-nav-tabs.panel-default .nav-tabs > .open > a:hover,
        .with-nav-tabs.panel-default .nav-tabs > .open > a:focus,
        .with-nav-tabs.panel-default .nav-tabs > li > a:hover,
        .with-nav-tabs.panel-default .nav-tabs > li > a:focus {
            color: #777;
                background-color: #ddd;
                border-color: transparent;
        }
        .with-nav-tabs.panel-default .nav-tabs > li.active > a,
        .with-nav-tabs.panel-default .nav-tabs > li.active > a:hover,
        .with-nav-tabs.panel-default .nav-tabs > li.active > a:focus {
                color: #555;
                background-color: #fff;
                border-color: #ddd;
                border-bottom-color: transparent;
        }
        .with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu {
            background-color: #f5f5f5;
            border-color: #ddd;
        }
        .with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > li > a {
            color: #777;   
        }
        .with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > li > a:hover,
        .with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > li > a:focus {
            background-color: #ddd;
        }
        .with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > .active > a,
        .with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > .active > a:hover,
        .with-nav-tabs.panel-default .nav-tabs > li.dropdown .dropdown-menu > .active > a:focus {
            color: #fff;
            background-color: #555;
        }
    </style>
    <?php 
    include_once 'details.php';
    ?>
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
    <div class="container" style="margin-top:80px;">
        
    </div>
    <div class="container">
        <?php
            include('db.php');

            $sqli = "select product, "
                    . "sum(po_create_release) as po_sum"
                    . ", sum(release_to_pkg_start) as release_sum"
                    . ", sum(pkg_start_bbr_finish) as pkg_start_sum"
                    . ", sum(pkg_finish_begin) as pkg_finish_sum"
                    . ", sum(brr_start_finish) as brr_sum "
                    . ", sum(brr_finish_qp_release) as brrfinish_sum "
                    . "from roche group by product";

            $query = mysqli_query($sql,$sqli);
            while($result = mysqli_fetch_assoc($query))
            {
                $data[] = $result;
            }
            //echo "<pre>";print_r($data);
        ?>
        <table class="table table-striped">
            <tr>
                <th>&nbsp;</th>
                <th>Sum - PO create to release </th>
                <th>Sum - Release to Pkg Start</th>
                <th>Sum - PKG Finish to BRR Begin</th>
                <th>Sum - BRR Start to Finish</th>
                <th>Sum - BRR Start to Finish</th>
                <th>Sum - BRR Finish to QP Release</th>
            </tr>
            <?php foreach ($data as $key => $val){?>
            <tr>
                
                <td><?php echo $val['product'];?></td>
                <td><?php echo $val['po_sum'];?></td>
                <td><?php echo $val['release_sum'];?></td>
                <td><?php echo $val['pkg_start_sum'];?></td>
                <td><?php echo $val['pkg_finish_sum'];?></td>
                <td><?php echo $val['brr_sum'];?></td>
                <td><?php echo $val['brrfinish_sum'];?></td>
                
            </tr>
            <?php } ?>
        </table>      
        
    </div>
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
</body>
</html>