import boto3
client = boto3.client('lambda')
response = client.invoke(FunctionName='sameer_test:1', InvocationType = 'RequestResponse', Payload = '{"id" : "39dcda76-a9f9-11e9-b1a9-12009e28c71e"}')
print ('response = ' + str(response))
p = response['Payload']
r = p.read()
print ('response.Payload = ' + str(r))
