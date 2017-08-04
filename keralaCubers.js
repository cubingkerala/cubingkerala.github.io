var url = 'https://52.34.39.20:8081/'
var xhttp = new XMLHttpRequest();
xhttp.open("POST", url + 'getMembers', true);
xhttp.onload = function() {
    var json = JSON.parse(xhttp.responseText);
    for (var i = 0; i < json.rows.length; i++) {
        document.getElementById('tbody').innerHTML += `
        <tr>
            <td>` + json.rows[i].name + `</td>
            <td>` + json.rows[i].id + `</td>
            <td>` + json.rows[i].compCount.toString() + `</td>
        </tr>
        `
    }
}
xhttp.setRequestHeader('Content-Type', 'application/json');
xhttp.send();