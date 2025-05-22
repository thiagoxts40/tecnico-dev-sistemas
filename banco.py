#pip install mysql-connector-python (para instalar o import)
#para se conectar ao banco de dados
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database="mydatabase"
)
#print(mydb)
#para executar os comendos do banco de dados
mycursor = mydb.cursor()
'''
mycursor.execute('create database if not exists mydatabase')
mycursor.execute("show databases")
for x in mycursor:
    print(x)'''
ArtistTableSql = '''create table if not exists artists(
ID int (20) primary key auto_increment,
Name char(20) not null,
Track char(10))'''
mycursor.execute(ArtistTableSql)
'''insert1="insert into artists(name,track) values('Edson','Eurodance');"
insert2="insert into artists(name,track) values('fernanda','sertanejo');"
mycursor.execute(insert1)
mycursor.execute(insert2)
mydb.commit()'''
mycursor.execute("select * from artistis;")
rows = mycursor.fetchall()
for row in rows
    print(f"id:{row[0]}\nNome:{row1}\nEstilo:{row2}")
mydb.close()