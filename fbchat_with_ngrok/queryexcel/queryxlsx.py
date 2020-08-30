import random
import xlrd

class Readexcel:

    def __init__(self, path):
        self.path = path

    def import_excel(self):
        self.inputWorkbook = xlrd.open_workbook(self.path)
        self.inputWorksheet = self.inputWorkbook.sheet_by_index(0)
        #print(self.inputWorksheet.nrows)
        #print(self.inputWorksheet.ncols)
        print(self.inputWorksheet.cell_value(3, 1))

    def append_items(self):
        self.bejovo_uzenetek = []
        self.index = []
        self.valasz_index = []
        self.random1 = []
        self.random2 = []
        for y in range(1, self.inputWorksheet.nrows):
            self.bejovo_uzenetek.append(self.inputWorksheet.cell_value(y, 1))
            self.index.append(self.inputWorksheet.cell_value(y, 2))
            self.valasz_index.append(self.inputWorksheet.cell_value(y, 3))
            self.random1.append(self.inputWorksheet.cell_value(y, 4))
            self.random2.append(self.inputWorksheet.cell_value(y, 5))

        print(self.bejovo_uzenetek)
        print(self.index)
        print(self.valasz_index)
        print(self.random1)
        print(self.random2)


r = Readexcel('answers.xlsx')

r.import_excel()
r.append_items()

#path = 'answers.xlsx'

#inputWorkbook = xlrd.open_workbook(path)
#inputWorksheet = inputWorkbook.sheet_by_index(0)

#print(inputWorksheet.nrows)
#print(inputWorksheet.ncols)

#print(inputWorksheet.cell_value(1, 0))

#names = []
#scores = []

#for y in range(1, inputWorksheet.nrows):
#    names.append(inputWorksheet.cell_value(y, 0))
#    scores.append(inputWorksheet.cell_value(y, 1))

#print(names)
#print(scores)