import requests
from const import *
from id import *
from datetime import datetime
from datetime import timedelta
import json
from collections import namedtuple
from result import *
from urllib.parse import unquote
from hyper import HTTPConnection


g_product_id = id_tbc_ios
g_app_name = ""
g_bundle_id = ""
g_platform = ""
event_group_id_ad_interstitial_from = ""
event_group_id_watch_video = ""
event_group_id_buy_iap_total = ""
event_group_id_open_map2 = ""
event_group_id_open_map3 = ""
event_group_id_open_event = ""
event_group_id_show_claim = ""
event_group_id_unlock_business = ""

event_id_buy_iap_total = ""
event_id_show_claim = ""
event_id_unlock_business = ""
event_id_ad_play_action = ""
event_id_ad_play_event = ""
event_id_ad_play_map2 = ""
event_id_ad_play_map3 = ""

url_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=%(stats_type)s'
url_event_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&stats=%(stats_type)s&event_group_id=%(event_group_id)s'
url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&%(event_id)s&%(event_group_id)s&%(event_group_name)s&stats=%(stats_type)s&property_type=string'

today = datetime.today()
# today = today - timedelta(days=1)
interval = 8

cookies = {'JSESSIONID': '26A64F4332F1D3C22CFB9778FAA46811',
           'PHPSESSID': 'e25rks4rchtepldv23flhc7l82',
           'UM_distinctid': '16d10cf0765141-056e45dadb0c15-5373e62-240000-16d10cf0766e88',
           'isg': 'BHl5F5L7ANyeINyI5BmIkmxxiOWTLm1UkGz0TJuuxaAfIpm049KxCWJ7oG5xmgVw', 
           'uc_session_id': 'd521e33a-ddf0-4d6d-8ed3-a1d082639bd6',
           'um_lang': 'zh',
           'ummo_ss': 'BAh7CUkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjoGRVRbCEkiCVVzZXIGOwBGWwZvOhNCU09OOjpPYmplY3RJZAY6CkBkYXRhWxFpYmkxaVppAZppXGkSaQHzaQGTaT5pAGkKaXRJIhk4UVA3eElpcW1PaGRXdG1HUFpQawY7AFRJIhR1bXBsdXNfdWNfdG9rZW4GOwBGIj0xdVFkY1hjb3I2ZmtRXzI2bzVnMzYzd18wZTI2MGI3Yjc4Y2U0MjBkYjI5ODk4Yjk3MTk0ZjFkNUkiEF9jc3JmX3Rva2VuBjsARkkiMXdqZjBnY1EvLzYxazNTRnd6WFlOL3pTQlQ1M1Vxdk5vRXVmMTg0aGR6enM9BjsARkkiD3Nlc3Npb25faWQGOwBUSSIlMWU5NDQwZmE1NmY5Y2ZlYWVhYzUwNzg0MjllNzQyYmIGOwBG--4011cfd5b83413aedc5acc4244e0e8e6bb3d73f3',
           'umplus_uc_loginid': 'fangfang_ren',
           'umplus_uc_token': '1uQdcXcor6fkQ_26o5g363w_0e260b7b78ce420db29898b97194f1d5'
           }

query_xi_back_gun_connect_sid = unquote(
    's%3Ae_O5RJ8-rXFpEW91Ua7eKVSABBJEanws.w3NAuc1%2BI6Ni%2FDg%2BzuQ%2BZJ3zWwqdAytz0zYkzVkgRyM')

query_xi_ecpm_connect_sid = unquote(
    's%3Ae_O5RJ8-rXFpEW91Ua7eKVSABBJEanws.w3NAuc1%2BI6Ni%2FDg%2BzuQ%2BZJ3zWwqdAytz0zYkzVkgRyM')


def stat_platform_ios():
    global g_product_id
    global g_app_name
    global g_bundle_id
    global g_platform

    global event_group_id_ad_interstitial_from
    global event_group_id_watch_video
    global event_group_id_buy_iap_total
    global event_group_id_open_map2
    global event_group_id_open_map3
    global event_group_id_open_event
    global event_group_id_show_claim
    global event_group_id_unlock_business

    global event_id_buy_iap_total
    global event_id_show_claim
    global event_id_unlock_business
    global event_id_ad_play_action
    global event_id_ad_play_event
    global event_id_ad_play_map2
    global event_id_ad_play_map3

    event_group_id_ad_interstitial_from = '5b7289ddf43e4838c7000268'
    event_group_id_watch_video = '5b7289a4f43e487686000096'
    event_group_id_buy_iap_total = '5b84cc7ca40fa34b91000015'
    event_group_id_open_map2 = '5b84cc7ca40fa34b91000019'
    event_group_id_open_map3 = '5b9a2569b27b0a5cb8000054'
    event_group_id_open_event = '5b7289ddf43e4838c7000282'
    event_group_id_show_claim = '5b7289ddf43e4838c7000289'
    event_group_id_unlock_business = '5b7289ddf43e4838c7000295'

    event_id_buy_iap_total = '5b9f7401c37c58067735ebc0'
    event_id_show_claim = '5b7be0660237f6071568cc54'
    event_id_unlock_business= '5b7bdfa20237f6071568cc50'
    event_id_ad_play_action = '5b7a8b163665ca0789e82188'
    event_id_ad_play_event = '5b74f0b25a16bc074d5f2633'
    event_id_ad_play_map2 = '5b9f0bd60237f606c0aca277'
    event_id_ad_play_map3 = '5ba22b756e21cc6462bdafd3'

    g_product_id = id_tbc_ios
    g_app_name = app_name_tbc3_ios
    g_bundle_id = bundle_id_tbc3_ios
    g_platform = platform_tbc3_ios


def stat_platform_android():
    global g_product_id
    global g_app_name
    global g_bundle_id
    global g_platform

    
    global event_group_id_ad_interstitial_from
    global event_group_id_watch_video
    global event_group_id_buy_iap_total
    global event_group_id_open_map2
    global event_group_id_open_map3
    global event_group_id_open_event
    global event_group_id_show_claim
    global event_group_id_unlock_business

    global event_id_buy_iap_total
    global event_id_show_claim
    global event_id_unlock_business
    global event_id_ad_play_action
    global event_id_ad_play_event
    global event_id_ad_play_map2
    global event_id_ad_play_map3

    event_group_id_ad_interstitial_from = '5b3de4bca40fa3572900007d' # ok
    event_group_id_watch_video = '5b3de4bca40fa35729000065' # ok
    event_group_id_buy_iap_total = '5b7e21c5f43e48055e000042' # ok
    event_group_id_open_map2 = '5b7e2198b27b0a7a4200001b' # ok
    event_group_id_open_map3 = '5b9a23a1f29d983795000100' # ok
    event_group_id_open_event = '5b642551f29d98672d000163' # ok
    event_group_id_show_claim = '5b3eee9cf29d9833db0001db' # ok
    event_group_id_unlock_business = '5b3de4bca40fa35729000078' # ok 

    event_id_buy_iap_total = '5b7e764f3665cafb7b5fe340' # ok 
    event_id_show_claim = '5b44647cdd26ca4c8f4db5ad'  # ok 
    event_id_unlock_business= '5b44645e5a16bc136ebd03a1' # ok 
    event_id_ad_play_action = '5b446ca85a16bc136ebd03a8' # ok 
    event_id_ad_play_event = '5b63c9ce3665ca073aad10ff'  # ok 
    event_id_ad_play_map2 = '5b7e51d20abec661afcec361'  # ok
    event_id_ad_play_map3 = '5b9f5e589242950645e25132' # ok


    g_product_id = id_tbc_android
    g_app_name = app_name_tbc3_android
    g_bundle_id = bundle_id_tbc3_android
    g_platform = platform_tbc3_android


def query_active_users():
    try:
        """查日活/新增"""
        # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-06&end_date=2019-09-14&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=active
        stats_type = 'active'
        report_type = 'game_reports'
        end_date = today.strftime('%Y-%m-%d')
        start_date = (today - timedelta(days=interval)).strftime('%Y-%m-%d')
        url = url_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                            'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
        resp = requests.get(url=url, cookies=cookies)
        data = resp.json()
        return {"昨天": [data['stats'][1]['active'], data['stats'][1]['install']], "前天": [data['stats'][2]['active'], data['stats'][2]['install']], '八天前': [data['stats'][-1]['active'], data['stats'][-1]['install']]}
    except:
        print("ERROR:query_active_users")

def query_launches_times():
    """启动次数"""
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-06&end_date=2019-09-14&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=launches
    stats_type = 'launches'
    report_type = 'reports'
    end_date = today.strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=interval)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][1]['data'], "前天": data['stats'][2]['data'], '八天前': data['stats'][-1]['data']}


def query_morrow_retentions():
    """用户次日留存"""
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-09&end_date=2019-09-15&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=retentions
    stats_type = 'retentions'
    report_type = 'reports'
    end_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=9)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][-1]['retention_rate'][0], "前天": data['stats'][-2]['retention_rate'][0], '八天前': data['stats'][0]['retention_rate'][0]}


def query_threedays_retentions():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-04&end_date=2019-09-15&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=retentions
    stats_type = 'retentions'
    report_type = 'reports'
    end_date = (today - timedelta(days=4)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=11)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][7]['retention_rate'][2], "前天": data['stats'][6]['retention_rate'][2], '八天前': data['stats'][0]['retention_rate'][2]}


def query_sevendays_retentions():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-01&end_date=2019-09-15&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=retentions
    stats_type = 'retentions'
    report_type = 'reports'
    end_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=14)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][6]['retention_rate'][6], "前天": data['stats'][5]['retention_rate'][6], '八天前': data['stats'][0]['retention_rate'][6]}


def query_video_supplement():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b7289ddf43e4838c7000268
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_ad_interstitial_from
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                               'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type, 'event_group_id': event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['count'], "前天": data['stats'][1]['count'], '八天前': data['stats'][-1]['count']}


def query_video():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b7289a4f43e487686000096
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_watch_video
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                               'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type, 'event_group_id': event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": [data['stats'][0]['count'], data['stats'][0]['device']], "前天": [data['stats'][1]['count'], data['stats'][1]['device']], '八天前': [data['stats'][-1]['count'], data['stats'][-1]['device']]}
# https://mobile.umeng.com/apps/eb00006c4684e34ff9d8d3b5/events/load_table_data?start_date=2019-09-19&end_date=2019-09-25&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b3de4bca40fa35729000065
# https://mobile.umeng.com/apps/eb00006c4684e34ff9d8d3b5/events/load_table_data?start_date=2019-09-17&end_date=2019-09-24&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b7289a4f43e487686000096


def query_iap_users():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b84cc7ca40fa34b91000015
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_buy_iap_total
    
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                               'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type, 'event_group_id': event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}


def query_open_map2_users():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?&start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b84cc7ca40fa34b91000019
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_open_map2
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                               'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type, 'event_group_id': event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}


def query_open_map3_users():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-09&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b9a2569b27b0a5cb8000054
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_open_map3
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                               'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type, 'event_group_id': event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}


def query_open_event():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b7289ddf43e4838c7000282
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_open_event
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                               'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type, 'event_group_id': event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}


def query_claim_times():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-09&end_date=2019-09-15&channels[]=&versions[]=&event_id=5b7be0660237f6071568cc54&event_group_id=5b7289ddf43e4838c7000289&event_group_name=show_claim&stats=count_distribute&property_type=string
    try:
        stats_type = 'count_distribute'
        report_type = 'events'
        event_id = event_id_show_claim
        event_group_id = event_group_id_show_claim
        event_group_name = 'show_claim'
        days = [1, 2, 8]
        response = []
        i = 0
        for day in days:
            end_date = (today - timedelta(days=day)).strftime('%Y-%m-%d')
            start_date = end_date
            url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&event_id=%(event_id)s&event_group_id=%(event_group_id)s&event_group_name=%(event_group_name)s&stats=%(stats_type)s&property_type=string'

            url = url_eventname_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                                           'start_date': start_date, 'end_date': end_date, 'event_id': event_id,
                                           'event_group_id': event_group_id, 'event_group_name': event_group_name, 'stats_type': stats_type}
            resp = requests.get(url=url, cookies=cookies)
            data = resp.json()
            response.append(data['stats'][1]['num'])
            i += 1
        return {"昨天": response[0], "前天": response[1], '八天前': response[2]}
    except:
        print("ERROR: query_claim_times")


def query_unlock_business():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-14&end_date=2019-09-14&channels[]=&versions[]=&event_id=5b7bdfa20237f6071568cc50&event_group_id=5b7289ddf43e4838c7000295&event_group_name=unlock_business&stats=count_distribute&property_type=string
    try:
        stats_type = 'count_distribute'
        report_type = 'events'
        event_id = event_id_unlock_business
        event_group_id = event_group_id_unlock_business
        event_group_name = 'unlock_business'
        days = [1, 2, 8]
        response = []
        i = 0
        for day in days:
            end_date = (today - timedelta(days=day)).strftime('%Y-%m-%d')
            start_date = end_date
            url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&event_id=%(event_id)s&event_group_id=%(event_group_id)s&event_group_name=%(event_group_name)s&stats=%(stats_type)s&property_type=string'

            url = url_eventname_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                                           'start_date': start_date, 'end_date': end_date, 'event_id': event_id,
                                           'event_group_id': event_group_id, 'event_group_name': event_group_name, 'stats_type': stats_type}
            resp = requests.get(url=url, cookies=cookies)
            data = resp.json()
            response.append(
                [data['stats'][3]['num'], data['stats'][-1]['num']])
            i += 1
        return {"昨天": response[0], "前天": response[1], '八天前': response[2]}
    except:
        print("ERROR: query_unlock_business")


def query_iap_money():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-14&end_date=2019-09-14&channels[]=&versions[]=&event_id=5b9f7401c37c58067735ebc0&event_group_id=5b84cc7ca40fa34b91000015&event_group_name=buy_iap_total&stats=count_distribute&property_type=string
    stats_type = 'count_distribute'
    report_type = 'events'
    event_id = event_id_buy_iap_total
    event_group_id = event_group_id_buy_iap_total
    event_group_name = 'buy_iap_total'
    group = []
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = end_date
    url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&event_id=%(event_id)s&event_group_id=%(event_group_id)s&event_group_name=%(event_group_name)s&stats=%(stats_type)s&property_type=string'

    url = url_eventname_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                                   'start_date': start_date, 'end_date': end_date, 'event_id': event_id,
                                   'event_group_id': event_group_id, 'event_group_name': event_group_name, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    for d in data['stats']:
        group.append({'label': d['label'], 'num': d['num']})

    return group


def query_ad_play_num(event_id, event_group_id):
    """查询播放广告次数"""
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-16&end_date=2019-09-22&channels[]=&versions[]=&event_id=5b7a8b163665ca0789e82188&event_group_id=5b7289a4f43e487686000096&event_group_name=watch_video&stats=count_distribute&property_type=string

    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-16&end_date=2019-09-22&channels[]=&versions[]=&event_id=5b74f0b25a16bc074d5f2633&event_group_id=5b7289a4f43e487686000096&event_group_name=watch_video&stats=count_distribute&property_type=string

    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-16&end_date=2019-09-22&channels[]=&versions[]=&event_id=5b9f0bd60237f606c0aca277&event_group_id=5b7289a4f43e487686000096&event_group_name=watch_video&stats=count_distribute&property_type=string

    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-16&end_date=2019-09-22&channels[]=&versions[]=&event_id=5ba22b756e21cc6462bdafd3&event_group_id=5b7289a4f43e487686000096&event_group_name=watch_video&stats=count_distribute&property_type=string
    stats_type = 'count_distribute'
    report_type = 'events'
    event_group_name = 'watch_video'
    event_group_id = event_group_id_watch_video
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = end_date
    url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&event_id=%(event_id)s&event_group_id=%(event_group_id)s&event_group_name=%(event_group_name)s&stats=%(stats_type)s&property_type=string'

    url = url_eventname_temlate % {"base_url": base_url, "id": g_product_id, 'report_type': report_type,
                                   'start_date': start_date, 'end_date': end_date, 'event_id': event_id,
                                   'event_group_id': event_group_id, 'event_group_name': event_group_name, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    dict = {}
    for item in data['stats']:
        dict[item['label']] = item['num']

    return dict


def query_ad_play_num_all():
    total = {}
    ids = [event_id_ad_play_action,
           event_id_ad_play_event,
           event_id_ad_play_map2,
           event_id_ad_play_map3]
    for id in ids:
        data = query_ad_play_num(id, event_group_id_watch_video)
        for key in data.keys():
            if key in total:
                total[key] += data[key]
            else:
                total[key] = data[key]

    return total


def calculate_iap_nums():
    '''IAP购买次数'''
    i = 0
    j = 0
    data = query_iap_money()
    for i in range(len(data)):
        j += data[i]['num']
    return j


def calculate_iap_money_sum():
    '''付费金额'''
    i = 0
    j = 0
    data = query_iap_money()
    for i in range(len(data)):
        if data[i]['label'] in product_id_iOS_unit_price:
            j += data[i]['num'] * product_id_iOS_unit_price[data[i]['label']]
        elif data[i]['label'] in product_id_andriod_unit_price:
            j += data[i]['num'] * \
                product_id_andriod_unit_price[data[i]['label']]
    return j


def query_xi_back_gun():
    """
    https://xi.harrybuy.com/es/monesimplify/pistolevent
    从xi平台查询, 回本手枪图
    """
    url = "https://xi.harrybuy.com/es/monesimplify/pistolevent"
    end_date = (today - timedelta(days=3)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=11)).strftime('%Y-%m-%d')
    qdata_temlate = '{"app_name":"%(app_name)s","date_range":["%(start_date)s","%(end_date)s"],"dimension":[],"time_span":"auto","limit":20,"subs_type":"real","filter":{"bundle_id":["%(bundle_id)s"],"platform":["%(platform)s"],"media_source":["Facebook Ads"],"country_code":["US"]}}'

    # qdata = b'{"app_name":"Game_iOS_Idle Capitalist","date_range":["2019-09-15","2019-09-19"],"dimension":[],"time_span":"auto","limit":20,"subs_type":"real","filter":{"bundle_id":["com.idlecapatalist.aovalw"],               "platform":["ios"],    "media_source":["Facebook Ads"],"country_code":["US"]}}'
    # qdata = b'{"app_name":"Game_android_TBC3",       "date_range":["2019-10-13","2019-10-25"],"dimension":[],"time_span":"auto","limit":20,"subs_type":"real","filter":{"bundle_id":["com.brokenreality.bigcapitalist3.android"],"platform":["android"],"media_source":["Facebook Ads"],"country_code":["US"]}}'
    qdata_str = qdata_temlate % {"app_name": g_app_name, "start_date": start_date,
                                 'end_date': end_date, 'bundle_id': g_bundle_id, 'platform': g_platform}
    qdata = qdata_str.encode("utf-8")
    headers = {
        "authority": "xi.harrybuy.com",
        "method": "POST",
        "Host": "xi.harrybuy.com",
        "Connection": "keep-alive",
        "accept": "application/json, text/plain, */*",
        "origin": "https://xi.harrybuy.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "content-type": "application/json",
        # "Accept": "*/*",
        "referer": "https://xi.harrybuy.com/v3/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "content-type": "application/json;charset=UTF-8",
        "cookie": f"Xi-Token=fangfang_ren; connect.sid= {query_xi_back_gun_connect_sid}",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-token": "fangfang_ren",
        "Referrer Policy": "no-referrer-when-downgrade"
    }

    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()

    try:
        dict = {}
        for item in data[0]:
            if item["date"] == end_date and item["lifetime"] == 24:
                dict["people_num_watch_video"] = item["users"]
                for event in item["event"]:
                    if event["event_name"] == "video_imp":
                        dict["num_video_played"] = event["cnt"]
        return dict
    except:
        print("ERROR: query_xi_back_gun")


def query_xi_ecpm(country=""):
    """从xi平台 收入查询 ecpm"""
    url = "https://xi.harrybuy.com/report/revenue"
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    # {"appName":["Game_iOS_Idle Capitalist"],"dateRange":["2019-09-16","2019-09-23"],"timeZone":"default","platform":[],"country":["US"],"breakdown":["app_name","date"]}}
    qdata_temlate_ecpm = '{"appName":["%(app_name)s"],"dateRange":["%(start_date)s","%(end_date)s"],"timeZone":"default","platform":[],"country":[%(country)s],"breakdown":["app_name","date"]}'
    qdata_ecpm_str = qdata_temlate_ecpm % {
        "app_name": g_app_name, "start_date": start_date, 'end_date': end_date, "country": country}
    qdata_ecpm = qdata_ecpm_str.encode("utf-8")
    headers = {
        "authority": "xi.harrybuy.com",
        "method": "POST",
        "path": "/report/revenue",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "Host": "xi.harrybuy.com",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"connect.sid={query_xi_ecpm_connect_sid}; Xi-Token=fangfang_ren",
        "Origin": "https://xi.harrybuy.com",
        "referer": "https://xi.harrybuy.com/v3/",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-token": "fangfang_ren"
    }

    resp = requests.post(url=url, data=qdata_ecpm, headers=headers)

    data = resp.json()

    return {"昨天": data[-1]['ecpm'], "前天": data[-2]['ecpm'], '八天前': data[1]['ecpm']}


# stat_platform_android()
# # print(query_xi_back_gun(app_name_tbc3_android, bundle_id_tbc3_android, platform_tbc3_android))
# print(query_xi_ecpm())
# print(query_xi_ecpm(country_us))

stat_platform_android()
print(query_xi_back_gun())
