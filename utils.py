import mysql.connector as mysql
mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="movies"
)

def doesUserExist(user):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `name`= '{}'".format(user)
    cur.execute(qry)
    result = cur.fetchone()
    return False if result is None else True

def registerUser(user, password):
    cur = mydb.cursor()
    sql = "INSERT INTO user (name, password) VALUES (%s, %s)"
    val = (user, password)
    cur.execute(sql, val)
    mydb.commit()
    print(cur.rowcount, "record inserted.")
    return True

def authenticateUser(user, password):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `name`= '{}' AND `password`= {}".format(user, password)
    cur.execute(qry)
    user = cur.fetchone()
    print(user)
    return False if user is None else True

