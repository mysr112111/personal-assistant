
import pymysql

conn = pymysql.connect(
    host="rm-2zevp3447f602lb113o.mysql.rds.aliyuncs.com",
    port=3306,
    user="root",
    passwd="QWERTYUIOP521a!",
    db="assistant",
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
def query_user_by_username(username):
    sql = "select * from sys_user where username = %s"
    cur = conn.cursor()
    cur.execute(sql, [username])
    result = cur.fetchone()
    return result

def add_user(username,password):
    sql = "insert into sys_user (username,password) values (%s,%s)"
    cur = conn.cursor()
    cur.execute(sql, [username,password])
    conn.commit()

def query_message_by_user_id(user_id):
    sql = "select * from chat_message where user_id = %s order by message_time asc"
    cur = conn.cursor()
    cur.execute(sql, [user_id])
    list = cur.fetchall()
    return list

def add_chat_message(user_id,message,role,message_time):
    sql = "insert into chat_message (user_id,message,role,message_time) values (%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql, [user_id,message,role,message_time])
    conn.commit()