# -*- coding: utf-8 -*-

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
import inspect

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
related_Id = ""
xiAppId = ""


url_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=%(stats_type)s'
url_event_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&stats=%(stats_type)s&event_group_id=%(event_group_id)s'
url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&%(event_id)s&%(event_group_id)s&%(event_group_name)s&stats=%(stats_type)s&property_type=string'

interval = 8

# Cookies不对时, 拷贝以下链接对应的cookies
# https://mobile.umeng.com/ht/api/v3/app/user/active/detail?relatedId=5b3d8d9ff43e4864c60000be
# detail?relatedId=5b3d8d9ff43e4864c60000be
cookies_str = 'um_lang=zh; UM_distinctid=16d0b6d430b151-07b72381dd6cf2-38607701-13c680-16d0b6d430c99; cna=qYvtFeWEAk8CAduMKb9Naxpx; umplus_uc_loginid=fangfang_ren; uc_session_id=60028085-4ed5-4567-97e5-ecf7bcccb1e1; XSRF-TOKEN=d043bdcb-f207-4c0d-b568-fc782f24f4ac; cn_1258498910_dplus=1%5B%7B%7D%2C0%2C1582300385%2C0%2C1582300385%2C%22%24direct%22%2C%2216d0b6d430b151-07b72381dd6cf2-38607701-13c680-16d0b6d430c99%22%2C%221567853500%22%2C%22https%3A%2F%2Fmobile.umeng.com%2Fhome%2Fcheck_login%3Furl%3Dhttps%253A%252F%252Fpassport.umeng.com%252Flogin%253FappId%253Dumeng%22%2C%22mobile.umeng.com%22%5D; umplus_uc_token=1wy8BetUNX7V10gkMzTS4IQ_f8bd4634914c4137a197542c7e8e6f4d; isg=BIWF8z2id0sPR1ArZyJGFWZ-lMe_QjnUBai_64fqWbzLHqWQT5djpJo3LELoLVGM; XSRF-TOKEN-HAITANG=2d07c9af-a157-4207-b3e9-f06431e9c913; ummo_ss=BAh7CEkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjoGRVRbCEkiCVVzZXIGOwBGWwZvOhNCU09OOjpPYmplY3RJZAY6CkBkYXRhWxFpYmkxaVppAZppXGkSaQHzaQGTaT5pAGkKaXRJIhk4UVA3eElpcW1PaGRXdG1HUFpQawY7AFRJIhR1bXBsdXNfdWNfdG9rZW4GOwBGIj0xd3k4QmV0VU5YN1YxMGdrTXpUUzRJUV9mOGJkNDYzNDkxNGM0MTM3YTE5NzU0MmM3ZThlNmY0ZEkiD3Nlc3Npb25faWQGOwBUSSIlZjU0M2M0MjdmZDA5NjI4YTliNDUzNjVmZmUzNWVkMzIGOwBG--5170287049c6c9b47d11942fcb82526d7ff2a04e; CNZZDATA1259864772=245797500-1567853794-https%253A%252F%252Fpassport.umeng.com%252F%7C1582374749; cn_1259864772_dplus=1%5B%7B%22%E6%98%AF%E5%90%A6%E7%99%BB%E5%BD%95%22%3Atrue%2C%22UserID%22%3A%22fangfang_ren%22%2C%22Uapp_appkey%22%3A%225b3d8d9ff43e4864c60000be%22%2C%22Uapp_platform%22%3A%22android%22%7D%2C0%2C1582376122%2C0%2C1582376122%2C%22%24direct%22%2C%2216d0b6d430b151-07b72381dd6cf2-38607701-13c680-16d0b6d430c99%22%2C%221567853794%22%2C%22https%3A%2F%2Fpassport.umeng.com%2Freg-redirect.html%3FredirectUrl%3Dhttps%253A%252F%252Fmobile.umeng.com%252Fapps%22%2C%22passport.umeng.com%22%5D; cn_1273967994_dplus=1%5B%7B%7D%2Cnull%2Cnull%2Cnull%2Cnull%2C%22%24direct%22%2C%2216d0b6d430b151-07b72381dd6cf2-38607701-13c680-16d0b6d430c99%22%2C%221567853794%22%2C%22https%3A%2F%2Fmobile.umeng.com%2Fapps%22%2C%22mobile.umeng.com%22%5D'

# x-xsrf-token可能也需要更新
g_x_xsrf_token= "d043bdcb-f207-4c0d-b568-fc782f24f4ac"

query_xi_back_gun_connect_sid = unquote('s%3AACH4Z4vE7zmqg57ahLk67l4Rt25unSZi.zZBqjvgvie%2FbURJ%2BHgIQpdvup2ycuOfrkZ8xRjfG4aU')

query_xi_ecpm_connect_sid = unquote('s%3ACGTnbTJdCAzpAWTu3Q2CDZX958umZLda.AxF5yblaNnJdLve7iePH9wbnNqwsnlACot7lfTvwnls')


def stat_platform_ios():
    global g_product_id
    global g_app_name
    global g_bundle_id
    global g_platform
    global xiAppId

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
    global related_Id

    
    related_Id = "5b7139be8f4a9d7dea000051"
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
    event_id_unlock_business = '5b7bdfa20237f6071568cc50'
    event_id_ad_play_action = '5b7a8b163665ca0789e82188'
    event_id_ad_play_event = '5b74f0b25a16bc074d5f2633'
    event_id_ad_play_map2 = '5b9f0bd60237f606c0aca277'
    event_id_ad_play_map3 = '5ba22b756e21cc6462bdafd3'

    g_product_id = id_tbc_ios
    g_app_name = app_name_tbc3_ios
    g_bundle_id = bundle_id_tbc3_ios
    g_platform = platform_tbc3_ios
    xiAppId = xiAppId_ios


def stat_platform_android():
    global g_product_id
    global g_app_name
    global g_bundle_id
    global g_platform
    global xiAppId

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
    global related_Id

    related_Id = "5b3d8d9ff43e4864c60000be"
    event_group_id_ad_interstitial_from = '5b3de4bca40fa3572900007d'  # ok
    event_group_id_watch_video = '5b3de4bca40fa35729000065'  # ok
    event_group_id_buy_iap_total = '5b7e21c5f43e48055e000042'  # ok
    event_group_id_open_map2 = '5b7e2198b27b0a7a4200001b'  # ok
    event_group_id_open_map3 = '5b9a23a1f29d983795000100'  # ok
    event_group_id_open_event = '5b642551f29d98672d000163'  # ok
    event_group_id_show_claim = '5b3eee9cf29d9833db0001db'  # ok
    event_group_id_unlock_business = '5b3de4bca40fa35729000078'  # ok

    event_id_buy_iap_total = '5b7e764f3665cafb7b5fe340'  # ok
    event_id_show_claim = '5b44647cdd26ca4c8f4db5ad'  # ok
    event_id_unlock_business = '5b44645e5a16bc136ebd03a1'  # ok
    event_id_ad_play_action = '5b446ca85a16bc136ebd03a8'  # ok
    event_id_ad_play_event = '5b63c9ce3665ca073aad10ff'  # ok
    event_id_ad_play_map2 = '5b7e51d20abec661afcec361'  # ok
    event_id_ad_play_map3 = '5b9f5e589242950645e25132'  # ok

    g_product_id = id_tbc_android
    g_app_name = app_name_tbc3_android
    g_bundle_id = bundle_id_tbc3_android
    g_platform = platform_tbc3_android
    xiAppId = xiAppId_android

def get_start_time():
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    return start_date

def get_start_time():
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')

def query_new_users():
    """从umeng平台"""
    print(inspect.stack()[0][3])
    url = f"https://mobile.umeng.com/ht/api/v3/app/user/new/detail?relatedId={related_Id}"
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    # {"page":1,"pageSize":30,"fromDate":"2019-11-17","toDate":"2019-11-24","version":[],"channel":[],"timeUnit":"day","view":"newUser","relatedId":"5b7139be8f4a9d7dea000051"}
    qdata_temlate = '{"page":1,"pageSize":30,"fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","view":"%(view)s","relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'view': 'newUser', 'related_Id': related_Id}
    qdata = qdata_str.encode("utf-8")
    query_type = "installation"
    user_status_type = 'new'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/user/{user_status_type}/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/reports/{query_type}",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }

    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['newUser']}


def query_active_users():
    """从umeng平台"""
    print(inspect.stack()[0][3])
    url = f"https://mobile.umeng.com/ht/api/v3/app/user/active/detail?relatedId={related_Id}"
    #       https://mobile.umeng.com/ht/api/v3/app/user/active/detail?relatedId=5b3d8d9ff43e4864c60000be
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    qdata_temlate = '{"page":1,"pageSize":30,"fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","view":"activeUserDay","relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id}
    qdata = qdata_str.encode("utf-8")
    query_type = "active_user"
    user_status_type = 'active'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/user/{user_status_type}/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/reports/{query_type}",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }

    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['activeUser']}


def query_new_active_users():
    print(inspect.stack()[0][3])
    new_user = query_new_users()
    active_user = query_active_users()
    return {"昨天": [active_user['昨天'], new_user['昨天']]}


def query_launches_times():
    """启动次数"""
    print(inspect.stack()[0][3])
    url = f"https://mobile.umeng.com/ht/api/v3/app/user/launch/detail?relatedId={related_Id}"
    # {"page":1,"pageSize":30,"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-18","toDate":"2019-11-25","version":[],"channel":[],"timeUnit":"day","view":"launch"}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    qdata_temlate = '{"page":1,"pageSize":30,"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","view":"launch"}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id}
    qdata = qdata_str.encode("utf-8")
    query_type = "launch"
    user_status_type = 'launch'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/user/{user_status_type}/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/reports/{query_type}",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['launch']}


def query_morrow_retentions():
    print(inspect.stack()[0][3])
    """用户次日留存"""
    url = f'https://mobile.umeng.com/ht/api/v3/app/retention/view?relatedId={related_Id}'
    # {"fromDate":"2019-11-17","toDate":"2019-11-24","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"5b3d8d9ff43e4864c60000be"}
    end_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    qdata_temlate = '{"fromDate":"%(from_date)s","toDate":"%(to_date)s","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id}
    qdata = qdata_str.encode("utf-8")
    query_type = "retention"
    user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/user/{user_status_type}/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/reports/{query_type}",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['rateItems'][0]['retention'][0]}


def query_threedays_retentions():
    """用户三日留存"""
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/retention/view?relatedId={related_Id}'
    # {"fromDate":"2019-11-17","toDate":"2019-11-24","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"5b3d8d9ff43e4864c60000be"}
    end_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=9)).strftime('%Y-%m-%d')
    qdata_temlate = '{"fromDate":"%(from_date)s","toDate":"%(to_date)s","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id}
    qdata = qdata_str.encode("utf-8")
    query_type = "retention"
    user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/user/{user_status_type}/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/reports/{query_type}",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    # Todo: 消除数字-3可能带来的风险
    return {"昨天": data['data']['rateItems'][-3]['retention'][2]}


def query_sevendays_retentions():
    """用户七日留存"""
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/retention/view?relatedId={related_Id}'
    # {"fromDate":"2019-11-17","toDate":"2019-11-24","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"5b3d8d9ff43e4864c60000be"}
    end_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    qdata_temlate = '{"fromDate":"%(from_date)s","toDate":"%(to_date)s","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id}
    qdata = qdata_str.encode("utf-8")
    query_type = "retention"
    user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/user/{user_status_type}/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/reports/{query_type}",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    # Todo: 消除魔鬼数字可能带来的风险
    return {"昨天": data['data']['rateItems'][0]['retention'][-1]}


def query_video_supplement():
    '''查插屏數量'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-20","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"ad_interstitial_from","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "ad_interstitial_from"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","channel":[],"version":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    # query_type = "retention"
    # user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"ht/api/v3/app/event/analysis/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_ad_interstitial_from}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventLaunch']}


def query_video():
    '''查視頻數量及獨立人數'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-20","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"watch_video","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "watch_video"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    # query_type = "retention"
    # user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"ht/api/v3/app/event/analysis/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_watch_video}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": [data['data']['items'][1]['eventLaunch'], data['data']['items'][1]['eventDevice']]}


def query_iap_users():
    '''查詢内購iap人數'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-20","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"buy_iap_total","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "buy_iap_total"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    # query_type = "retention"
    # user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"ht/api/v3/app/event/analysis/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_buy_iap_total}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_open_map2_users():
    '''查詢進入map2獨立用戶數'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-21","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"open_map2","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "open_map2"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    # query_type = "retention"
    # user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"ht/api/v3/app/event/analysis/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_open_map2}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_open_map3_users():
    '''查詢進入map3獨立用戶數'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-21","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"open_map3","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "open_map3"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    # query_type = "retention"
    # user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"ht/api/v3/app/event/analysis/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_open_map3}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_open_event():
    '''查詢進入event獨立用戶數'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-21","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"open_event","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "open_event"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    # query_type = "retention"
    # user_status_type = 'retention'
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"ht/api/v3/app/event/analysis/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_open_event}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_claim_times():
    '''查詢成功claim次數'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-26","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"show_claim","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    eventName = "show_claim"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}'
    qdata_str = qdata_temlate % {
        "from_date": end_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_show_claim}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['value']}


def query_unlock_business():
    '''查詢產業解鎖人數'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-26","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"unlock_business","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    eventName = "unlock_business"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}'
    qdata_str = qdata_temlate % {
        "from_date": end_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_unlock_business}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": [data['data']['items'][3]['value'], data['data']['items'][-1]['value']]}


def query_iap_money():
    '''查詢iap產品與數量'''
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-27","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"buy_iap_total","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    eventName = "buy_iap_total"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(end_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}'
    qdata_str = qdata_temlate % {
        "end_date": end_date, "to_date": end_date, 'related_Id': related_Id, 'eventName': eventName}
    qdata = qdata_str.encode("utf-8")
    group = []
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_buy_iap_total}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    # return {"business_5": data['data']['items']}
    for d in data['data']['items']:
        group.append({'name': d['name'], 'value': d['value']})
    return group


def query_ad_play_num(property_value):
    """查询廣告場景視頻播放次数"""
    print(inspect.stack()[0][3])
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-27","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"buy_iap_total","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-30","toDate":"2019-11-30","version":[],"channel":[],"timeUnit":"day","eventName":"watch_video","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    eventName = "watch_video"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(end_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","propertyName":"%(property_value)s","view":"propertyStringLaunchView","type":"propertyValue"}'
    qdata_str = qdata_temlate % {"end_date": end_date, "to_date": end_date,
                                 'related_Id': related_Id, 'eventName': eventName, 'property_value': property_value}
    qdata = qdata_str.encode("utf-8")
    group = []
    headers = {
        "authority": "mobile.umeng.com",
        "method": "POST",
        "path": f"/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": f"{cookies_str.encode('utf-8')}",
        "origin": "https://mobile.umeng.com",
        "referer": f"https://mobile.umeng.com/platform/{related_Id}/function/events/detail/{event_group_id_watch_video}/string",
        "pragma": "no-cache",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}"
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()

    dict = {}
    for item in data['data']['items']:
        dict[item['name']] = item['value']

    return dict


def query_ad_play_num_all():
    print(inspect.stack()[0][3])
    total = {}
    names = [event_name_ad_play_action,
             event_name_ad_play_event,
             event_name_ad_play_map2,
             event_name_ad_play_map3]
    for name in names:
        data = query_ad_play_num(name)
        for key in data.keys():
            if key in total:
                total[key] += data[key]
            else:
                total[key] = data[key]

    return total


def calculate_iap_nums():
    '''IAP购买次数'''
    print(inspect.stack()[0][3])
    i = 0
    j = 0
    data = query_iap_money()
    for i in range(len(data)):
        j += data[i]['value']
    return j


def calculate_iap_money_sum():
    '''iap内購金额'''
    print(inspect.stack()[0][3])
    i = 0
    j = 0
    data = query_iap_money()
    for i in range(len(data)):
        if data[i]['name'] in product_id_iOS_unit_price:
            j += data[i]['value'] * product_id_iOS_unit_price[data[i]['name']]
        elif data[i]['name'] in product_id_andriod_unit_price:
            j += data[i]['value'] * \
                product_id_andriod_unit_price[data[i]['name']]
    return j


def query_xi_back_gun():
    print(inspect.stack()[0][3])
    """从xi平台查询, 回本手枪图"""
    url = "https://api-xi.harrybuy.com/es/monesimplify/pistolevent"
    end_date = (today - timedelta(days=3)).strftime('%Y-%m-%d 23:59:59')
    end_date_resp = (today - timedelta(days=3)).strftime('%Y%m%d00')
    start_date = (today - timedelta(days=3)).strftime('%Y-%m-%d 00:00:00')
    init_time_span = 24
    # {"app_name":"Game_android_TBC3","date_range":["2019-12-04","2019-12-04"],"dimension":[],"time_span":"auto","limit":20,"subs_type":"real","filter":{"bundle_id":["com.brokenreality.bigcapitalist3.android"],"platform":["android"],"media_source":["Facebook Ads"],"country_code":["US"]}}
    # {"app_name":"Game_android_TBC3","date_range":["2020-02-19 00:00:00","2020-02-19 23:59:59"],"dimension":[],"time_span":"auto","limit":20,"subs_type":"real","init_time_span":24,"filter":{"bundle_id":["com.brokenreality.bigcapitalist3.android"],"platform":["android"],"media_source":["Facebook Ads"],"country_code":["US"]}}
    qdata_temlate = '{"app_name":"%(app_name)s","date_range":["%(start_date)s","%(end_date)s"],"dimension":[],"time_span":"auto","limit":20,"subs_type":"real","init_time_span":%(init_time_span)d,"filter":{"bundle_id":["%(bundle_id)s"],"platform":["%(platform)s"],"media_source":["Facebook Ads"],"country_code":["US"]}}'
    qdata_str = qdata_temlate % {"app_name": g_app_name, "start_date": start_date,
                                 'end_date': end_date, "init_time_span":init_time_span,'bundle_id': g_bundle_id, 'platform': g_platform}
    qdata = qdata_str.encode("utf-8")
    headers = {
        "authority": "api-xi.harrybuy.com",
        "method": "POST",
        # "Host": "xi.harrybuy.com",
        # "Connection": "keep-alive",
        "accept": "application/json, text/plain, */*",
        "origin": "https://xi.harrybuy.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "x-xsrf-token": f"{g_x_xsrf_token}",
        "referer": "https://xi.harrybuy.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "content-type": "application/json;charset=UTF-8",
        "cookie": f"connect.sid= {query_xi_back_gun_connect_sid}",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-token": "fangfang_ren",
        # "Referrer Policy": "no-referrer-when-downgrade"
    }

    try:
        resp = requests.post(url=url, data=qdata, headers=headers)
        data = resp.json()

        dict = {}
        for item in data[0]:
            if item["date"] == end_date_resp and item["lifetime"] == 24:
                dict["people_num_watch_video"] = item["users"]
                for event in item["event"]:
                    if event["event_name"] == "video_imp":
                        dict["num_video_played"] = event["cnt"]
        return dict
    except:
        print("ERROR: query_xi_back_gun")


def query_xi_ecpm(country=""):
    print(inspect.stack()[0][3])
    """从xi平台 收入查询 ecpm"""
    url = "https://api-xi.harrybuy.com/report/revenuedatav4"
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    # {"xiAppId":"Android_com.brokenreality.bigcapitalist3.android","dateRange":["2019-11-29","2019-12-06"],"vendor":[],"country":[],"breakdown":["xi_application_id","date"]
    # {"xiAppId":"Android_com.brokenreality.bigcapitalist3.android","dateRange":["2019-11-29","2019-12-06"],"vendor":[],"country":["US"],"breakdown":["xi_application_id","date"]}
    qdata_temlate_ecpm = '{"xiAppId":"%(xiAppId)s","dateRange":["%(start_date)s","%(end_date)s"],"vendor":[],"country":[%(country)s],"breakdown":["xi_application_id","date"]}'
    qdata_ecpm_str = qdata_temlate_ecpm % {'xiAppId': xiAppId, "start_date": start_date, 'end_date': end_date, "country": country}
    qdata_ecpm = qdata_ecpm_str.encode("utf-8")
    headers = {
        "authority": "api-xi.harrybuy.com",
        "method": "POST",
        # "Host": "xi.harrybuy.com",
        # "Connection": "keep-alive",
        "accept": "application/json, text/plain, */*",
        "origin": "https://xi.harrybuy.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "referer": "https://xi.harrybuy.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5",
        "content-type": "application/json;charset=UTF-8",
        "cookie": f"connect.sid= {query_xi_ecpm_connect_sid}",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-token": "fangfang_ren",
        # "Referrer Policy": "no-referrer-when-downgrade"
    }
    try:
        resp = requests.post(url=url, data=qdata_ecpm, headers=headers)
        data = resp.json()

        return {"昨天": float(data[-1]['ecpm']), "前天": float(data[-2]['ecpm'])}
    except:
        print("ERROR: query_xi_back_gun")


# stat_platform_android()
# # print(query_xi_back_gun(app_name_tbc3_android, bundle_id_tbc3_android, platform_tbc3_android))
# print(query_xi_ecpm())
# print(query_xi_ecpm(country_us))

# stat_platform_android()
# print(query_active_users())

def test():
    # stat_platform_ios()
    stat_platform_android()
    print(query_xi_back_gun())
    # print(query_active_users())

# test()