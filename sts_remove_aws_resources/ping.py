def ping_request():
   import boto3
   import getpass
   import requests
   import sys
   from requests.packages.urllib3.exceptions import InsecureRequestWarning

   # disables warning for insecure web calls for gathering credentials
   requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

   ADUser = #input("Input your ad name (no domain): ")
   ADPassword = #getpass.getpass("Input Password: ")
   AccountNumber = #input("Input the account number to get credentials for: ")
   RoleName = #input("Input the role name to get credentials for: ")

   # retrieves temp credentials from ping
   def creds(user, password, account, role):

       s = requests.Session()
       url = "<insert_ping_url>"
       payload = {"method":"usernameroleaccount","username":user,"password":password,"account":account,"role":role}
       req = requests.Request('POST', url, data=payload)
       prepped = req.prepare()

       resp = s.send(prepped,
           stream=True,
           verify=False
       )
       content = resp.content
       if (content.decode().startswith("ERROR")):
           print(content.decode())
           print("Credentials failed. please try again.")
           # quit script of credentials fail
           sys.exit()
       else:
           return content.decode().split(',')

   tempcreds = creds(ADUser, ADPassword, AccountNumber, RoleName)
   #print(tempcreds)
   access_key = tempcreds[2]
   secret_key = tempcreds[0]
   session_token = tempcreds[1]

   client = boto3.client("s3", aws_access_key_id=access_key,     aws_secret_access_key=secret_key,     aws_session_token=session_token)

   response = client.list_objects(Bucket='341254748130-ca-central-1-s3-logs')

   for objects in response:
       print(objects)
