var event = document.getElementById('event').value;
var type = document.getElementById('type').value;
document.getElementById(event.toString() + type.toString()).style.display = 'block';
document.getElementById('button').onclick = function() {
	document.getElementById(event.toString() + type.toString()).style.display = 'none';
	event = document.getElementById('event').value;
	type = document.getElementById('type').value;
	document.getElementById(event.toString() + type.toString()).style.display = 'block';
}