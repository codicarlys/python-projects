__version__ = '0.1.0'

import csv
from openpyxl import Workbook

def Csv_To_Excel():
    wb = Workbook()
    sheet = wb.active()
    file = open('file.csv', 'r')
    for row in csv.reader(file):
        sheet.append(row)

wb.save('output.xlsx')