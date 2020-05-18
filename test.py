import sqlite3
#CREATED BY JAYD

class use_goods:
	def __init__(self,name): #ENTER THE NAME OF THE DATABASE AS ARGUMENT
		
		mydb= sqlite3.connect(name + '.db')

		mycursor = mydb.cursor()
	
		mycursor.execute("""CREATE TABLE IF NOT EXISTS GOODS(
							ITEM_NO INTEGER,
							ITEM_NAME TEXT,
							QTY INTEGER,
							RATE REAL
						)""")
		mycursor.execute("""CREATE TABLE IF NOT EXISTS EMPLO(
							ID_NO INTEGER,
							NAME TEXT,
							PHNO INTEGER,
							DEPT TEXT
						)""")
		self.mydb = mydb
		self.mycursor = mycursor
		
	def insert_items_goods(self,item_num,name,qty,price):	#ENTER ITEM NUMBER, ITEM NAME, QTY, PRICE AS ARGUMENT
		self.mycursor.execute('INSERT INTO GOODS VALUES(:no,:name,:qty,:price)',{'no':item_num, 'name':name,'qty':qty,'price':price })

		
		self.mydb.commit()
		self.mydb.close()
	def update_items_goods_remove(self,item_num,qty):   #ENTER ITEM NUMBER AND QUANTITIES TO BE REMOVED AS ARGUMENT
		self.mycursor.execute("""UPDATE GOODS
								SET QTY=QTY-:qty
								WHERE ITEM_NO=:item""",{'qty':qty,'item':item_num})
		self.mydb.commit()
	def update_items_goods_add(self,item_num,qty):   #ENTER ITEM NUMBER AND QUANTITIES TO BE ADDED AS ARGUMENT
		self.mycursor.execute("""UPDATE GOODS
								SET QTY=QTY+:qty
								WHERE ITEM_NO=:item""",{'qty':qty,'item':item_num})
		self.mydb.commit()
		self.mydb.close()


	def insert_items_emplo(self,id_no,name,phno,dept):	#ENTER ID,NAME, PHNO, DEPT AS ARGUMENT
		self.mycursor.execute('INSERT INTO EMPLO VALUES(:id_no,:name,:phno,:dept)',{'id_no':id_no, 'name':name,'phno':phno,'dept':dept })

		
		self.mydb.commit()
		self.mydb.close()

object1= use_goods('hen')
object1.update_items_goods_add(125,50)	