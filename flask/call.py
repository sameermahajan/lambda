import requests

base_url = 'http://<public ip>:8080/samples'
response = requests.get(base_url)
print ('response = ' + str(response))
print ('response.text = ' + response.text)

response = requests.get(base_url + '/' + '39dcda76-a9f9-11e9-b1a9-12009e28c71e')
print ('response = ' + str(response))
print ('response.text = ' + response.text)
