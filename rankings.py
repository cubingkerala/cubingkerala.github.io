"""
select p.name,r.best,r.countryRank,r.continentRank,r.worldRank
from RanksSingle r, Persons p, KeralaCubers k
where k.id = p.id and r.personId = k.id and eventId='333'
order by r.countryRank
"""
import MySQLdb

def getStr(x,event,type):
	if (event == '333fm' and type == 'single'):
		return str(x)
	if (event == '333mbf'):
		missed = x % 100
		x = x / 100
		secs = x % 100000
		solved = 99 - x / 100000 + missed
		string = str(solved) + '/' + str(solved + missed) + ' ' + str(secs / 60) + ':' + str('%02d' % (secs % 60))
		return string
	millisecs = x % 100
	x = x / 100;
	secs = x % 60;
	mins = x / 60;
	string = str('%02d' % secs) + '.' + str('%02d' % millisecs);
	if (mins > 0):
		string = str(mins) + ':' + string;
	return string

file = open("rankings.html","w")
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
			<h4>Kerala Cubers Rankings</h4>
			<p>Note: The official details of Cubers and their results are extracted from official <a href="www.worldcubeassociation.org">WCA site</a>.</p>
			<p>If you are from Kerala and you have participated in WCA Competitions, please contact Cubing Kerala Admins at keralaspeedcubing@gmail.com along with the proof.</p>
			<form class="form-inline" onsubmit="return false;">
				<div class="form-group">
					<select class="form-control" id="event">
						<option value='333' selected='selected'>Rubik&#039;s Cube</option>
						<option value='222'>2x2x2 Cube</option>
						<option value='444'>4x4x4 Cube</option>
						<option value='555'>5x5x5 Cube</option>
						<option value='666'>6x6x6 Cube</option>
						<option value='777'>7x7x7 Cube</option>
						<option value='333bf'>3x3x3 Blindfolded</option>
						<option value='333fm'>3x3x3 Fewest Moves</option>
						<option value='333oh'>3x3x3 One-Handed</option>
						<option value='333ft'>3x3x3 With Feet</option>
						<option value='minx'>Megaminx</option>
						<option value='pyram'>Pyraminx</option>
						<option value='clock'>Rubik&#039;s Clock</option>
						<option value='skewb'>Skewb</option>
						<option value='sq1'>Square-1</option>
						<option value='444bf'>4x4x4 Blindfolded</option>
						<option value='555bf'>5x5x5 Blindfolded</option>
						<option value='333mbf'>3x3x3 Multi-Blind</option>
					</select>
				</div>
				<div class="form-group">
					<select class="form-control" id="type">
						<option value="single">Single</option>
						<option value="average">Average</option>
					</select>
				</div>
				<button id="button" class="btn btn-default">Go</button>
			</form>
		</div>
"""
footer = """
		</table>

		<script src="./rankings.js"></script>

	</body>

</html>
"""
content = ""
print('Connecting to MySQL...')
db = MySQLdb.connect(host="localhost", user="dany", passwd="emmaus", db="wca")
print('Connected to MySQL.')
events = ['333','222','444','555','666','777','333bf','333fm','333oh','333ft','minx','pyram','clock','skewb','sq1','444bf','555bf','333mbf']
cur = db.cursor()
for event in events:
	cur.execute("""
		select p.name,r.best,r.countryRank,r.continentRank,r.worldRank
		from RanksSingle r, Persons p, KeralaCubers k
		where k.id = p.id and r.personId = k.id and eventId='""" + event + """'
		order by r.countryRank
		""")
	content += '<table  id="' + event + 'single' +'" class="table" style="margin-left: 25px; display: none;">'
	content += """
			<thead>
				<tr>
					<th>Rank</th>
					<th>Name</th>
					<th>Result</th>
					<th>National Rank</th>
					<th>Asian Rank</th>
					<th>World Rank</th>
				</tr>
			</thead>
			<tbody>
	"""
	i = 0
	for row in cur.fetchall():
		i = i + 1
		content += '<tr>'
		content += '<td>' + str(i) + '</td>'
		content += '<td>' + row[0] + '</td>'
		content += '<td>' + getStr(row[1],event,'single') + '</td>'
		content += '<td>' + str(row[2]) + '</td>'
		content += '<td>' + str(row[3]) + '</td>'
		content += '<td>' + str(row[4]) + '</td>'
		content += '</tr>'
	content += '</tbody></table>'
	cur.execute("""
		select p.name,r.best,r.countryRank,r.continentRank,r.worldRank
		from RanksAverage r, Persons p, KeralaCubers k
		where k.id = p.id and r.personId = k.id and eventId='""" + event + """'
		order by r.countryRank
		""")
	content += '<table  id="' + event + 'average' +'" class="table" style="margin-left: 25px; display: none;">'
	content += """
			<thead>
				<tr>
					<th>Rank</th>
					<th>Name</th>
					<th>Result</th>
					<th>National Rank</th>
					<th>Asian Rank</th>
					<th>World Rank</th>
				</tr>
			</thead>
			<tbody>
	"""
	i = 0
	for row in cur.fetchall():
		i = i + 1
		content += '<tr>'
		content += '<td>' + str(i) + '</td>'
		content += '<td>' + row[0] + '</td>'
		content += '<td>' + getStr(row[1],event,'average') + '</td>'
		content += '<td>' + str(row[2]) + '</td>'
		content += '<td>' + str(row[3]) + '</td>'
		content += '<td>' + str(row[4]) + '</td>'
		content += '</tr>'
	content += '</tbody></table>'
# cur.execute("""
# select p.name as name, k.id as id, count(distinct r.competitionId) as compCount
# from KeralaCubers k, Results r, Persons p
# where k.id = r.personId and p.id = k.id
# group by p.name, k.id;
# """)
# for row in cur.fetchall():
# 	content += '<tr>'
# 	content += '<td>' + row[0] + '</td>'
# 	content += '<td>' + row[1] + '</td>'
# 	content += '<td>' + str(row[2]) + '</td>'
# 	content += '</tr>'
file.write(header)
file.write(content)
file.write(footer)