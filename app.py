from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

#set route for mainpage
@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM emp")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

#set route for add_user
@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        empname=request.form['empname']
        contacts=request.form['contacts']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("INSERT INTO emp(EMPNAME,CONTACT) VALUES (?,?)",(empname,contacts))
        con.commit()
        flash('User Added','success')
        return redirect(url_for('index'))
    return render_template("add_user.html")

 #set route for edit_user
@app.route("/edit_user/<string:empid>",methods=['POST','GET'])
def edit_user(empid):
    if request.method=='POST':
        empname=request.form['empname']
        contacts=request.form['contacts']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("UPDATE emp SET EMPNAME=?,CONTACT=? WHERE EMPID=?",(empname,contacts,empid))
        con.commit()
        flash('user updated','success')
        return redirect(url_for('index'))
    con=sql.connect("db_Web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM emp WHERE EMPID=?",(empid)) 
    data=cur.fetchone()
    return render_template('edit_user.html',datas=data) 


   #set route for delete
@app.route("/delete_user/<string:empid>",methods=['GET']) 
def delete_user(empid):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("DELETE FROM emp WHERE EMPID=?",(empid))
    con.commit()
    flash('User Deleted','danger')
    return redirect(url_for('index'))
if __name__=='__main__':
    app.secret_key='durga77'
    app.run(debug=True)       
    
    