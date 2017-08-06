import MySQLdb

file = open("competitions.html","w")
header = """
<!DOCTYPE html>
<html lang="en">

	<head>

		<title>Cubing Kerala</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

	</head>

	<body>

		<!--Navbar-->
		<div id="nav"></div>
		<script src="./insertNav.js"></script>

		<div style="margin-left: 25px">
			<h4>List of past and upcoming WCA Official Competitions in Kerala</h4>
			<p>Note: The official details of competitions are extracted from official <a href="www.worldcubeassociation.org">WCA site</a>.</p>
		</div>
		<table class="table" style="margin-left: 25px">
			<thead>
				<tr>
					<th>Competition Name</th>
					<th>Date</th>
					<th>Number of Participants</th>
				</tr>
			</thead>
			<tbody>
"""
footer = """
			</tbody>
		</table>
	</body>

</html>
"""
content = ""
print('Connecting to MySQL...')
db = MySQLdb.connect(host="localhost", user="dany", passwd="emmaus", db="wca")
print('Connected to MySQL.')
cur = db.cursor()
for id in open("competitionsID.dat","r").readlines():
	content += '<tr>'
	cur.execute("select name,year,month,day,endMonth,endDay from Competitions where id='" + id.strip() +"'")
	row = cur.fetchone()
	content += '<td><a href="https://www.worldcubeassociation.org/competitions/' + id +'">' + row[0] + '</a></td>'
	date = "";
	date += str(row[1]) + " "
	month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	date += month_lst[row[2]-1] + " " + str(row[3])
	if (row[2] == row[4]):
		if (row[3] != row[5]):
			date += "-" + str(row[5])
	else:
		date += "-" + month_lst[row[4]-1] + " " + str(row[5])
	content += '<td>' + date + '</td>'
	cur.execute("select count(distinct personId) from Results where competitionId='" + id.strip() + "'");
	row = cur.fetchone()
	content += '<td>' + str(row[0]) + '</td>'
	content += '</tr>'
file.write(header)
file.write(content)
file.write(footer)