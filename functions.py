import requests
from const import *
from id import *
from datetime import datetime
from datetime import timedelta
import json
from collections import namedtuple
from result import *


url_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=%(stats_type)s'
url_event_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&stats=%(stats_type)s&event_group_id=%(event_group_id)s'
url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&%(event_id)s&%(event_group_id)s&%(event_group_name)s&stats=%(stats_type)s&property_type=string'

today = datetime.today()
interval = 8

cookies = {'JSESSIONID': '6A5D190CC2D4BDDB173828B8ED74C9C8',
           'PHPSESSID': 'e25rks4rchtepldv23flhc7l82',
           'UM_distinctid': '16d10cf0765141-056e45dadb0c15-5373e62-240000-16d10cf0766e88',
           'isg': 'BDg4JMX1ke6pr_1rzd7ZoTXeCebKoZwr3WE1I3KpHXMmjdl3GrIdulXlQc2Y3VQD',
           'uc_session_id': 'be1aa0ff-4855-49d0-98d8-796308b6cc09',
           'um_lang': 'zh',
           'ummo_ss': 'BAh7CEkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjoGRVRbCEkiCVVzZXIGOwBGWwZvOhNCU09OOjpPYmplY3RJZAY6CkBkYXRhWxFpYmkxaVppAZppXGkSaQHzaQGTaT5pAGkKaXRJIhk4UVA3eElpcW1PaGRXdG1HUFpQawY7AFRJIhR1bXBsdXNfdWNfdG9rZW4GOwBGIj0xVjNhb1pHRkpZcnJnNVA3VGpWd2F6UV8wYmI1ZDVkNDM5YTU0NjIwYTNhOWQ0NWU3ODgxNDE1N0kiD3Nlc3Npb25faWQGOwBUSSIlMDQ1ODJkYWRmOWY2MTAxOGRjMWU4ZmM1OTJlMzBkOGUGOwBG--243cef22fcee4c238eac801bc9d3b42fc5eac4a4',
           'umplus_uc_loginid': 'fangfang_ren',
           'umplus_uc_token': '1V3aoZGFJYrrg5P7TjVwazQ_0bb5d5d439a54620a3a9d45e78814157'}


def query_active_users():
    """查日活/新增"""
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-06&end_date=2019-09-14&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=active
    stats_type = 'active'
    report_type = 'game_reports'
    end_date = today.strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=interval)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": [data['stats'][1]['active'], data['stats'][1]['install']], "前天": [data['stats'][2]['active'], data['stats'][2]['install']], '八天前': [data['stats'][-1]['active'], data['stats'][-1]['install']]}


def query_launches_times():
    """启动次数"""
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-06&end_date=2019-09-14&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=launches
    stats_type = 'launches'
    report_type = 'reports'
    end_date = today.strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=interval)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][1]['data'], "前天": data['stats'][2]['data'], '八天前': data['stats'][-1]['data']}


def query_morrow_retentions():
    """用户次日留存"""
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-09&end_date=2019-09-15&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=retentions
    stats_type = 'retentions'
    report_type = 'reports'
    end_date = (today -timedelta(days=2)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=9)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][-1]['retention_rate'][0], "前天": data['stats'][-2]['retention_rate'][0], '八天前': data['stats'][0]['retention_rate'][0]}

def query_threedays_retentions():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-04&end_date=2019-09-15&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=retentions
    stats_type = 'retentions'
    report_type = 'reports'
    end_date = (today -timedelta(days=4)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=11)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type,'event_group_id':event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][7]['retention_rate'][2], "前天": data['stats'][6]['retention_rate'][2], '八天前': data['stats'][0]['retention_rate'][2]}

def query_sevendays_retentions():    
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_table_data?start_date=2019-09-01&end_date=2019-09-15&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=retentions
    stats_type = 'retentions'
    report_type = 'reports'
    end_date = (today -timedelta(days=7)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=14)).strftime('%Y-%m-%d')
    url = url_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][6]['retention_rate'][6], "前天": data['stats'][5]['retention_rate'][6], '八天前': data['stats'][0]['retention_rate'][6]}

def query_video_supplement():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b7289ddf43e4838c7000268
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_ad_interstitial_from
    end_date = (today -timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type,'event_group_id':event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['count'], "前天": data['stats'][1]['count'], '八天前': data['stats'][-1]['count']}
    
def query_video():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b7289a4f43e487686000096
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_watch_video
    end_date = (today -timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type,'event_group_id':event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": [data['stats'][0]['count'], data['stats'][0]['device']], "前天": [data['stats'][1]['count'],data['stats'][1]['device']], '八天前': [data['stats'][-1]['count'],data['stats'][-1]['device']]}

def query_iap_users():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b84cc7ca40fa34b91000015
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_iap
    end_date = (today -timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type,'event_group_id':event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}

def query_open_map2_users():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?&start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b84cc7ca40fa34b91000019
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_open_map2
    end_date = (today -timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type,'event_group_id':event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}

def query_open_map3_users():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-09&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b9a2569b27b0a5cb8000054
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_open_map3
    end_date = (today -timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type,'event_group_id':event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}

def query_open_event():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-07&end_date=2019-09-15&channels[]=&versions[]=&stats=event_group_trend&event_group_id=5b7289ddf43e4838c7000282
    stats_type = 'event_group_trend'
    report_type = 'events'
    event_group_id = event_group_id_open_event
    end_date = (today -timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=8)).strftime('%Y-%m-%d')
    url = url_event_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                         'start_date': start_date, 'end_date': end_date, 'stats_type': stats_type,'event_group_id':event_group_id}
    resp = requests.get(url=url, cookies=cookies)
    data = resp.json()
    return {"昨天": data['stats'][0]['device'], "前天": data['stats'][1]['device'], '八天前': data['stats'][-1]['device']}

def query_claim_times():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-09&end_date=2019-09-15&channels[]=&versions[]=&event_id=5b7be0660237f6071568cc54&event_group_id=5b7289ddf43e4838c7000289&event_group_name=show_claim&stats=count_distribute&property_type=string
    stats_type = 'count_distribute'
    report_type = 'events'
    event_id = event_id_show_claim
    event_group_id = event_group_id_show_claim
    event_group_name = 'show_claim'
    days = [1,2,8]
    response=[]
    i = 0
    for day in days:
        end_date = (today -timedelta(days=day)).strftime('%Y-%m-%d')
        start_date =end_date
        url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&event_id=%(event_id)s&event_group_id=%(event_group_id)s&event_group_name=%(event_group_name)s&stats=%(stats_type)s&property_type=string'

        url = url_eventname_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                                   'start_date': start_date, 'end_date': end_date, 'event_id': event_id,
                                   'event_group_id':event_group_id,'event_group_name': event_group_name,'stats_type': stats_type}
        resp = requests.get(url=url, cookies=cookies)
        data = resp.json()
        response.append(data['stats'][1]['num'])
        i+=1
    return {"昨天": response[0], "前天": response[1], '八天前': response[2]}

def query_unlock_business():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-14&end_date=2019-09-14&channels[]=&versions[]=&event_id=5b7bdfa20237f6071568cc50&event_group_id=5b7289ddf43e4838c7000295&event_group_name=unlock_business&stats=count_distribute&property_type=string
    stats_type = 'count_distribute'
    report_type = 'events'
    event_id = event_id_unlock_business
    event_group_id = event_group_id_unlock_business
    event_group_name = 'unlock_business'
    days = [1,2,8]
    response=[]
    i = 0
    for day in days:
        end_date = (today -timedelta(days=day)).strftime('%Y-%m-%d')
        start_date =end_date
        url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&event_id=%(event_id)s&event_group_id=%(event_group_id)s&event_group_name=%(event_group_name)s&stats=%(stats_type)s&property_type=string'

        url = url_eventname_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                                   'start_date': start_date, 'end_date': end_date, 'event_id': event_id,
                                   'event_group_id':event_group_id,'event_group_name': event_group_name,'stats_type': stats_type}
        resp = requests.get(url=url, cookies=cookies)
        data = resp.json()
        response.append([data['stats'][3]['num'],data['stats'][-1]['num']])
        i+=1
    return {"昨天": response[0], "前天": response[1], '八天前': response[2]}

def query_iap_money():
    # https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/events/load_table_data?start_date=2019-09-14&end_date=2019-09-14&channels[]=&versions[]=&event_id=5b9f7401c37c58067735ebc0&event_group_id=5b84cc7ca40fa34b91000015&event_group_name=buy_iap_total&stats=count_distribute&property_type=string
    stats_type = 'count_distribute'
    report_type = 'events'
    event_id = event_id_buy_iap_total
    event_group_id = event_group_id_buy_iap_total
    event_group_name = 'buy_iap_total'
    days = [1,2,8]
    response=[]
    i = 0
    for day in days:
        group=[]
        end_date = (today -timedelta(days=day)).strftime('%Y-%m-%d')
        start_date =end_date
        url_eventname_temlate = '%(base_url)s/%(id)s/%(report_type)s/load_table_data?start_date=%(start_date)s&end_date=%(end_date)s&channels[]=&versions[]=&event_id=%(event_id)s&event_group_id=%(event_group_id)s&event_group_name=%(event_group_name)s&stats=%(stats_type)s&property_type=string'

        url = url_eventname_temlate % {"base_url": base_url, "id": id_tbc_ios, 'report_type': report_type,
                                   'start_date': start_date, 'end_date': end_date, 'event_id': event_id,
                                   'event_group_id':event_group_id,'event_group_name': event_group_name,'stats_type': stats_type}
        resp = requests.get(url=url, cookies=cookies)
        data = resp.json()
        for d in data['stats']:
            group.append({'label':d['label'],'num':d['num']})
        response.append(group)
        i+=1
    return {"昨天": response[0], "前天": response[1], '八天前': response[2]}



print(query_iap_money())   