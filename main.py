from openpyxl import workbook,load_workbook


book=load_workbook('Book.xlsx')
sheet= book.active

abc = sheet['A2'].value
print(f"Value in A1: {abc}")