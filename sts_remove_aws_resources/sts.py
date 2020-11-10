def sts_request(account_ID, RoleArn,  pr_access_key, pr_secret_key, pr_session_token):
    import boto3, os

    stsclient = boto3.client('sts', aws_access_key_id=pr_access_key, aws_secret_access_key=pr_secret_key, aws_session_token=pr_session_token)#, AccessKeyId=access_key, SecretAccessKey=secret_key, SessionToken=session_token)
    
    response = stsclient.assume_role(
        RoleArn=RoleArn,
        RoleSessionName="cseregy",
        DurationSeconds=3600
    )
    
    Access_key_sts = response['Credentials']['AccessKeyId']
    SecretAccessKey_sts = response['Credentials']['SecretAccessKey']
    SessionToken_sts = response['Credentials']['SessionToken']

    return Access_key_sts, SecretAccessKey_sts, SessionToken_sts