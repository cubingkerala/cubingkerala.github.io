import MySQLdb

file = open("keralaCubers.html","w")
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
			<h4>List of Kerala Cubers who have participated in WCA Official Rubik's Cube Competitions</h4>
			<p>Note: The official details of Cubers and their results are extracted from official <a href="www.worldcubeassociation.org">WCA site</a>.</p>
			<p>If you are from Kerala and you have participated in WCA Competitions, please contact Cubing Kerala Admins at keralaspeedcubing@gmail.com along with the proof.</p>
		</div>
		<table class="table" style="margin-left: 25px">
			<thead>
				<tr>
					<th>Name</th>
					<th>WCA ID</th>
					<th>Number of Competitions</th>
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
cur.execute("""
select p.name as name, k.id as id, count(distinct r.competitionId) as compCount
from KeralaCubers k, Results r, Persons p
where k.id = r.personId and p.id = k.id
group by p.name, k.id;
""")
for row in cur.fetchall():
	content += '<tr>'
	content += '<td>' + row[0] + '</td>'
	content += '<td>' + row[1] + '</td>'
	content += '<td>' + str(row[2]) + '</td>'
	content += '</tr>'
file.write(header)
file.write(content)
file.write(footer)