<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Roche</title>
        <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="bootstrap/css/bootstrap-theme.min.css">
    </head>
    <body>
        <style type="text/css">
            * {
                -webkit-box-sizing: border-box;
                       -moz-box-sizing: border-box;
                            box-sizing: border-box;
                    outline: none;
            }

            .form-control {
                position: relative;
                font-size: 16px;
                height: auto;
                padding: 10px;
                &:focus {
                    z-index: 2;
                }
            }

            body {
               -webkit-background-size: cover;
                -moz-background-size: cover;
                -o-background-size: cover;
                background-size: cover;
            }

            .login-form {
                margin-top: 160px;
            }

            form[role=login] {
                color: #5d5d5d;
                background: #f2f2f2;
                padding: 50px 26px 26px 26px;
                border-radius: 10px;
                -moz-border-radius: 10px;
                -webkit-border-radius: 10px;
            }
            form[role=login] img {
                display: block;
                    margin: 0 auto;
                    margin-bottom: 35px;
            }
            form[role=login] input,
            form[role=login] button {
                    font-size: 18px;
                    margin: 16px 0;
            }
            form[role=login] > div {
                    text-align: center;
            }
    </style>
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
        </div>
    </nav>
    <div class="container">
        <div class="row" id="pwd-container">
            <div class="col-md-4"></div>
            <div class="col-md-4">
                <section class="login-form">
                    <form method="post" action="#" role="login">
                        <img src="roche-logo_1.png" class="img-responsive" alt="" />
                        <input type="text" class="form-control" id="username" placeholder="Username">
                        <input type="password" class="form-control" id="password" placeholder="Password">
                        <a href="dashboardlayout.php"class="btn btn-lg btn-primary btn-block">Log in with Roche credentials</a>
                    </form>
                </section>  
            </div>
            <div class="col-md-4"></div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
</body>
</html>