'use strict';

module.exports = function(app) {
  var restapis = require('../controllers/ckController');
  app.route('/test').post(restapis.test);
};