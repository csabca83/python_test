from boto3_functions import Boto3_functions as b3
from readexcel import Readexcel as rx
from sts import sts_request as sr
from ping import ping_request as pr

path = "collection_of_key_values.xlsx"
resource_column = 0
account_column = 1
cell = 3

r = rx(resource_column, account_column, cell, path)
r.reading_items()
checked = r.check_items()
print(checked)

#TODO