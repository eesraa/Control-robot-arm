from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/my-link/', methods=['POST'])
def my_link():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase2"
    )
    mycursor = mydb.cursor()
    R1 = request.form['R1']
    R2 = request.form['R2']
    R3 = request.form['R3']
    R4 = request.form['R4']
    R5 = request.form['R5']
    R6 = request.form['R6']
    if request.form.get('R7', False):
        R7 = 'On'
    else:
        R7 = 'Off'
    sql = "INSERT INTO engines (engine1, engine2, engine3, engine4, engine5, engine6, onoff) VALUES (%s, %s, %s, %s, %s,%s,%s)"
    val = (R1, R2, R3, R4, R5, R6, R7)
    mycursor.execute(sql, val)
    mydb.commit()
    return 'Success'
if __name__ == '__main__':
    app.run(debug=True)
    