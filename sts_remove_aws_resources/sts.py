def sts_request(account_ID, RoleArn):
    import boto3, os

    stsclient = boto3.client('sts')#, AccessKeyId=access_key, SecretAccessKey=secret_key, SessionToken=session_token)
    
    response = stsclient.assume_role(
        RoleArn=RoleArn,
        RoleSessionName="Mysession"
    )
    
    Access_key_sts = response['Credentials']['AccessKeyId']
    SecretAccessKey_sts = response['Credentials']['SecretAccessKey']
    SessionToken_sts = response['Credentials']['SessionToken']

    os.environ["AWS_ACCESS_KEY_ID"] = Access_key_sts
    os.environ["AWS_SECRET_ACCESS_KEY"] = SecretAccessKey_sts
    os.environ["AWS_SESSION_TOKEN"] = SessionToken_sts
