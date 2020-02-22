# -*- coding: utf-8 -*-

from functions import *
# 查数据
def test1():
    stat_platform_android()
    data = query_video()
    print(data)


def test2():
    # "2020-02-21 23:59:59"
    today_date = datetime.today()
    end_date_resp = (today_date - timedelta(days=3)).strftime('%Y%m%d00')
    print(end_date_resp)

test2()