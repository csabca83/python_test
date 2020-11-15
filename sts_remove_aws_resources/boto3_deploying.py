import boto3, os, json, time

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

        policy_folder_items = os.listdir('./POLICY_TO_CREATE_JSON/')

        for items in range(len(policy_folder_items)):

            file_name = policy_folder_items[items]


            try:
                for_arn = file_name.replace('.json', "").strip()
                try:
                    iam_client.get_policy(PolicyArn=(f"arn:aws:iam::{self.account_ID}:policy/{for_arn}"))
                    print('\x1b[0;30;43m' + f"{for_arn} policy already exists on {self.account_ID}, skipping this step." + '\x1b[0m')
                except iam_client.exceptions.NoSuchEntityException:
                    time.sleep(2)
                    iam_client.get_policy(PolicyArn=(f"arn:aws:iam::{self.account_ID}:policy/{for_arn}"))
                    print('\x1b[0;30;43m' + f"{for_arn} policy already exists on {self.account_ID}, skipping this step." + '\x1b[0m')                    


            except:
                try:                    
                # Create a policy
                    policy_path = ("./POLICY_TO_CREATE_JSON/" + f"{file_name}")

                    file_name = (file_name.replace('.json', "")).strip()

                    with open(policy_path) as json_file:
                        data = json.load(json_file)

                    iam_client.create_policy(PolicyName=file_name,
                                            PolicyDocument=json.dumps(data))
                    print('\x1b[6;30;42m' + f"Policy {file_name} was successfully deployed on the {self.account_ID}" + '\x1b[0m')

                except iam_client.exceptions.EntityAlreadyExistsException:
                    print('\x1b[0;30;43m' + f"{for_arn} policy already exists on {self.account_ID}." + '\x1b[0m')
