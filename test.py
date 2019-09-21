from functions import *
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
data10 =  ()
data11 = query_open_event()
data12 = query_claim_times()
data13 = query_iap_money()
###############

# 数据计算
value_E = data['昨天'][0] / data['昨天'][1]  # E列生命周期
value_L = data4 ['昨天'] / data['昨天'][0]   # L列日活启动次数
value_M = data5['昨天'][0]/ data['昨天'][0]  # M列日活视频次数
value_N = data5['昨天'][0]/ data5['昨天'][1]  # N列独立用户视频次数
value_Y = (data5['昨天'][0]+data6['昨天'])/data['昨天'][0]        # Y列人均视频+插频次数


print(data13)