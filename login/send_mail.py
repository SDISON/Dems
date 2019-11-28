import smtplib  

class sending:
	def __init__(self,obj_to):
		self.tomail = str(obj_to.email)
		self.obj = obj_to.visitor
	
	def start(self):
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		username = 'email@example.com'
		password = 'password'
		s.login(username, password) 
		message = "Someone wants to visit you.\n\nDetails of visitor.\nName of visitor: "+self.obj.firstname + " " + self.obj.lastname +"\n"+ "Email of visitor: "+self.obj.email +"\nVisitor Phone: "+self.obj.phone_num
		print(message)
		s.sendmail(username, self.tomail, message)    
		s.quit()
