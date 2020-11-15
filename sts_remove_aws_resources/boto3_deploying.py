import boto3, os, json

class Deploying:

    def __init__(self, account_ID, resource_ID, access_key_id, secret_access_key, session_token):

        self.account_ID = account_ID
        self.resource_ID = resource_ID
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.session_token = session_token

    def create_iam_policies(self):

        # Create IAM client

        iam_client = boto3.client('iam', 
                                   aws_access_key_id = self.access_key_id, 
                                   aws_secret_access_key = self.secret_access_key, 
                                   aws_session_token = self.session_token)

        file_name = os.listdir('./POLICY_TO_CREATE_JSON/')[0]
        try:
            # Create a policy
            policy_path = ("./POLICY_TO_CREATE_JSON/" + f"{file_name}")

            file_name = file_name.replace('.json', "")

            with open(policy_path) as json_file:
                data = json.load(json_file)

            iam_client.create_policy(PolicyName=file_name,
                                     PolicyDocument=json.dumps(data))
            print('\x1b[6;30;42m' + f"Policy {file_name} was successfully deployed on the {self.account_ID}" + '\x1b[0m')

        except:
            print(f"{file_name} policy already exists on {self.account_ID}, skipping this step.")



