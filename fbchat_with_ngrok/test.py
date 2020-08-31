from queryexcel.queryxlsx import Readexcel

text_input = "szia"

r = Readexcel('C:\\Users\\Csaba\\Desktop\\VSC folder\\github\\python_test\\fbchat_with_ngrok\\queryexcel\\answers.xlsx')

r.import_excel()
r.append_items()
r.append_items_2(text_input)
r.find_answer()