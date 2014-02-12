from celery import Celery
import sys
import getpass
import time
import requests
from splitBook import splitBookIntoPages
from requests.auth import HTTPBasicAuth

API_URL = "https://auphonic.com/api/simple/productions.json"
API_DETAILS_URL = "https://auphonic.com/api/production/%s.json"

app = Celery('tasks', broker='redis://localhost')

#@app.task
#def add(x, y):
#    return x + y
@app.task(name='wa.tasks.soundProcessingWithAuphonicTask')
def soundProcessingWithAuphonicTask(f):
	username = 'ashuven63@gmail.com'
	password = 'ashu177'
	preset = 'aPZCk3SVNZGPUfPGEgA76Q'
	data = {'preset': preset, 'action': 'start', }
	input_files = {}
	input_files['input_file'] = open(f, 'r')
	print "opened file"
	response_upload = requests.post(API_URL, data=data, files=input_files,auth=HTTPBasicAuth(str(username), str(password)))
	json_response = response_upload.json()
	uuid = json_response['data']['uuid']
	detail_url = API_DETAILS_URL % uuid
	headers = {'content-type': 'application/json'}
	getDetails = True
	noOfTries = 0
	while getDetails and noOfTries<5:
		detail_response_upload = requests.get(detail_url,headers=headers,auth=HTTPBasicAuth(str(username), str(password)))
		detail_object = detail_response_upload.json()
		print detail_object['data']['status_string']
		if detail_object['data']['status_string']=='Done':
			getDetails=False
			continue
		time.sleep(10)
		noOfTries=noOfTries+1
	download_url = detail_object['data']['output_files'][0]['download_url']
	#use this URL to download back into the server 
	print download_url		
	return 0

@app.task(name='wa.tasks.uploadSplitBookIntoGridFS')
def uploadSplitBookIntoGridFS(f):
	splitBookIntoPages(f)

    
