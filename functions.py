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

url_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=%(stats_type)s'
url_event_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&stats=%(stats_type)s&event_group_id=%(event_group_id)s'
url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&%(event_id)s&%(event_group_id)s&%(event_group_name)s&stats=%(stats_type)s&property_type=string'

interval = 8
related_Id = "5b3d8d9ff43e4864c60000be"

cookies_str = 'umplus_uc_loginid=fangfang_ren; UM_distinctid=16d10cf0765141-056e45dadb0c15-5373e62-240000-16d10cf0766e88; um_lang=zh; cn_1276392090_dplus=1%5B%7B%7D%2C0%2C1567949770%2C0%2C1567949770%2Cnull%2C%2216d10cf0765141-056e45dadb0c15-5373e62-240000-16d10cf0766e88%22%2C%221567940381%22%2C%22https%3A%2F%2Fpassport.umeng.com%2Freg-redirect.html%3FredirectUrl%3Dhttps%253A%252F%252Fweb.umeng.com%252Fmain.php%253Fc%253Dsite%2526a%253Dshow%2526from%253Dlogin%22%2C%22passport.umeng.com%22%5D; cna=6axpFZjaSlYCATuvJCB7x6Bc; frame=; CNZZDATA1259864772=1505950409-1567941798-%7C1574772244; uc_session_id=52585a1b-32f8-463f-90fd-8c55e39a84b1; cn_1258498910_dplus=1%5B%7B%7D%2C0%2C1574777601%2C0%2C1574777601%2C%22%24direct%22%2C%2216d10cf0765141-056e45dadb0c15-5373e62-240000-16d10cf0766e88%22%2C%221569051311%22%2C%22https%3A%2F%2Fmobile.umeng.com%2Fhome%2Fcheck_login%3Furl%3Dhttps%253A%252F%252Fpassport.umeng.com%252Flogin%253FappId%253Dumeng%22%2C%22mobile.umeng.com%22%5D; umplus_uc_token=1L2mCUHZal1wrd1d6SfpyLg_b9c85717ee5a46b587acb02ba84ed045; isg=BGJi2sjVS2B7JleVMyxTB1NMs-gEG2ahvX2Gnqz7g1WAfwL5lEZ23LZ2q_Mm795l; ummo_ss=BAh7CEkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjoGRVRbCEkiCVVzZXIGOwBGWwZvOhNCU09OOjpPYmplY3RJZAY6CkBkYXRhWxFpYmkxaVppAZppXGkSaQHzaQGTaT5pAGkKaXRJIhk4UVA3eElpcW1PaGRXdG1HUFpQawY7AFRJIhR1bXBsdXNfdWNfdG9rZW4GOwBGIj0xTDJtQ1VIWmFsMXdyZDFkNlNmcHlMZ19iOWM4NTcxN2VlNWE0NmI1ODdhY2IwMmJhODRlZDA0NUkiD3Nlc3Npb25faWQGOwBUSSIlNTc3MWM4M2FkMWM3NThkOGEzMTZlMGRmNjJiZTYzMTEGOwBG--7485405d89e438c288b3fd4a8b73a88a4270e262; cn_1259864772_dplus=1%5B%7B%22%E6%98%AF%E5%90%A6%E7%99%BB%E5%BD%95%22%3Atrue%2C%22UserID%22%3A%22fangfang_ren%22%2C%22Uapp_appkey%22%3A%225b3d8d9ff43e4864c60000be%22%2C%22Uapp_platform%22%3A%22android%22%7D%2C0%2C1574777590%2C0%2C1574777590%2C%22%24direct%22%2C%2216d10cf0765141-056e45dadb0c15-5373e62-240000-16d10cf0766e88%22%2C%221567941798%22%2C%22%24direct%22%2C%22%24direct%22%5D; cn_1273967994_dplus=1%5B%7B%7D%2Cnull%2Cnull%2Cnull%2Cnull%2C%22%24direct%22%2C%2216d10cf0765141-056e45dadb0c15-5373e62-240000-16d10cf0766e88%22%2C%221567945446%22%2C%22https%3A%2F%2Fmobile.umeng.com%2Fplatform%2Fapps%2Flist%22%2C%22mobile.umeng.com%22%5D'

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
    event_id_unlock_business = '5b7bdfa20237f6071568cc50'
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


def query_new_users():
    """从umeng平台"""
    print(inspect.stack()[0][3])
    related_Id = "5b7139be8f4a9d7dea000051"
    url = f"https://mobile.umeng.com/ht/api/v3/app/user/active/detail?relatedId={related_Id}"
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    # {"page":1,"pageSize":30,"fromDate":"2019-11-17","toDate":"2019-11-24","version":[],"channel":[],"timeUnit":"day","view":"newUser","relatedId":"5b7139be8f4a9d7dea000051"}
    qdata_temlate = '{"page":1,"pageSize":30,"fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","view":"%(view)s","relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {
        "from_date": start_date, "to_date": end_date, 'view':'newUser', 'related_Id': related_Id}
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
    }

    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['newUser']}


def query_active_users():
    """从umeng平台"""
    print(inspect.stack()[0][3])
    related_Id = "5b7139be8f4a9d7dea000051"
    url = f"https://mobile.umeng.com/ht/api/v3/app/user/active/detail?relatedId={related_Id}"
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    # {"page":1,"pageSize":30,"fromDate":"2019-11-17","toDate":"2019-11-24","version":[],"channel":[],"timeUnit":"day","view":"activeUserDay","relatedId":"5b7139be8f4a9d7dea000051"}
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
    }

    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['activeUser']}


def query_launches_times():
    """启动次数"""
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f"https://mobile.umeng.com/ht/api/v3/app/user/launch/detail?relatedId={related_Id}"
    # {"page":1,"pageSize":30,"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-18","toDate":"2019-11-25","version":[],"channel":[],"timeUnit":"day","view":"launch"}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    qdata_temlate = '{"page":1,"pageSize":30,"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","view":"launch"}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['launch']}


def query_morrow_retentions():
    print(inspect.stack()[0][3])
    """用户次日留存"""
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/retention/view?relatedId={related_Id}'
    # {"fromDate":"2019-11-17","toDate":"2019-11-24","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"5b3d8d9ff43e4864c60000be"}
    end_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=9)).strftime('%Y-%m-%d')
    qdata_temlate = '{"fromDate":"%(from_date)s","toDate":"%(to_date)s","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['rateItems'][6]['retention'][0]}


def query_threedays_retentions():
    """用户三日留存"""
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/retention/view?relatedId={related_Id}'
    # {"fromDate":"2019-11-17","toDate":"2019-11-24","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"5b3d8d9ff43e4864c60000be"}
    end_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=9)).strftime('%Y-%m-%d')
    qdata_temlate = '{"fromDate":"%(from_date)s","toDate":"%(to_date)s","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['rateItems'][-3]['retention'][2]}


def query_sevendays_retentions():
    """用户七日留存"""
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/retention/view?relatedId={related_Id}'
    # {"fromDate":"2019-11-17","toDate":"2019-11-24","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"5b3d8d9ff43e4864c60000be"}
    end_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=9)).strftime('%Y-%m-%d')
    qdata_temlate = '{"fromDate":"%(from_date)s","toDate":"%(to_date)s","timeUnit":"day","page":1,"pageSize":30,"type":"newUser","view":"retention","channel":[],"version":[],"relatedId":"%(related_Id)s"}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['rateItems'][0]['retention'][-1]}

def query_video_supplement():
    '''查插屏數量'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    #{"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-20","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"ad_interstitial_from","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "ad_interstitial_from"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","channel":[],"version":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventLaunch']}


def query_video():
    '''查視頻數量及獨立人數'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    #{"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-20","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"watch_video","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "watch_video"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天_數量": data['data']['items'][1]['eventLaunch'],"昨天_人數": data['data']['items'][1]['eventDevice']}


def query_iap_users():
    '''查詢内購iap人數'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    #{"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-20","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"buy_iap_total","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "buy_iap_total"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_open_map2_users():
    '''查詢進入map2獨立用戶數'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    # {"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-21","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"open_map2","view":"eventSDetailView","page":1,"pageSize":30}  
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "open_map2"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_open_map3_users():
    '''查詢進入map3獨立用戶數'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    #{"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-21","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"open_map3","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "open_map3"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_open_event():
    '''查詢進入event獨立用戶數'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/detail?relatedId={related_Id}'
    #{"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-21","toDate":"2019-11-27","version":[],"channel":[],"timeUnit":"day","eventName":"open_event","view":"eventSDetailView","page":1,"pageSize":30}
    end_date = (today - timedelta(days=0)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    eventName = "open_event"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","view":"eventSDetailView","page":1,"pageSize":30}'
    qdata_str = qdata_temlate % {"from_date": start_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['eventDevice']}


def query_claim_times():
    '''查詢成功claim次數'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}'
    #{"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-26","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"show_claim","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    eventName = "show_claim"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}'
    qdata_str = qdata_temlate % {"from_date": end_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"昨天": data['data']['items'][1]['value']}

def query_unlock_business():
    '''查詢成功claim次數'''
    print(inspect.stack()[0][3])
    related_Id = "5b3d8d9ff43e4864c60000be"
    url = f'https://mobile.umeng.com/ht/api/v3/app/event/analysis/property/string/detail?relatedId={related_Id}'
    #{"relatedId":"5b3d8d9ff43e4864c60000be","fromDate":"2019-11-26","toDate":"2019-11-26","version":[],"channel":[],"timeUnit":"day","eventName":"unlock_business","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    eventName = "unlock_business"
    qdata_temlate = '{"relatedId":"%(related_Id)s","fromDate":"%(from_date)s","toDate":"%(to_date)s","version":[],"channel":[],"timeUnit":"day","eventName":"%(eventName)s","propertyName":"action","view":"propertyStringLaunchView","type":"propertyValue"}'
    qdata_str = qdata_temlate % {"from_date": end_date, "to_date": end_date,'related_Id': related_Id,'eventName':eventName}
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
    }
    resp = requests.post(url=url, data=qdata, headers=headers)
    data = resp.json()
    return {"business_5": data['data']['items'][3]['value'],"business_10": data['data']['items'][-1]['value']}

def query_iap_money():
    print(inspect.stack()[0][3])
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
    print(inspect.stack()[0][3])
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
    print(inspect.stack()[0][3])
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
    print(inspect.stack()[0][3])
    '''IAP购买次数'''
    i = 0
    j = 0
    data = query_iap_money()
    for i in range(len(data)):
        j += data[i]['num']
    return j


def calculate_iap_money_sum():
    print(inspect.stack()[0][3])
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
    print(inspect.stack()[0][3])
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

    try:
        resp = requests.post(url=url, data=qdata, headers=headers)
        data = resp.json()

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
    print(inspect.stack()[0][3])
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

    try:
        resp = requests.post(url=url, data=qdata_ecpm, headers=headers)
        data = resp.json()

        return {"昨天": data[-1]['ecpm'], "前天": data[-2]['ecpm'], '八天前': data[1]['ecpm']}
    except:
        print("ERROR: query_xi_back_gun")


# stat_platform_android()
# # print(query_xi_back_gun(app_name_tbc3_android, bundle_id_tbc3_android, platform_tbc3_android))
# print(query_xi_ecpm())
# print(query_xi_ecpm(country_us))

# stat_platform_android()
# print(query_xi_back_gun())

def test():
    stat_platform_android()
    print(query_claim_times())


test()
