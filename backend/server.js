var express = require('express'),
app = express(),
port = 8081,
mysql = require('mysql'),
bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(function (req, res, next) {
	res.setHeader('Access-Control-Allow-Origin', '*');
	res.header('Access-Control-Allow-Methods', 'POST, OPTIONS');
	res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
	res.header('Access-Control-Allow-Credentials', true);
	return next();
});

var routes = require('./api/routes/ckRoutes');
routes(app);

app.listen(port);

console.log('RESTful API server started on: ' + port);