'use strict';

var mysql = require("mysql");
var connection = mysql.createPool({
host: "localhost",
user: "dany",
password: "emmaus",
database: "wca",
multipleStatements: true
});

exports.getMembers = function(req, res) {
  var query = `
  select p.name as name, k.id as id, count(distinct r.competitionId) as compCount
  from KeralaCubers k, Results r, Persons p
  where k.id = r.personId and p.id = k.id
  group by p.name, k.id;
  `;
  connection.query(query, function(err, rows) {
    if (!err) {
      res.json({
        success: true,
        rows: rows
      });
    } else {
      res.json({
        success: false
      });
    }
  });
};