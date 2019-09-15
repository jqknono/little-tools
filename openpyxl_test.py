import pandas
from datetime import date, datetime, timedelta
from xlutils.copy import copy
import openpyxl
from functions import *
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from copy import copy

# df = pandas.read_excel("工作簿1.xlsx",sheet_name="iOS")
# df.to_excel("工作簿2.xlsx",sheet_name="iOS",)

today = datetime.today()
yesterday = (today - timedelta(days=1)).strftime('%Y/%m/%d')
save_file_name = (today - timedelta(days=1)).strftime('%Y-%m-%d')

filename = "工作簿1.xlsx"
wb = openpyxl.load_workbook(filename)
# grab the active worksheet
ws = wb.active

columns = ws.max_column
rows = ws.max_row

###############
# 查数据
data = query_active_users()
###############

###############
# 填数据到excel
ws.append([   yesterday, 'iOS', data["昨天"][1], data['昨天'][0]         ])
###############

ws[f'A{rows+1}'].font = copy(ws[f'A{rows}'].font)
ws[f'B{rows+1}'].font = copy(ws[f'B{rows}'].font)
ws[f'C{rows+1}'].font = copy(ws[f'C{rows}'].font)

# Save the file
wb.save(f"fanfan-{save_file_name}.xlsx")
