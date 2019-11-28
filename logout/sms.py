import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'
class message:
	def __init__(self,obj_to):
		self.tosend = obj_to.phone_num
		self.obj = obj_to
	# get request
	def sendPostRequest(self,reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  		req_params = {'apikey':apiKey,'secret':secretKey,'usetype':useType,'phone': phoneNo,'message':textMessage,'senderid':senderId}
  		return requests.post(reqUrl, req_params)
	# get response
	def start(self):
		apikey=''#provide this
		secretkey=''#provide this
		phone_num=''#provide this
		message = "You just logged out.\n\nYour details.\nName : "+self.obj.firstname + " " + self.obj.lastname +"\n"+ "Email : "+self.obj.email +"\nPhone: "+self.obj.phone_num+"\nCheckin time: "+((self.obj.check_in).strftime('%Y-%m-%d %H:%M:%S'))+"\nCheckout time: "+((self.obj.check_out).strftime('%Y-%m-%d %H:%M:%S'))
		response = self.sendPostRequest(URL, apikey, secretkey, 'stage', self.tosend , phone_num,message)
		print(response.text)
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
