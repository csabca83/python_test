import boto3

class Boto3_functions:

    def __init__(self, account_ID, resource_ID):
        self.account_ID = account_ID
        self.resource_ID = resource_ID

    def s3_remove(self):

        s3_client = boto3.client('s3')

        try:
            objects = s3_client.list_objects(Bucket=self.resource_ID)["Contents"]

            for items in objects:
                s3_client.delete_object(Bucket=self.resource_ID, Key = items["Key"])
                print('\x1b[6;30;42m' + f'{items["Key"]} deleted.' + '\x1b[0m')
        except KeyError:
            print("No object was found.")

        bucket = boto3.resource('s3').Bucket(self.resource_ID)

        bucket.delete()
        print('\x1b[6;30;42m' + f"{self.resource_ID} bucket deleted." + '\x1b[0m')
        print("----------------")

    def cloudwatch_even_rule_disable(self):

        cerv = boto3.client('events')

        try:
            cerv.disable_rule(Name=self.resource_ID)
            print('\x1b[6;30;42m' + f"{self.resource_ID} event rule disabled." + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No event rule was found.")
            print("----------------")

    def lambda_remove(self):
        #TODO
        #Research what's the impact of deleting a lambda alias

        lambda_client = boto3.client('lambda')

        lambda_client.delete_function(FunctionName=self.resource_ID)

    def disable_kms(self):
        #TODO
        #Research what's the impact of deleting a KMS alias

        kms_client = boto3.client('kms')

        kms_client.disable_key(KeyId=self.resource_ID)

    def delete_log_group(self):

        log_group_client = boto3.client('logs')

        try:
            log_group_client.delete_log_group(logGroupName=self.resource_ID)
            print('\x1b[6;30;42m' + f"{self.resource_ID} cloudwatch log group deleted." + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No log group was found for the given name.")
            print("----------------")

    def delete_key_pair(self):

        ec2_client = boto3.client('ec2')

        try:
            ec2.delete_key_pair(KeyName=self.resource_ID)
            print('\x1b[6;30;42m' + f"{self.resource_ID} ec2-keypair deleted." + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No ec2 key pair was found for the given name.")
            print("----------------")
