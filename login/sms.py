import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'
class message:
	def __init__(self,obj_to):
		self.tosend = obj_to.phone_num
		self.obj = obj_to.visitor
	# get request
	def sendPostRequest(self,reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  		req_params = {'apikey':apiKey,'secret':secretKey,'usetype':useType,'phone': phoneNo,'message':textMessage,'senderid':senderId}
  		return requests.post(reqUrl, req_params)
	# get response
	def start(self):
		apikey=''#provide this
		secretkey=''#provide this
		phone_num=''#provide this
		message = "Someone wants to visit you.\n\nDetails of visitor.\nName of visitor: "+self.obj.firstname + " " + self.obj.lastname +"\n"+ "Email of visitor: "+self.obj.email +"\nVisitor Phone: "+self.obj.phone_num
		response = self.sendPostRequest(URL, apikey, secretkey, 'stage', self.tosend , phone_num,message)
		print(response.text)
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
