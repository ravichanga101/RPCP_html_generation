import json

with open('list.json') as f:
    data = json.load(f)

file_name = "table_listing.html"
f = open(file_name, 'w')

mytable_header = f"""   <table border="1">
                            <tr>
                                <th>  # </th>
                                <th> Name </th>
                                <th> Image </th>
                                <th> Details </th>
                            </tr>
                    """
tbl_trs = ''

for i in data['table_listing']:

    for ele in i:
        tbl_tr = ''
        tbl_tr += "<tr>"

        tbl_tr += "<td>"
        tbl_tr += ele
        tbl_tr += "</td>"

        tbl_tr += "<td>"
        tbl_tr += i[ele]['name']
        tbl_tr += "</td>"

        tbl_tr += "<td>"
        tbl_tr += "<img src=" + i[ele]['image_url'] + ">"
        #tbl_tr += i[ele]['image_url']
        tbl_tr += "</td>"

        tbl_tr += "<td>"
        tbl_tr += "<a href='index.php?v=" + \
            i[ele]['unique_code']+"'> View Details </a>"
        tbl_tr += "</td>"

        tbl_tr += "</tr>"
        tbl_trs += tbl_tr


mytable = mytable_header + tbl_trs + "</table>"
# print(mytable)

html_template = f'''<html>
<head>
<title> Title </title>
</head>
<body>
<h2> Welcome To RPCP</h2>
{mytable}
</body>
</html>'''.format(i, mytable)

f.write(html_template)
f.close()
