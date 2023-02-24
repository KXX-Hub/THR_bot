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
start_station : ''
end_station : ''
# 輸入出發時間 
# | 00:00 00:30 01:00 01:30 02:00 02:30 03:00 03:30 04:00 04:30 |
# | 05:00 05:30 06:00 06:30 07:00 07:30 08:00 08:30 09:00 09:30 |
# | 10:00 10:30 11:00 11:30 12:00 12:30 13:00 13:30 14:00 14:30 |
# | 15:00 15:30 16:00 16:30 17:00 17:30 18:00 18:30 19:00 19:30 |
# | 20:00 20:30 21:00 21:30 22:00 22:30 23:00 23:30 24:00 24:30 |

start_time : ''
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
            start = get_start_station(data['start_station'])
            end = get_end_station(data['end_station'])
            config = {
                'start_station': start,
                'end_station': end,
                'start_time' :data['start_time']
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()


def get_start_station(start):
    if start == "南港":
        start = 1
    elif start == "台北":
        start = 2
    elif start == "板橋":
        start = 3
    elif start == "桃園":
        start = 4
    elif start == "新竹":
        start = 5
    elif start == "苗栗":
        start = 6
    elif start == "台中":
        start = 7
    elif start == "彰化":
        start = 8
    elif start == "雲林":
        start = 9
    elif start == "嘉義":
        start = 10
    elif start == "台南":
        start = 11
    elif start == "左營":
        start = 12
    return start


def get_end_station(end):
    if end == "南港":
        end = 1
    elif end == "台北":
        end = 2
    elif end == "板橋":
        end = 3
    elif end == "桃園":
        end = 4
    elif end == "新竹":
        end = 5
    elif end == "苗栗":
        end = 6
    elif end == "台中":
        end = 7
    elif end == "彰化":
        end = 8
    elif end == "雲林":
        end = 9
    elif end == "嘉義":
        end = 10
    elif end == "台南":
        end = 11
    elif end == "左營":
        end = 12
    return end


#time_dict = {
#    '00:00': 2, '00:30': 3, '01:00': 4, '01:30': 5, '02:00': 6, '02:30': 7, '03:00': 8, '03:30': 9, '04:00': 10,
#
#    '04:30': 11,
#    '05:00': 12, '05:30': 13, '06:00': 14, '06:30': 15, '07:00': 16, '07:30': 17, '08:00': 18, '08:30': 19, '09:00': 20,
#    '09:30': 21,
#}


def get_start_time(time):
    if time == "00:00":
        time = 2
    elif time == "00:30":
        time = 3
    elif time == "01:00":
        time = 4
    elif time == "01:30":
        time = 5
    elif time == "02:00":
        time = 6
    elif time == "02:30":
        time = 7
    elif time == "03:30":
        time = 8
    elif time == "04:00":
        time = 9
    elif time == "05:00":
        time = 10
    elif time == "05:30":
        time = 11
    elif time == "06:00":
        time = 12
    elif time == "06:30":
        time = 13
    elif time == "07:00":
        time = 14
    return time
