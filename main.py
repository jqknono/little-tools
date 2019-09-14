import requests
from const import *
from id import *
from datetime import datetime
from datetime import timedelta
from functions import *

# url = 'https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_chart_data?start_date=2019-08-10&end_date=2019-09-08&versions%5B%5D=&channels%5B%5D=&segments%5B%5D=&time_unit=daily&stats=active_users'
# https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_chart_data?start_date=2019-09-07&end_date=2019-09-14&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=active_users


def main():

    # step1: 查日活
    # data = query_active_users()
    # print(data)

    # step2: 获取启动次数
    # data = query_launches_times()
    # print(data)

    # step3: 获取次日留存
    data = query_retentions()
    print(data)


















if __name__ == "__main__":
    main()
    
