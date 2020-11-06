def sts_request(access_key, secret_key, session_token, account_ID, RoleArn):
    import boto3

    stsclient = boto3.client('sts', aws_access_key=access_key, aws_secret_access_key=secret_key, aws_session_token=session_token)

    response = stsclient.assume_role(
        RoleArn=RoleArn
    )
    
    Access_key_sts = response['Credentials']['AccessKeyId']
    SecretAccessKey_sts = response['Credentials']['SecretAccessKey']
    SessionToken_sts = response['Credentials']['SessionToken']

    return Access_key_sts, SecretAccessKey_sts, SessionToken_sts