from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST']     = 'localhost'
app.config['MYSQL_USER']     = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB']       = 'flaskcontacts'
mysql = MySQL(app)

# Settings
app.secret_key = 'asdasdasad'

@app.route('/')
def index():
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contacts')
  data = cur.fetchall()
  return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone    = request.form['phone']
    email    = request.form['email']
    cur      = mysql.connection.cursor()
    cur.execute('INSERT INTO contacts VALUES(NULL, %s, %s, %s)', (fullname, phone, email))
    mysql.connection.commit()
    flash('Contact Added Succesfully')
    return redirect(url_for('index'))

@app.route('/edit/<id>')
def get_contact(id):
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contacts WHERE id = %s', (id,))
  data = cur.fetchone()
  return render_template('edit.html', contact = data)

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone    = request.form['phone']
    email    = request.form['email']
    cur      = mysql.connection.cursor()
    cur.execute("""
      UPDATE contacts SET
        fullname = %s,
        email = %s,
        phone = %s
      WHERE id = %s
    """, (fullname, phone, email, id))
    mysql.connection.commit()
    flash('Contact Updated Succesfully')
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_contact():
  if request.method == 'POST':
    id = request.form['id']
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Contact Removed Succesfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(port = 3000, debug = True)
