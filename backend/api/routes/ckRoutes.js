'use strict';

module.exports = function(app) {
  var restapis = require('../controllers/ckController');
  app.route('/getMembers').post(restapis.getMembers);
};