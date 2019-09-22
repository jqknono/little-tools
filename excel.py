import pandas
from datetime import date, datetime, timedelta
from xlutils.copy import copy
import openpyxl
from functions import *
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, Color
from copy import copy

# df = pandas.read_excel("工作簿1.xlsx",sheet_name="iOS")
# df.to_excel("工作簿2.xlsx",sheet_name="iOS",)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

filename = "工作簿1.xlsx"
wb = openpyxl.load_workbook(filename)
# grab the active worksheet
ws = wb.active

columns = ws.max_column
rows = int(ws.max_row)

def assign_value(row,column,value):
    ws[f'{column}{row}'] = value
    ws[f'{column}{row}'].font = copy(ws[f'{column}{row-10}'].font)
  

today = datetime.today()
yesterday = (today - timedelta(days=1)).strftime('%Y/%m/%d')
save_file_name = (today - timedelta(days=1)).strftime('%Y-%m-%d')


###############
# 查数据
data = query_active_users()
data1 = query_morrow_retentions()
data2 = query_threedays_retentions()
data3 = query_sevendays_retentions()
data4 = query_launches_times()
data5 = query_video()
data6 = query_video_supplement()
data7 = query_iap_users()
data8 = query_unlock_business()
data9 = query_open_map2_users()
data10 = query_open_map3_users()
data11 = query_open_event()
data12 = query_claim_times()
data13 = query_iap_money()
data14 = calculate_iap_nums()
data15 = calculate_iap_money_sum()

#数据计算
value_E = data['昨天'][0] / data['昨天'][1]    # E列生命周期
value_L = data4 ['昨天'] / data['昨天'][0]     # L列日活启动次数
value_M = data5['昨天'][0]/ data['昨天'][0]    # M列日活视频次数
value_N = data5['昨天'][0]/ data5['昨天'][1]   # N列独立用户视频次数
value_O = data5['昨天'][1]/data['昨天'][0]     # O列视频用户覆盖率
value_X = data6['昨天']/data['昨天'][0]        # x列人均插频次数
value_Y = (data5['昨天'][0]+data6['昨天'])/data['昨天'][0]        # Y列人均视频+插频次数

value_z = data14                             # Z列内购次数

value_AA = data7['昨天']                      # AA列内购人数
value_AB = data15                             # AB列内购金额
value_AD = data14/data['昨天'][0]             # AD列日活人均付费次数
value_AE = data7['昨天']/data['昨天'][0]       # AE列日活付费率
value_AF = data15/data14                      # AF列单次付费价值
value_AG = data15/data['昨天'][0]              # AG列日活人均付费金额

value_AH = data8['昨天'][0]/data['昨天'][1]    # AH列新增用户解锁第5产业占比
value_AI = data8['昨天'][1]/data['昨天'][1]    # AI列新增用户解锁第10产业占比
value_AJ = data12['昨天']/data['昨天'][0]      # AJ列成功claim日活用户占比
value_AK = data9['昨天']/data['昨天'][0]       # AK列进入map2日活用户占比
value_AL = data10['昨天']/data['昨天'][0]      # AL列进入map3日活用户占比
value_AM = data11['昨天']/data['昨天'][0]      # AM列进入event日活用户占比






# 切换列数
new_row = rows + 1
row_I = new_row-1
row_J = new_row-3
row_K = new_row-7

# 填数据到excel

assign_value(new_row, 'A',yesterday)
assign_value(new_row, 'B','iOS')
assign_value(new_row, 'C',data['昨天'][1])
assign_value(new_row, 'D',data['昨天'][0])
assign_value(new_row, 'E',value_E)

assign_value(row_I, 'I',data1['昨天']/100)
assign_value(row_J, 'J',data2['昨天']/100)   
assign_value(row_K, 'K',data3['昨天']/100)       
assign_value(new_row, 'L',value_L)   
assign_value(new_row, 'M',value_M)    
assign_value(new_row, 'N',value_N)     
assign_value(new_row, 'O',value_O)

assign_value(new_row, 'X',value_X)
assign_value(new_row, 'Y',value_Y)
assign_value(new_row, 'Z',value_z)
assign_value(new_row, 'AA',value_AA)
assign_value(new_row, 'AB',value_AB)
assign_value(new_row, 'AD',value_AD)
assign_value(new_row, 'AE',value_AE)
assign_value(new_row, 'AF',value_AF)
assign_value(new_row, 'AG',value_AG)
assign_value(new_row, 'AH',value_AH)
assign_value(new_row, 'AI',value_AI)
assign_value(new_row, 'AJ',value_AJ)
assign_value(new_row, 'AK',value_AK)
assign_value(new_row, 'AL',value_AL)
assign_value(new_row, 'AM',value_AM)




# Save the file
wb.save(f"TBC3每日数据{save_file_name}.xlsx")
