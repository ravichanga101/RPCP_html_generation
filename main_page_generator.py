import json

with open('./json/001.json') as f:
    data = json.load(f)

file_name = "table_data_demo.html"
f = open(file_name, 'w')


mytable_header = f"""   
                   <table class="table table-bordered text-center w-75" style=' width: 50%; margin: 0 auto !important;' >
                 """
tbl_trs = ''

# initialize variable
row_count = 0
tbl_tr = ''

# create table 
for k,v in data.items():
    
    if row_count == 0 :
        tbl_tr += '<tr>'
        tbl_tr += "<td colspan='2'>"
        tbl_tr += '<h3>'+v+'</h3>' # title
        tbl_tr += '</td>'
        tbl_tr += '</tr>'
    elif row_count == 1 :
        tbl_tr += '<tr>'
        tbl_tr += "<td colspan='2'>"
        tbl_tr += "<img src='./images/"+v+"' class='rounded mx-auto d-block ' width='5%' alt=''>" # image
        tbl_tr += '</td>'
        tbl_tr += '</tr>'
        
    else :    
        tbl_tr += "<tr>"
        tbl_tr += "<td scope='row' class='w-50'>"+k+" </td>"
        tbl_tr += "<td  style='text-align:left'>"+v+"</td>"
        tbl_tr += "</tr>"

    row_count = row_count + 1 # end for loop

mytable = mytable_header + tbl_tr + "</table>"

# create webpage
html_template = f'''<!doctype html><html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    
    <title>RPCP</title>
  </head>
  <body>
    
		

		<div class="header-body" style="min-height:240px; background:url('https://www.charusat.ac.in/rpcp/images/HG3.jpg') no-repeat; background-size:100% 170%;">
			<div id="sticky-wrapper" class="sticky-wrapper" style="height: 72px;"><nav class="navbar edu-navbar" style="width: 1349px;">
				<div class="container">
					<div class="navbar-header">
						<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<a href="#" class="navbar-brand data-scroll"><img src="https://www.charusat.ac.in/rpcp/images/rpcplogo-1.png  " alt="" style="height:80px;width:auto;"></a>
					</div>

					
				</div><!-- /.container -->
			</nav></div>

			<div class="container">
				<div class="row">
					<div class="col-md-12">
						<div class="intro-text ">
							<!--<h1>Herbal Garden</h1>-->
						</div>
					</div>
				</div><!-- /.row -->
			</div><!-- /.container -->
		</div>
	
    <div class="container-fluid table-responsive-md">
        <br/>
        {mytable}
        <br/>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>'''.format(mytable)

f.write(html_template)
f.close()
