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
        #print(self.inputWorksheet.cell_value(3, 1))

    def append_items(self):
        self.bejovo_uzenetek = []
        self.index = []
        self.valasz_index = []
        self.random1 = []
        self.random2 = []
        self.index_int = []
        for y in range(1, self.inputWorksheet.nrows):
            self.bejovo_uzenetek.append(self.inputWorksheet.cell_value(y, 1))
            self.index.append(self.inputWorksheet.cell_value(y, 2))
            self.valasz_index.append(self.inputWorksheet.cell_value(y, 3))
            self.random1.append(self.inputWorksheet.cell_value(y, 4))
            self.random2.append(self.inputWorksheet.cell_value(y, 5))

        self.index_int = [int(i) for i in self.index]

        #print(self.bejovo_uzenetek)
        #print(self.index)
        #print(self.index_int)
        #print(self.valasz_index)
        #print(self.random1)
        #print(self.random2)

    def append_items_2(self, text_input):
        for i, items in enumerate(self.bejovo_uzenetek):
            if str.lower(text_input) in str.lower(items):
                #print(items)
                self.number_order = (i)
                #print(self.number_order)
                break
    
    def find_answer(self):
        self.answer_index = (self.index_int[self.number_order])
        random_answers = []
        for z in range(4, self.inputWorksheet.ncols):
            if self.inputWorksheet.cell_value(self.answer_index, z) == "":
                pass
            else:
                random_answers.append(self.inputWorksheet.cell_value(self.answer_index, z))

        #print(random_answers)
        self.random_answers = random.choice(random_answers)
        #print(self.random_answers)


#r = Readexcel('answers.xlsx')

#r.import_excel()
#r.append_items()
#r.append_items_2(text_input)
#r.find_answer()


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
