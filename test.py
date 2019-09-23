from functions import *
# 查数据

data = query_xi_back_gun()

print(data)
'{"app_name":["%(app_name)s"],"dateRange":["%(start_date)s","%(end_date)s"],"timeZone":"default","platform":[],"country":[],"breakdown":["app_name","date"]}'