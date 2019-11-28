import smtplib  
from datetime import datetime
class sending:
	def __init__(self,obj_to):
		self.tomail = str(obj_to.email)
		self.obj = obj_to
	
	def start(self):
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls()
		username = 'email@example.com'
		password = 'password'
		s.login(username, password) 
		message = "You just logged out.\n\nYour details.\nName : "+self.obj.firstname + " " + self.obj.lastname +"\n"+ "Email : "+self.obj.email +"\nPhone: "+self.obj.phone_num+"\nCheckin time: "+((self.obj.check_in).strftime('%Y-%m-%d %H:%M:%S'))+"\nCheckout time: "+(self.obj.check_out.strftime('%Y-%m-%d %H:%M:%S'))
		print(message)
		s.sendmail(username, self.tomail, message)  
		s.quit()
