from forumapp import *

while True:
	print("\n\n","-"*20)
	print("Choose an action. \n 1. Register \n 2. Login\n 3. Exit\n")
	choice=input("--> ")

	if choice =="1":
		user_register()
		

	elif choice=="2":
		
		user = login()
		
		while True:		
				
			if user:
				print("\n","-"*20)
				print("Choose an action. \n 1. Posts \n 2.Settings \n 3. Logout")
				choice1=input("-->")
			
				if choice1=="1":
					print("Choose an action. \n 1. Post Question \n 2. View Question \n  ")
					choice2=input("-->")
					if choice2=="1":
						content =input("Write your Question\n------------\n")
						post_ques(user, content)
					
					elif choice2=="2":
						view_ques()
						print("Choose an action. \n 1. Post Answer \n 2. View Answer \n  ")
						choice3=input("-->")
						if choice3=="1":
							ques_id=input("Enter question no. you want to answer-->")
							content =input("Write your Answer\n------------\n")
							post_ans(user, content, ques_id)
						elif choice3=="2":
							question_id=input("Choose your question by id -->")
							ans_check=view_ans(question_id)
							if ans_check != 0:
								ans_id= input("Choose an answer by ID --> ")
								get_ans_by_id(ans_id)
						else:
							continue
					

					else:
						continue
					

				elif choice1=="2":
					print("Choose an action. \n 1. Change password \n 2. Change email \n 3. Delete account ")
					choice4=input("-->")
					if choice4=="1":
						change_password(user)


					elif choice4=="2":
						change_email(user)

					elif choice4=="3":
						password1=input("Enter your password-->")
						del1=delete_account(user,password1)
						if del1 == 1:
							break

					
				elif choice1=="3":
					break

			else:
				break

			
	elif choice=="3":
		exit()
	else:
		exit()
