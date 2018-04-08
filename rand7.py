import pymysql  #import pymysql
import random as rand
 #open db


db= pymysql.connect(host="127.0.0.1",user="root",password="mysql",db="ccybexp6_itzed",charset='utf8')
winning_numbers = range( 456789, 456795 )
input_numbers = input("Input your lottery numbers ").split(",")

correct_guesses = sum(1 for inp_num in input_numbers if inp_num in winning_numbers)
cur = db.cursor()

sql = "select * from users AS t ORDER BY RAND() LIMIT 1;"
try:
    cur.execute(sql)    # تمام سوابق پرس و جو را دریافت کنید
    results = cur.fetchall()
    print("id","phone","name")
      # گذار از نتیجه


    for row in results :
        id = row[0]
        name = row[1]
        phone = row[2]
        print(id,name,phone)       
finally:
    db.close() #بستن اتصال

