from peewee import *

db = SqliteDatabase('forum.db')

class User(Model):
	full_name = CharField()
	username=CharField()
	password =CharField()
	email_id= CharField()


	class Meta:
		database = db # This model uses the "forum.db" database.

class Question(Model):
	user_id = ForeignKeyField(User, backref='Questions')
	Posted_Questions = TextField()
	
	timestamp = TimestampField()

	class Meta:
		database = db

class Answer(Model):
	user_id = ForeignKeyField(User, backref='Answers')
	question_id= ForeignKeyField(Question, backref='Answers')
	Posted_Answers = TextField()
	likes=IntegerField()
	dislikes=IntegerField()
	timestamp = TimestampField()

	class Meta:
		database = db

if __name__ == '__main__':    
	#runs only when models.py is executed
	#won't run when models.py is imported 
	db.connect()
	db.create_tables([User, Question,Answer])