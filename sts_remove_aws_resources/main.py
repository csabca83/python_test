from boto3_functions import Boto3_functions as b3
from readexcel import Readexcel as rx
from sts import sts_request as sr
from ping import ping_request as pr
import xlrd, os, sys

f = open("options.txt", "r+")
s = f.read()
what_to_do = input(s)

pr_creds = pr()
pr_access_key = pr_creds[0]
pr_secret_key = pr_creds[1]
pr_session_token = pr_creds[2]

path = "collection_of_key_values.xlsx" #input("Paste the file name and location here, if it's in the same folder as this script the filename + extension is enough: ")#"collection_of_key_values.xlsx"
resource_column = int(input("Type the number for the column where the resource is , for example: A1 would be 0, B3 would be 1: "))
account_column = int(input("Type the number for the column where the account ID is: "))

workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

for i in range(sheet.nrows):

    os.environ["AWS_ACCESS_KEY_ID"] = pr_creds[0]
    os.environ["AWS_SECRET_ACCESS_KEY"] = pr_creds[1]
    os.environ["AWS_SESSION_TOKEN"] = pr_creds[2]
    os.environ["AWS_DEFAULT_REGION"] = "ca-central-1"

    r = rx(resource_column, account_column, i, path)
    r.reading_items()
    checked = r.check_items()
    print(checked)
    if str(checked) == "None":
        print("----------------")
    else:
        try:

            RoleArn = (f"arn:aws:iam::{str(checked[0])}:role/<add_your_role>")
            sts_creds = sr(str(checked[0]), RoleArn)

            boto_function = b3(checked[0], checked[1])

            exec(f"boto_function.{what_to_do}()")

        except:
            print('\x1b[0;30;41m' + f"{sys.exc_info()[1]}" + '\x1b[0m')
            print("----------------")
