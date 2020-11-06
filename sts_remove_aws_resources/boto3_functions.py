class Boto3_functions:

    def __init__(self, account_ID, resource_ID):
        self.account_ID = account_ID
        self.resource_ID = resource_ID

    def s3_remove(self):
        import boto3

        s3_client = boto3.client('s3')

        try:
            objects = s3_client.list_objects(Bucket=self.resource_ID)["Contents"]

            for items in objects:
                s3_client.delete_object(Bucket=self.resource_ID, Key = items["Key"])
                print(f'{items["Key"]} deleted.')
        except KeyError:
            print("No object was found.")

        bucket = boto3.resource('s3').Bucket(self.resource_ID)

        bucket.delete()
        print(f"{self.resource_ID} deleted.")
        print("----------------")
