# flask
It contains a sample API based web service using flask. It also contains sample python code that calls this service.

- **getscore.py:** It is flask based service. It implements a couple of RESTful APIs. It runs the flask server on port 8080 and the public ip address of the machine.
                
- **call.py:** It is sample python code that calls the above service, gets the results and prints them.

# lambda_function
It contains a sample lambda function that calls above service.

- **sameer_test_lambda_function.py:** It is the hosted lambda function. It invokes the above service, gets the results and returns them 
    to its caller.

# lambda_invoke
It contains sample python code that invokes above lambda function.

- **invoke.py:** It invokes the above lambda function synchronously using boto3 library, gets the results and prints them
