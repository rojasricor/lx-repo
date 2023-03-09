const mysql = require("mysql");
// Coloca aquí tus credenciales
module.exports = mysql.createPool({
  host: "127.0.0.1",
  user: "admin",
  password: "admin",
  database: "tienda"
});