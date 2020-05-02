import requests
def sendsms():
	pass
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=driver is drowsy, please alert him&language=english&route=p&numbers=6302613196,9642464607"
	headers = {
	'authorization': "LrWIhZgMBP7nR5lp83GstCdFiz0qSkKDQxOcN9vo6HEbV1aTm4FEcGyYN1UXzenxSrkKAJBf7RPIMbu6",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)
