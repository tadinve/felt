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
        .divide {
            border-right: 1px solid #ccc;
            padding-right: 10px;
            margin-right: -10px;
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
                <li class="active"><a href="dashboardlayout.php">Dashboard</a></li>
                <li><a href="brr_report.php">BRR Priority Report</a></li>
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
        <div class="panel panel-default">
            <div class="panel-body">
                <div class="row">
                    <div class="col-lg-2 divide">
                        <label for="from">Show By:</label>
                        <div class="row">
                            <div class="col-lg-6">
                                <label class="radio-inline">
                                    <input type="radio" name="optradio" checked="checked" class="timeradio" value="year">Year
                                </label>
                            </div>
                            <div class="col-lg-6">
                                <label class="radio-inline">
                                    <input type="radio" name="optradio" class="timeradio" value="quarter">Quarter
                                </label>
                            </div>
                            <div class="col-lg-6">
                                <label class="radio-inline">
                                    <input type="radio" name="optradio" class="timeradio" value="months">Month
                                </label>
                            </div>
                            <div class="col-lg-6">
                                <label class="radio-inline">
                                    <input type="radio" name="optradio" class="timeradio" value="week">Week
                                </label>
                            </div>
                        </div>
                        
                    </div>                   
                    <div class="col-lg-2">
                        <label for="from">From:</label>
                        <input type="text" class="form-control" id="from">
                    </div>
                    <div class="col-lg-2 divide">
                        <label for="to">To:</label>
                        <input type="text" class="form-control" id="to">
                    </div>
                    <div class="col-lg-2">
                        <label for="to">Product:</label>
                        <select class="form-control" id="product">
                            <option value="">All</option>
                            <?php  foreach ($products as $product=>$val){?>
                            <option value="<?php echo $val;?>"><?php echo $val;?></option>
                            <?php } ?>
                        </select>
                    </div>
                    <div class="col-lg-2">
                        <label for="to">Product Name:</label>
                        <select class="form-control" id="product_name">
                            <option value="">All</option>
                        </select>
                    </div>
                    <div class="col-lg-2">
                        <label for="to">Batch:</label>
                        <select class="form-control" id="batch_number">
                            <option value="">All</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="panel with-nav-tabs panel-default">
            <div class="panel-heading">
                <ul class="nav nav-tabs">
                    <li class="active"><a href="#tab1default" data-toggle="tab">Tableau</a></li>
                    <li><a href="#tab2default" data-toggle="tab">Custom</a></li>
                    <li><a href="#tab3default" data-toggle="tab">Box Plot</a></li>
                </ul>
            </div>
            <div class="panel-body">
                <div class="tab-content">
                    <div class="tab-pane fade in active" id="tab1default">
                        <script type='text/javascript' src='https://us-east-1.online.tableau.com/javascripts/api/viz_v1.js'></script>
                        <div class='tableauPlaceholder' style='width: 80%;'>
                            <object class='tableauViz' width='100%' height='655' style='display:none;'>
                                <param name='host_url' value='https%3A%2F%2Fus-east-1.online.tableau.com%2F' /> 
                                <param name='site_root' value='&#47;t&#47;solivarlabsroche' />
                                <param name='name' value='Stackedchart3&#47;Sheet1' />
                                <param name='tabs' value='no' />
                                <param name='toolbar' value='yes' />
                                <param name='showAppBanner' value='false' />
                                <param name='showShareOptions' value='true' />
                            </object>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="tab2default">
                        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
                        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
                        <script type="text/javascript">
                            // Load the Visualization API and the piechart package.
                            google.charts.load('current', {'packages':['corechart']});
                            // Set a callback to run when the Google Visualization API is loaded.
                            google.charts.setOnLoadCallback(function(){
                                drawChart();
                            });

                            function drawChart(product='',productname='',batchnumber='',timeline='') {
                                
                                // Define the chart to be drawn.
                                var data1 = $.ajax({
                                    url: "roche.php",
                                    dataType: "json",
                                    async: false,
                                    data: { product: product,productname: productname,batchnumber: batchnumber,timeline:timeline},
                                    type: "POST"
                                }).responseText;

                                var data = google.visualization.arrayToDataTable(jQuery.parseJSON(data1));

                                var options = {
                                    //title: "BRR Finish to QP Release, BRR Start To Finish, PKG Finish to BRR Begin, Release to Pkg Start and PO Create to Release by Year and Product",
                                    vAxis: {title: "Product"},
                                    hAxis: {title: "Days", viewWindow: {min:0}},
                                    isStacked:true,
                                    width: 1200,
                                    height: 800,
                                    legend: { position: 'right', maxLines: 3 },
                                    bar: { groupWidth: '75%' },
                                };
                                /**/
                                var chart = new google.visualization.BarChart(document.getElementById('stackedbar_div'));
                                chart.draw(data, options);
                            }
                        </script>
                        <div id="stackedbar_div">
                            
                        </div>
                    </div>
                    <div class="tab-pane fade" id="tab3default">
                        <script type='text/javascript' src='https://us-east-1.online.tableau.com/javascripts/api/viz_v1.js'></script>
                        <div class='tableauPlaceholder' style='width: 1523px; height: 655px;'>
                            <object class='tableauViz' width='100%' height='655' style='display:none;'>
                                <param name='host_url' value='https%3A%2F%2Fus-east-1.online.tableau.com%2F' /> 
                                <param name='site_root' value='&#47;t&#47;solivarlabsroche' />
                                <param name='name' value='Stackedchart3&#47;Boxplot' />
                                <param name='tabs' value='no' />
                                <param name='toolbar' value='yes' />
                                <param name='showAppBanner' value='false' />
                                <param name='showShareOptions' value='true' />
                            </object>
                        </div>
                    </div>
                </div>
            </div>
        </div>    
        
    </div>
    
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>

<script src="bootstrap/js/bootstrap.min.js"></script>
<script type="text/javascript">
        $( document ).ready(function() {
            $('#product').change(function(){
                var URL = 'ajaxdetails.php';
                var input = {};
                var product = $('#product').val();
                input['product'] = product;
                input['level'] = 2;
                $.ajax({
                    method: "post",
                    url: URL,
                    dataType:'html',
                    data:input,
                    success : function(data){
                        $('#product_name').html('');
                        $('#product_name').html(data);
                        $('#stackedbar_chart').html('');
                        google.charts.load('current', {'packages':['corechart']});
                            // Set a callback to run when the Google Visualization API is loaded.
                        google.charts.setOnLoadCallback(function(){
                            drawChart(product);
                        });
                    }
                });

            });
            
            $('#product_name').change(function(){
                var URL = 'ajaxdetails.php';
                var input = {};
                var product = $('#product').val();
                var product_name = $('#product_name').val();
                input['product_name'] = product_name;
                input['level'] = 3;
                $.ajax({
                    method: "post",
                    url: URL,
                    dataType:'html',
                    data:input,
                    success : function(data){
                        $('#batch_number').html('');
                        $('#batch_number').html(data);
                        $('#stackedbar_chart').html('');
                        $('#stackedbar_chart').html('');
                        google.charts.load('current', {'packages':['corechart']});
                            // Set a callback to run when the Google Visualization API is loaded.
                        google.charts.setOnLoadCallback(function(){
                            drawChart(product,product_name);
                        });
                    }
                });

            });
            
            $('#batch_number').change(function(){
                var product = $('#product').val();
                var product_name = $('#product_name').val();
                var batch_number = $('#batch_number').val();
                
                google.charts.load('current', {'packages':['corechart']});
                            // Set a callback to run when the Google Visualization API is loaded.
                google.charts.setOnLoadCallback(function(){
                    drawChart(product,product_name,batch_number);
                });
                
            });
        });
         $(".timeradio").click(function() {
            //alert($(this).val());
            var product = $('#product').val();
            var product_name = $('#product_name').val();
            var batch_number = $('#batch_number').val();
            var timeline = $(this).val();
            google.charts.load('current', {'packages':['corechart']});
                        // Set a callback to run when the Google Visualization API is loaded.
            google.charts.setOnLoadCallback(function(){
                drawChart(product,product_name,batch_number,timeline);
            });
            
        });
    </script>
</body>
</html>