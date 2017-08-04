'use strict';

var mysql = require("mysql");
var connection = mysql.createPool({
host: "localhost",
user: "dany",
password: "emmaus",
database: "eawadDB",
multipleStatements: true
});

exports.test = function(req, res) {
  console.log("Hi");
};