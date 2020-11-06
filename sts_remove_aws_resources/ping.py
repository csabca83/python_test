def ping_request():
    import getpass
    import requests
    import sys, os
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

    # disables warning for insecure web calls for gathering credentials
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    ADUser = '<ad user name>' #input("Input your ad name (no domain): ")
    ADPassword = '<ad password>' #getpass.getpass("Input Password: ")
    AccountNumber = '<account number>' #input("Input the account number to get credentials for: ")
    RoleName = '<role name>' #input("Input the role name to get credentials for: ")

    # retrieves temp credentials from ping
    def creds(user, password, account, role):

        s = requests.Session()
        url = "https://awsapi.us.aegon.com/default.aspx"
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

    return access_key, secret_key, session_token

