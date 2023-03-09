from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'customers'
mysql = MySQL(app)

@app.route('/api/customers')
@cross_origin()
def getAllCustomers():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM customers")
	data = cur.fetchall()
	return jsonify(data)

@app.route('/api/customer/<int:id>')
@cross_origin()
def getCustomer(id):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM customers WHERE id = %s", [str(id)])
	result = cur.fetchall()
	return jsonify(result)

@app.route('/api/customer', methods = ['POST'])
@cross_origin()
def saveCustomer():
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO customers (firstname, lastname, email, phone, address) VALUES (%s, %s, %s, %s, %s)",
		(request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'], request.json['address']))
	mysql.connection.commit()
	return 'Saved client'

@app.route('/api/customer', methods = ['PUT'])
@cross_origin()
def updateCustomer():
	cur = mysql.connection.cursor()
	cur.execute("UPDATE customers SET firstname = %s, lastname = %s, email = %s, phone = %s, address = %s WHERE customers.id = %s",
		(request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'], request.json['address'], request.json['id']))
	mysql.connection.commit()
	return 'Updated client'

@app.route('/api/customer/<int:id>', methods = ['DELETE'])
@cross_origin()
def removeCustomer(id):
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM customers WHERE customers.id = %s", [str(id)])
	mysql.connection.commit()
	return 'Deleted client'

@app.route('/')
@cross_origin()
def index():
	return render_template('index.html')

@app.route('/<path:path>')
@cross_origin()
def publicFiles(path):
	return render_template(path)

if __name__ == '__main__':
	app.run(None, 3000, True)

