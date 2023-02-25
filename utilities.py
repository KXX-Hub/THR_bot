"""This python will handle some extra functions."""
import sys
from os.path import exists

import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | Auto_bot_test                        |
# | Made by KXX (MIT License)            |
# ++--------------------------------++
# 輸入起訖站
# |  南港  台北  板橋  桃園  新竹  苗栗      |
# |  台中  彰化  雲林  嘉義  台南  左營      |
start_station : '台北'
end_station : '左營'
# -------------------------------------------
# 輸入出發時間 
# | 00:00 00:30 01:00 01:30 02:00 02:30 03:00 03:30 04:00 04:30 |
# | 05:00 05:30 06:00 06:30 07:00 07:30 08:00 08:30 09:00 09:30 |
# | 10:00 10:30 11:00 11:30 12:00 12:30 13:00 13:30 14:00 14:30 |
# | 15:00 15:30 16:00 16:30 17:00 17:30 18:00 18:30 19:00 19:30 |
# | 20:00 20:30 21:00 21:30 22:00 22:30 23:00 23:30 24:00 24:30 |
start_time : '00:00'
# -------------------------------------------
# 輸入票種及數量，沒有則填0
regular_ticket : '0' #全票
children_ticket : '0' #孩童票
disabled_ticket : '0' #愛心票
student_ticket : '0'  #大學生票
senior_persons_ticket : '0' #敬老票
"""
                )
    sys.exit()


def read_config():
    """Read config file.
    Check if config file exists, if not, create one.
    if exists, read config file and return config with dict type.
    :rtype: dict
    """
    if not exists('./config.yml'):
        print("Config file not found, create one by default.\nPlease finish filling config.yml")
        with open('config.yml', 'w', encoding="utf8"):
            config_file_generator()

    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            start_station = get_start_station(data['start_station'])
            end_station = get_end_station(data['end_station'])
            start_time = get_start_time(data['start_time'])
            config = {
                'start_station': start_station,
                'end_station': end_station,
                'start_time': start_time
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()


time_list = [
    '00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30',
    '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
    '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30',
    '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '24:00'
]
station_list = [
    '南港', '台北', '板橋', '桃園', '新竹', '苗栗',
    '台中', '彰化', '雲林', '嘉義', '台南', '左營'
]


def get_start_station(start_station):
    start_station = station_list.index(start_station) + 1
    return start_station


def get_end_station(end_station):
    end_station = station_list.index(end_station) + 1
    return end_station


def get_start_time(start_time):
    start_time = time_list.index(start_time) + 2
    return start_time

