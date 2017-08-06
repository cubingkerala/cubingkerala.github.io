var eventID = document.getElementById('event').value;
var type = document.getElementById('type').value;
document.getElementById(eventID.toString() + type.toString()).style.display = 'block';
document.getElementById('button').onclick = function() {
	document.getElementById(eventID.toString() + type.toString()).style.display = 'none';
	eventID = document.getElementById('event').value;
	type = document.getElementById('type').value;
	document.getElementById(eventID.toString() + type.toString()).style.display = 'block';
}