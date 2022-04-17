import requests
import sys

def check(email):

	url = 'https://eu.api.mega.co.nz/cs'

	# data to send
	v1 = '[{"a":"ere","m":"'+email+'","v":2}]'

	# post request
	resp = requests.post('https://eu.api.mega.co.nz/cs', data=v1)
	
	# print the status
	if (resp.text == '[-11]' or resp.text == '[-9]' or resp.text == '[-2]'):
		print(resp.text + ": - "+email+" - Invalid Email\n")
		return 1
	elif (resp.text == '[{"val":1,"2fa":0}]'):
		print(resp.text + ": - "+email+" - Might be Working\n")
        
		return 0
	else:
		print(resp.text + ": - "+email+" - Not Worky Duuno the code\n")
		return 0
with open('emails.txt', 'r') as f:
    emails = [line.strip() for line in f]
    for email in emails:
        check(email)