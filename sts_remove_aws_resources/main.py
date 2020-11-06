from boto3_functions import Boto3_functions as b3
from readexcel import Readexcel as rx
from sts import sts_request as sr
from ping import ping_request as pr
import xlrd

#TODO
#test the ping and make sure it returns the keys
#pr_creds = pr()
#pr_access_key = pr_creds[0]
#pr_secret_key = pr_creds[1]
#pr_session_token = pr_creds[2]
#sts_access_key = ""
#sts_secret_key = ""
#sts_session_token = ""

path = input("Paste the file name and location here, if it's in the same folder as this script the filename + extension is enough: ")#"collection_of_key_values.xlsx"
resource_column = int(input("Type the number for the column where the resource is , for example: A1 would be 0, B3 would be 1: "))
account_column = int(input("Type the number for the column where the account ID is: "))
name = "John"

workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

def s3_remove():
    print("Hello")

for i in range(sheet.nrows):
    r = rx(resource_column, account_column, i, path)
    r.reading_items()
    checked = r.check_items()
    print(checked)

    #TODO
    #RoleArn = (f"arn:aws:iam::{checked[0]}:role/<role_name>")
    #sts_creds = sr(pr_access_key, pr_secret_key, pr_session_token, checked[0], RoleArn)
    #sts_access_key = sts_creds[0]
    #sts_secret_key = sts_creds[1]
    #sts_session_token = sts_creds[2]
    #boto_function = b3(sts_access_key, sts_secret_key, sts_session_token, checked[0], checked[1])


    try:
        exec(f"{checked[2]}()")
        #exec(f"boto_function.{checked[2]}()")
    except:
        print("No function needs to be executed.")