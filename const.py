# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta

base_url = 'https://mobile.umeng.com/apps'
xi_base_url = 'https://xi.harrybuy.com/es/monesimplify/pistolevent'

today_date = datetime.today()
today = today_date - timedelta(days=0)
yesterday_str = (today - timedelta(days=1)).strftime('%Y-%m-%d')
day_before_yesterday_str = (today - timedelta(days=2)).strftime('%Y-%m-%d')
nine_days_before_str = (today - timedelta(days=9)).strftime('%Y-%m-%d')
read_file_name = f"TBC3每日数据{day_before_yesterday_str}.xlsx"
save_file_name = f"TBC3每日数据{yesterday_str}.xlsx"

ad_play_dict_keys = ["FreeBonus_money",
                     "Offline",
                     "Double_Cash",
                     "skip_30_minutes",
                     "speedUp",
                     "cost_50%_off",
                     "Slot",
                     "AdClaim",
                     "FreeBonus_gold"]

product_id_iOS_unit_price = {
    'com.idlecapatalist.aovalw.goldspin': 0.99,
    'com.idlecapatalist.aovalw.offer7.99': 7.99,
    'com.idlecapatalist.aovalw.offer2.99': 2.99,
    'com.idlecapatalist.aovalw.gold4.99': 4.99,
    'com.idlecapatalist.aovalw.offer9.99': 9.99,
    'com.idlecapatalist.aovalw.gold9.99': 9.99,
    'com.idlecapatalist.aovalw.offer19.99': 19.99,
    'com.idlecapatalist.aovalw.gold19.99': 19.99,
    'com.idlecapatalist.aovalw.offer49.99': 49.99,
    'com.idlecapatalist.aovalw.gold49.99': 49.99,
    'com.idlecapatalist.aovalw.offer79.99': 79.99,
    'com.idlecapatalist.aovalw.gold99.99': 99.99,
    'com.idlecapatalist.aovalw.eventdeal19.99': 19.99
}

product_id_andriod_unit_price = {
    'com.brokenreality.tbc3.goldspin': 0.99,
    'com.brokenreality.tbc3.offer7.99': 7.99,
    'com.brokenreality.tbc3.offer2.99': 2.99,
    'com.brokenreality.tbc3.gold4.99': 4.99,
    'com.brokenreality.tbc3.offer9.99': 9.99,
    'com.brokenreality.tbc3.gold9.99': 9.99,
    'com.brokenreality.tbc3.offer19.99': 19.99,
    'com.brokenreality.tbc3.gold19.99': 19.99,
    'com.brokenreality.tbc3.offer49.99': 49.99,
    'com.brokenreality.tbc3.gold49.99': 49.99,
    'com.brokenreality.tbc3.offer79.99': 79.99,
    'com.brokenreality.tbc3.gold99.99': 99.99,
    'com.brokenreality.tbc3.christmasoffer': 19.99
}
