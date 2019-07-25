#This is the main script
from models1 import User, Question, Answer
from datetime import datetime

def user_register():
	full_name= input("Enter full name -->")
	username= input("Enter username -->")

	u=True

	while u==True:
		user2=User.select().where(User.username == username)
		if user2.exists():
			print("Username already exists!\n")
			username=input("Enter new username -->")
		else:
			break


	password=input("Enter password -->")
	email=input("Enter email --> ")
	v=True

	while v==True:
		email1=User.select().where(User.email_id == email)
		if email1.exists():
			print("Email id already exists!\n")
			email=input("Enter new email id -->")
		else:
			break
	user1=User(full_name=full_name, username=username, password=password, email_id=email)
	user1.save()
	if user1:
		print("Registration successful!")

def post_ques(user, content):
	entry=Question(Posted_Questions=content, user_id=user, timestamp=datetime.now())
	entry.save()
	if entry:
		print("question saved successfully!")

def post_ans(user,content,ques_id):
	
	#entry1=Question.select().where(Question.Posted_Questions == content)
	

	entry=Answer(Posted_Answers=content, user_id=user, timestamp=datetime.now(),question_id=ques_id, likes=0, dislikes=0)
	entry.save()
	if entry:
		print("answer saved successfully!")





def view_ques():
	entries = Question.select()

	print ("-"*20)

	for entry in entries:
		print (entry.id, entry.timestamp, entry.Posted_Questions,"...", sep="\t")
	print("-"*20)

def view_ans(question_id):
	entries = Answer.select().where(Answer.question_id==question_id)
	# entry2=Answer.select().where(Answer.question_id == question_id)

	if not  entries.exists():
		print("No answers posted yet!")
		return 0
	else:

		print ("-"*20)

		for entry in entries:
			print (entry.id, entry.timestamp, entry.Posted_Answers[:20],"...", sep="\t")
		print("-"*20)



def get_ans_by_id(ans_id):
	entry = Answer.select().where(Answer.id ==ans_id).get()
	print ("-"*20)
	print(entry.Posted_Answers)
	print ("-"*20)
	print("\nRate the answer:\n1. Like \n2. Dislike \n3. Can't say")
	choice5=input("--> ")
	if choice5=="1":
		likes = Answer.update(likes=Answer.likes + 1)
		likes.execute()
	elif choice5=="2":
		dislikes = Answer.update(dislikes=Answer.dislikes + 1)
		dislikes.execute()
	elif choice5 == "3":
		return 0

def change_password(user):
	user1=User.select().where(User.username == user)
	if user1.exists():
		password1=input("enter current password-->")
		if User.password==password1:
			new_password=input("enter new password-->")
			user1=User.update(password=new_password).where(User.username==user)
			user1.execute()
			print("password changed")
		else:
			print("incorrect password")
	else:
		return 0

def change_email(user):
	user1=User.select().where(User.username == user)
	if user1.exists():
		new_email=input("enter new email-->")
		user1=User.update(email_id=new_email).where(User.username==user)
		user1.execute()
		print("Email changed")
	else:
		return 0

def login():
	username = input("Enter Username -->")
	password = input("Enter Password -->")

	
	user=User.select().where(User.username == username)

	if not user.exists():
		print("incorrect credentials!\n")
		return 0

	if user.get().password == password:
		print("Logged in successfully!\n")
		return user.get()
		

	else:
		print("Incorrect password!\n")
		return 0