import boto3

class Boto3_functions:

    def __init__(self, account_ID, resource_ID, access_key_id, secret_access_key, session_token):
        self.account_ID = account_ID
        self.resource_ID = resource_ID
        self.access_key_id = access_key_id 
        self.secret_access_key = secret_access_key 
        self.session_token = session_token

    def s3_remove(self):

        s3_client = boto3.client('s3', 
                                  aws_access_key_id = self.access_key_id, 
                                  aws_secret_access_key = self.secret_access_key, 
                                  aws_session_token = self.session_token)

        try:
            objects = s3_client.list_objects(Bucket=self.resource_ID)["Contents"]

            for items in objects:
                s3_client.delete_object(Bucket=self.resource_ID, Key = items["Key"])
                print('\x1b[6;30;42m' + f'{items["Key"]} deleted.' + '\x1b[0m')
        except KeyError:
            print("No object was found.")

        bucket = boto3.resource('s3', 
                                 aws_access_key_id = self.access_key_id, 
                                 aws_secret_access_key = self.secret_access_key, 
                                 aws_session_token = self.session_token).Bucket(self.resource_ID)

        bucket.delete()
        print('\x1b[6;30;42m' + f"{self.resource_ID} bucket deleted." + '\x1b[0m')
        print("----------------")

    def cloudwatch_event_rule_delete(self):

        cerv = boto3.client('events', 
                             aws_access_key_id = self.access_key_id, 
                             aws_secret_access_key = self.secret_access_key, 
                             aws_session_token = self.session_token)

        try:
            cerv.disable_rule(Name=self.resource_ID)
            print('\x1b[6;30;42m' + f"{self.resource_ID} event rule disabled." + '\x1b[0m')

            target_IDs = cerv.list_targets_by_rule(Rule=self.resource_ID)
            

            for target in target_IDs['Targets']:
                target_ID = []
                target_ID.append(target['Id'])
                cerv.remove_targets(Rule=self.resource_ID,
                                    Ids=target_ID)

                print('\x1b[6;30;42m' + f"{target_ID[0]} target were removed from the role." + '\x1b[0m')     

            cerv.delete_rule(Name=self.resource_ID)

            print('\x1b[6;30;42m' + f"{self.resource_ID} event rule deleted." + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No event rule was found.")
            print("----------------")

    def lambda_remove(self):

        lambda_client = boto3.client('lambda', 
                                      aws_access_key_id = self.access_key_id, 
                                      aws_secret_access_key = self.secret_access_key, 
                                      aws_session_token = self.session_token)

        lambda_client.delete_function(FunctionName=self.resource_ID)
        print('\x1b[6;30;42m' + f"{self.resource_ID} lambda function deleted." + '\x1b[0m')
        print("----------------")

    def disable_kms(self):

        kms_client = boto3.client('kms', 
                                   aws_access_key_id = self.access_key_id, 
                                   aws_secret_access_key = self.secret_access_key, 
                                   aws_session_token = self.session_token)

        kms_client.disable_key(KeyId=self.resource_ID)

    def delete_log_group(self):

        log_group_client = boto3.client('logs', 
                                         aws_access_key_id = self.access_key_id, 
                                         aws_secret_access_key = self.secret_access_key, 
                                         aws_session_token = self.session_token)

        try:
            log_group_client.delete_log_group(logGroupName=self.resource_ID)
            print('\x1b[6;30;42m' + f"{self.resource_ID} cloudwatch log group deleted." + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No log group was found for the given name.")
            print("----------------")

    def delete_key_pair(self):

        ec2_client = boto3.client('ec2', 
                                   aws_access_key_id = self.access_key_id, 
                                   aws_secret_access_key = self.secret_access_key, 
                                   aws_session_token = self.session_token)
        key_pair_list = []
        key_pair_list.append(self.resource_ID)
        ec2_client.describe_key_pairs(KeyNames=key_pair_list)

        ec2_client.delete_key_pair(KeyName=self.resource_ID)
        print('\x1b[6;30;42m' + "Request for " + f"{self.resource_ID} ec2-keypair deletion was initiated." + '\x1b[0m')
        print("----------------")

    def delete_kms_alias(self):

        kms_client = boto3.client('kms', 
                                   aws_access_key_id = self.access_key_id, 
                                   aws_secret_access_key = self.secret_access_key, 
                                   aws_session_token = self.session_token)

        try:
            kms_client.delete_alias(AliasName=self.resource_ID)
            print('\x1b[6;30;42m' + f"{self.resource_ID} kms alias deleted." + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No ec2 key pair alias was found for the given key alias.")
            print("----------------")            

    def schedule_kms_deletion(self):

        kms_client = boto3.client('kms', 
                                   aws_access_key_id = self.access_key_id, 
                                   aws_secret_access_key = self.secret_access_key, 
                                   aws_session_token = self.session_token)
        try:
            kms_client.disable_key(KeyId=self.resource_ID)
            print('\x1b[6;30;42m' + f"{self.resource_ID} key disabled." + '\x1b[0m')
            deletion_days = 7
            kms_client.schedule_key_deletion(KeyId=self.resource_ID, 
                                             PendingWindowInDays=deletion_days)

            print('\x1b[6;30;42m' + f"{self.resource_ID} scheduled for deletion, the key will be deleted in {deletion_days} days." + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No ec2 key pair was found for the given Key ID.")
            print("----------------")

    def cancel_kms_deletion(self):

        kms_client = boto3.client('kms', 
                                   aws_access_key_id = self.access_key_id, 
                                   aws_secret_access_key = self.secret_access_key, 
                                   aws_session_token = self.session_token)

        kms_client.cancel_key_deletion(KeyId=self.resource_ID)

        print('\x1b[6;30;42m' + f"{self.resource_ID} scheduled deletion was cancelled." + '\x1b[0m')
        print("----------------")

    def enable_kms(self):

        kms_client = boto3.client('kms', 
                                   aws_access_key_id = self.access_key_id, 
                                   aws_secret_access_key = self.secret_access_key, 
                                   aws_session_token = self.session_token)
        try:
            kms_client.enable_key(KeyId=self.resource_ID)

            print('\x1b[6;30;42m' + f"{self.resource_ID} key enabled" + '\x1b[0m')
            print("----------------")

        except KeyError:
            print("No ec2 key pair was found for the given Key ID.")
            print("----------------")



