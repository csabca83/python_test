class Boto3_functions:

    def __init__(self, Access_key_sts, SecretAccessKey_sts, SessionToken_sts, account_ID, resource_ID):
        self.Access_key_sts = Access_key_sts
        self.SecretAccessKey_sts = SecretAccessKey_sts
        self.SessionToken_sts = SessionToken_sts
        self.account_ID = account_ID
        self.resource_ID = resource_ID

    def s3_remove(self):
        import boto3

        s3_client = boto3.resource('s3',
        aws_access_key=self.Access_key_sts,
        aws_secret_access_key=self.SecretAccessKey_sts,
        aws_session_token=self.SessionToken_sts
        )

        objects = s3_client.list_objects(Bucket=self.resource_ID)["Contents"]

        for items in objects:
            print(items["Key"])
            s3_client.delete_object(Bucket=self.resource_ID, Key = items["Key"])

        bucket = s3_client.Bucket(self.resource_ID)

        bucket.delete()
        print(f"{self.resource_ID} deleted.")