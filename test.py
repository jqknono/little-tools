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

from math import log10, floor

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x)))))

def test():
    # stat_platform_ios()
    stat_platform_android()
    data17= query_xi_back_gun()
    # print(query_active_users())
    # print(query_xi_ecpm())
    # print(query_xi_ecpm(country_us))
    print(round_sig(data17['num_video_played']/data17['people_num_watch_video']))

test()

def test3():
    # stat_platform_ios()
    stat_platform_ios()
    print(query_xi_back_gun())
    # print(query_active_users())

# test3()

