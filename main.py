# -*- coding: utf-8 -*-

import requests
from const import *
from id import *
from datetime import datetime
from datetime import timedelta
from functions import *
from excel import *
from shutil import copyfile

# url = 'https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_chart_data?start_date=2019-08-10&end_date=2019-09-08&versions%5B%5D=&channels%5B%5D=&segments%5B%5D=&time_unit=daily&stats=active_users'
# https://mobile.umeng.com/apps/150000aed7d9a4f8eb9317b5/reports/load_chart_data?start_date=2019-09-07&end_date=2019-09-14&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=active_users


def main():
    copyfile(read_file_name, save_file_name)
    filename = save_file_name
    wb = open_excel(filename)
    save_to_ios(wb)
    save_to_android(wb)
    save_to_tbc3(wb)
    save_excel(wb)


if __name__ == "__main__":
    main()
    print("All Done!!!!")
    
