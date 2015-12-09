import MySQLdb
mysql_config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'***',
    'port':3306,
    'database':'Center',
    'charset':'utf8',

}
def isset(v):
    try:
        type (eval(v))
    except:
        return False
    else:
        return True
def LoadFile():
    try:
        cnn = MySQLdb.connector.connect(**mysql_config)
        sql = "LOAD DATA LOCAL INFILE '/app/python-study/test.csv' REPLACE INTO TABLE Center.test FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"
        cursor = cnn.cursor()
        cursor.execute(sql)
        cnn.commit()
    except MySQLdb.connector.Error as e:
        print('LoadFile sql fails {}'.format(e))
    finally:
        if isset("cursor"):
            cursor.close()
        if isset("cnn"):
            cnn.close()
def LoadFile2():
    cnn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="hyd_db", charset="utf8")
    cursor = cnn.cursor()
    f = open("E:/bak/sql.txt", "r")
    for line in f:
        content = line.split(',')

        user_id = content[0]

        item_id = content[1]

        rating = content[2]

        print user_id,item_id,rating

        cursor.execute("insert into blog_blogpost(title,content,timestamp) values(%s,%s,%s)",(user_id,item_id,rating))

      #  sql = "LOAD DATA LOCAL INFILE 'E:/bak/sql.txt' REPLACE INTO TABLE hyd_db.blog_blogpost FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"

        cnn.commit()
if __name__ == "__main__":
    #    LoadFile()
        LoadFile2()