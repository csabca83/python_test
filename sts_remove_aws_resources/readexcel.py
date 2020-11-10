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

        try:
            self.account_ID = int(sheet.cell_value(self.cell, self.account_column))
        except:
            self.account_ID = sheet.cell_value(self.cell, self.account_column)

        self.resource_ID = sheet.cell_value(self.cell, self.resource_column)

    def check_items(self):
        if len(str(self.account_ID)) == 12 and self.account_ID != "":
            if self.resource_ID != "":

                #print("Value found.")

                return int(self.account_ID), self.resource_ID

            else:

                print(f"No value was given for the: {self.account_ID}")

        else:
            print(f"Incorrect account number for the following cell value: {self.resource_ID}")

            return "None"