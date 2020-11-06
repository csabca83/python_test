class Readexcel:

    def __init__(self, resource_column, account_column, cell, path):
        self.resource_column = resource_column
        self.cell = cell
        self.path = path
        self.account_column = account_column

    def reading_items(self):
        import xlrd
        workbook = xlrd.open_workbook(self.path)
        sheet = workbook.sheet_by_index(0)

        self.account_ID = int(sheet.cell_value(self.cell, self.account_column))
        self.resource_ID = sheet.cell_value(self.cell, self.resource_column)

        #return account_ID, resource_ID

    def check_items(self):
        if len(str(self.account_ID)) == 12 and self.account_ID != "":
            if "s3" in self.resource_ID:

                print("S3 resource found")

                return self.account_ID, self.resource_ID, "s3_remove"
                
            #elif:
                #TODO

            else:

                print(f"Uknown resource for this value: {self.resource_ID}")

        else:
            print(f"Incorrect account number for the following cell value: {self.account_ID}")